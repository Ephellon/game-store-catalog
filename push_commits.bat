@echo off
setlocal EnableDelayedExpansion
REM ============================================================
REM  Push commits to origin
REM  Works regardless of current working directory
REM  (update_readme.bat copies the scraper output in first)
REM ============================================================

REM --- Resolve to this script's directory so git targets this repo
pushd "%~dp0"

echo.
echo [92m[1/3] Staging files...[0m
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
echo [92m[2/3] Committing with message...[0m
git commit -m "Catalog update"
if errorlevel 1 (
    echo [91mCommit failed[0m
    popd
    exit /b 2
)

echo.
echo [92m[3/3] Pushing to origin/main[0m
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
