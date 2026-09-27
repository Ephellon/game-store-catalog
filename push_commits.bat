@echo off
setlocal EnableDelayedExpansion
REM ============================================================
REM  Push commits to origin
REM  Works regardless of current working directory
REM ============================================================

REM --- Resolve to this script's directory so git targets this repo
pushd "%~dp0"

echo.
echo [92m[1/4] Robocopying files...[0m
REM /E copies real files and never deletes from the destination.
REM Never use /MIR here: it deletes everything not in out\ (.git, scripts).
robocopy "\Users\ephel\Development\store-scraper\out" "%~dp0." /E
REM robocopy: 0-7 = success (1 = files copied), 8+ = failure
if errorlevel 8 (
    echo [91mRobocopy failed[0m
    popd
    exit /b 1
)

echo.
echo [92m[2/4] Staging files...[0m
git add -A
if errorlevel 1 (
    echo [91mStaging failed[0m
    popd
    exit /b 1
)

REM --- Nothing staged means nothing to commit; not an error
git diff --cached --quiet
if not errorlevel 1 (
    echo.
    echo [93mNo changes to commit[0m
    popd
    exit /b 0
)

echo.
echo [92m[3/4] Committing with message...[0m
git commit -m "Catalog update"
if errorlevel 1 (
    echo [91mCommit failed[0m
    popd
    exit /b 2
)

echo.
echo [92m[4/4] Pushing to origin/main[0m
git push origin main
if errorlevel 1 (
    echo [91mPush failed[0m
    popd
    exit /b 3
)

echo.
echo [92mCommit complete[0m
popd
endlocal
exit /b 0
