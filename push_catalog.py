#!/usr/bin/env python
"""Commit and push catalog updates to GitHub.

Replaces the Claude Haiku step of the "\\Personal\\Game Store Catalog"
scheduled task. Runs as action 3 of that task (after --update.bat and
update_readme.bat), and standalone every Sunday at 09:00 local time via
"\\Personal\\Push Game Store Catalog".

git is invoked directly (no shell, no PowerShell) because spawning a
PowerShell instance intermittently stalls for minutes on this machine.

Exit codes:
    0  pushed, or nothing to push
    1  a git command failed
    2  README.md was not part of the staged changes -- paused and flagged
"""

from __future__ import annotations

import ctypes
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
REMOTE = "origin"
BRANCH = "main"
SUMMARY = "Catalog update"
MESSAGE = "Games have been updated."
README = "README.md"

# Matches the repo's ".*.*" .gitignore rule, so the log never self-commits.
LOG_FILE = REPO / ".push_catalog.log"

GIT_TIMEOUT = 120       # seconds, local operations
PUSH_TIMEOUT = 600      # seconds, network operations

MB_OK = 0x00000000
MB_ICONWARNING = 0x00000030
MB_SYSTEMMODAL = 0x00001000


def log(message: str) -> None:
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    print(line, flush=True)
    with LOG_FILE.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def flag(title: str, body: str) -> None:
    """Log a blocking problem and raise a modal dialog for the user.

    BurntToast is deliberately not used here: it would require spawning
    powershell.exe, which is the stall this script exists to avoid.
    """
    log(f"FLAG: {title} -- {body}")
    try:
        ctypes.windll.user32.MessageBoxW(
            None, body, f"Game Store Catalog: {title}",
            MB_OK | MB_ICONWARNING | MB_SYSTEMMODAL,
        )
    except Exception as error:  # headless session, no window station, etc.
        log(f"could not show dialog ({error}); see this log instead")


def find_git() -> str:
    found = shutil.which("git")
    if found:
        return found
    for candidate in (
        r"C:\Program Files\Git\cmd\git.exe",
        r"C:\Program Files\Git\mingw64\bin\git.exe",
    ):
        if Path(candidate).is_file():
            return candidate
    raise FileNotFoundError("git.exe not found on PATH or in the usual install locations")


def git(exe: str, *args: str, timeout: int = GIT_TIMEOUT) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    # Fail fast instead of blocking on a credential prompt in a headless run.
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["GIT_OPTIONAL_LOCKS"] = "0"

    log(f"$ git {' '.join(args)}")
    result = subprocess.run(
        [exe, *args],
        cwd=REPO,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        shell=False,
    )
    for stream in (result.stdout, result.stderr):
        for line in (stream or "").splitlines():
            if line.strip():
                log(f"  {line.rstrip()}")
    return result


def main() -> int:
    log(f"--- push_catalog starting in {REPO}")

    try:
        exe = find_git()
    except FileNotFoundError as error:
        flag("git missing", str(error))
        return 1
    log(f"using {exe}")

    if git(exe, "rev-parse", "--is-inside-work-tree").returncode != 0:
        flag("not a repository", f"{REPO} is not a git working tree; nothing was pushed.")
        return 1

    if git(exe, "add", "-A").returncode != 0:
        flag("staging failed", "git add -A failed. See .push_catalog.log for the git output.")
        return 1

    staged = git(exe, "diff", "--cached", "--name-only")
    if staged.returncode != 0:
        flag("staging check failed", "git diff --cached failed. See .push_catalog.log.")
        return 1
    files = [line.strip() for line in staged.stdout.splitlines() if line.strip()]

    if not files:
        log("no staged changes")
        ahead = git(exe, "rev-list", "--count", f"{REMOTE}/{BRANCH}..{BRANCH}")
        pending = ahead.stdout.strip() if ahead.returncode == 0 else "0"
        if pending.isdigit() and int(pending) > 0:
            log(f"{pending} local commit(s) not on {REMOTE}/{BRANCH}; pushing those")
        else:
            log("nothing to commit and nothing to push -- done")
            return 0
    else:
        log(f"{len(files)} file(s) staged")
        if README not in files:
            flag(
                "README not updated",
                f"{len(files)} file(s) are staged but {README} is not among them, so "
                "update_readme.bat probably did not run or made no change.\n\n"
                "Nothing was committed or pushed. The changes are left staged for "
                f"inspection.\n\nLog: {LOG_FILE}",
            )
            return 2
        log(f"{README} is staged")

        commit = git(exe, "commit", "-m", SUMMARY, "-m", MESSAGE)
        if commit.returncode != 0:
            flag("commit failed", "git commit failed. See .push_catalog.log for the git output.")
            return 1

    if git(exe, "push", REMOTE, BRANCH, timeout=PUSH_TIMEOUT).returncode != 0:
        flag(
            "push failed",
            f"git push {REMOTE} {BRANCH} failed -- the commit is local only.\n\n"
            f"Log: {LOG_FILE}",
        )
        return 1

    log(f"pushed to {REMOTE}/{BRANCH} -- done")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except subprocess.TimeoutExpired as error:
        flag("git timed out", f"{error.cmd} exceeded {error.timeout}s and was killed.")
        sys.exit(1)
    except Exception as error:  # last resort -- never die silently in a scheduled run
        flag("unexpected error", f"{type(error).__name__}: {error}")
        sys.exit(1)
