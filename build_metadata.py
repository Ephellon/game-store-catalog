#!/usr/bin/env python3
"""Collect each store's summary ($.json) into one metadata.json.

Every store folder (psn, steam, xbox, ...) holds a `$.json` written by
store-scraper:

    {"size": 18147, "diff": 0, "date": "2026-09-27T06:53:09.361Z"}

The output nests them by folder name, so update_readme.py can resolve
markers like <!--@psn.size--> or <!--@xbox.diff|s-->:

    {"psn": {"size": 18147, "diff": 0, "date": "..."}, ...}
"""
import argparse, json, sys
from pathlib import Path

SUMMARY = "$.json"

def collect(root):
    data = {}
    for d in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")):
        f = d / SUMMARY
        if not f.is_file():
            continue
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data[d.name] = json.load(fh)
        except (OSError, json.JSONDecodeError) as e:
            print(f"\tSkipping {f}: {e}", file=sys.stderr)
    return data

def main():
    ap = argparse.ArgumentParser(description=f"Merge every <store>/{SUMMARY} into one metadata file")
    ap.add_argument("-r", "--root", default=Path(__file__).resolve().parent, type=Path,
                    help="Catalog folder containing the store folders (default: this script's folder)")
    ap.add_argument("-o", "--output", help="Write here instead of stdout")
    args = ap.parse_args()

    data = collect(args.root)
    if not data:
        print(f"No {SUMMARY} files found under {args.root}", file=sys.stderr)
        return 1

    text = json.dumps(data, indent=4, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8", newline="")
        print(f"\tWrote {len(data)} stores: {', '.join(data)}")
    else:
        sys.stdout.write(text)
    return 0

if __name__ == "__main__":
    sys.exit(main())
