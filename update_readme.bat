@echo off
setlocal EnableDelayedExpansion
REM ============================================================
REM  Auto-updater for metadata + README
REM  Works regardless of current working directory
REM ============================================================

REM --- Resolve to this script's directory
set "SCRIPT_DIR=%~dp0"
pushd "%SCRIPT_DIR%"

REM --- Configurable paths (relative to this script)
set "PYTHON=python"
set "SCRAPER_OUT=\Users\ephel\Development\store-scraper\out"
set "METADATA_SCRIPT=%SCRIPT_DIR%build_metadata.py"
set "README_SCRIPT=%SCRIPT_DIR%update_readme.py"
set "CLEANUP_SCRIPT=%SCRIPT_DIR%clean_names.py"
set "METADATA_FILE=%SCRIPT_DIR%metadata.json"
set "README_FILE=%SCRIPT_DIR%README.md"

echo.
echo [94mChecking for required files...[0m
echo.
REM --- Sanity checks
if not exist "%SCRAPER_OUT%\" (
    echo [91mMissing folder: "%SCRAPER_OUT%"[0m
    popd
    exit /b 1
)
if not exist "%METADATA_SCRIPT%" (
    echo [91mMissing file: "%METADATA_SCRIPT%"[0m
    popd
    exit /b 1
)
if not exist "%README_SCRIPT%" (
    echo [91mMissing file: "%README_SCRIPT%"[0m
    popd
    exit /b 1
)
if not exist "%CLEANUP_SCRIPT%" (
    echo [91mMissing file: "%CLEANUP_SCRIPT%"[0m
    popd
    exit /b 1
)

echo.
echo [92m[1/4] Copying scraper output into the catalog[0m
REM /E copies real files and never deletes from the destination.
REM Never use /MIR here: it deletes everything not in out\ (.git, scripts).
REM robocopy: 0-7 = success (1 = files copied), 8+ = failure
robocopy "%SCRAPER_OUT%" "%SCRIPT_DIR%." /E /NFL /NDL /NJH /NP
if errorlevel 8 (
    echo [91mCopy failed[0m
    popd
    exit /b 1
)
REM --- xbox-console and xbox-pc mirror out\xbox (they used to be junctions to it)
for %%D in (xbox-console xbox-pc) do (
    robocopy "%SCRAPER_OUT%\xbox" "%SCRIPT_DIR%%%D" /E /NFL /NDL /NJH /NJS /NP >nul
    if errorlevel 8 (
        echo [91mCopy to %%D failed[0m
        popd
        exit /b 1
    )
)

echo.
echo [92m[2/4] Cleaning names in JSON files[0m
"%PYTHON%" "%CLEANUP_SCRIPT%"
if errorlevel 1 (
    echo [91mName cleanup failed[0m
    popd
    exit /b 1
)

echo.
echo [92m[3/4] Building metadata.json[0m
"%PYTHON%" "%METADATA_SCRIPT%" -o "%METADATA_FILE%"
if errorlevel 1 (
    echo [91mMetadata build failed[0m
    popd
    exit /b 1
)

echo.
echo [92m[4/4] Updating README markers[0m
"%PYTHON%" "%README_SCRIPT%" "%README_FILE%" -v "%METADATA_FILE%" -i -f --warn-missing
if errorlevel 1 (
    echo [91mREADME update failed[0m
    popd
    exit /b 1
)

echo.
echo [92mAll updates complete[0m
popd
endlocal
exit /b 0
