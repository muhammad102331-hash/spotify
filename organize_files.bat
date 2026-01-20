@echo off
REM Organize Spotify Project Files into Folders

echo ========================================
echo   Organizing Spotify Project Files
echo ========================================
echo.

REM Move notebook to notebooks folder
if exist "spotify.ipynb" (
    move "spotify.ipynb" "notebooks\"
    echo [OK] Moved spotify.ipynb to notebooks/
)

REM Move streamlit app to dashboard folder
if exist "streamlit_app.py" (
    move "streamlit_app.py" "dashboard\"
    echo [OK] Moved streamlit_app.py to dashboard/
)

REM Move reports to reports folder
if exist "Spotify_Analysis_Summary.md" (
    move "Spotify_Analysis_Summary.md" "reports\"
    echo [OK] Moved Spotify_Analysis_Summary.md to reports/
)

REM Move documentation to docs folder
if exist "README_STREAMLIT.md" (
    move "README_STREAMLIT.md" "docs\"
    echo [OK] Moved README_STREAMLIT.md to docs/
)

if exist "GITHUB_SETUP.md" (
    move "GITHUB_SETUP.md" "docs\"
    echo [OK] Moved GITHUB_SETUP.md to docs/
)

if exist "Bussiness Requirements.docx" (
    move "Bussiness Requirements.docx" "docs\"
    echo [OK] Moved Bussiness Requirements.docx to docs/
)

REM Move data files to data folder
if exist "spotify .csv" (
    move "spotify .csv" "data\"
    echo [OK] Moved spotify .csv to data/
)

REM Move Power BI to assets folder
if exist "spotify.pbix" (
    move "spotify.pbix" "assets\"
    echo [OK] Moved spotify.pbix to assets/
)

echo.
echo ========================================
echo   Organization Complete!
echo ========================================
echo.
echo New folder structure:
echo   notebooks/       - Jupyter notebooks
echo   dashboard/       - Streamlit app
echo   reports/         - Analysis reports
echo   docs/            - Documentation
echo   data/            - Data files (excluded from Git)
echo   assets/          - Additional resources
echo.
pause
