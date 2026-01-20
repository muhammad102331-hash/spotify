#!/bin/bash
# Organize Spotify Project Files into Folders

echo "========================================"
echo "  Organizing Spotify Project Files"
echo "========================================"
echo

# Move notebook to notebooks folder
if [ -f "spotify.ipynb" ]; then
    mv "spotify.ipynb" "notebooks/"
    echo "[OK] Moved spotify.ipynb to notebooks/"
fi

# Move streamlit app to dashboard folder
if [ -f "streamlit_app.py" ]; then
    mv "streamlit_app.py" "dashboard/"
    echo "[OK] Moved streamlit_app.py to dashboard/"
fi

# Move reports to reports folder
if [ -f "Spotify_Analysis_Summary.md" ]; then
    mv "Spotify_Analysis_Summary.md" "reports/"
    echo "[OK] Moved Spotify_Analysis_Summary.md to reports/"
fi

# Move documentation to docs folder
if [ -f "README_STREAMLIT.md" ]; then
    mv "README_STREAMLIT.md" "docs/"
    echo "[OK] Moved README_STREAMLIT.md to docs/"
fi

if [ -f "GITHUB_SETUP.md" ]; then
    mv "GITHUB_SETUP.md" "docs/"
    echo "[OK] Moved GITHUB_SETUP.md to docs/"
fi

if [ -f "Bussiness Requirements.docx" ]; then
    mv "Bussiness Requirements.docx" "docs/"
    echo "[OK] Moved Bussiness Requirements.docx to docs/"
fi

# Move data files to data folder
if [ -f "spotify .csv" ]; then
    mv "spotify .csv" "data/"
    echo "[OK] Moved spotify .csv to data/"
fi

# Move Power BI to assets folder
if [ -f "spotify.pbix" ]; then
    mv "spotify.pbix" "assets/"
    echo "[OK] Moved spotify.pbix to assets/"
fi

echo
echo "========================================"
echo "  Organization Complete!"
echo "========================================"
echo
echo "New folder structure:"
echo "  notebooks/       - Jupyter notebooks"
echo "  dashboard/       - Streamlit app"
echo "  reports/         - Analysis reports"
echo "  docs/            - Documentation"
echo "  data/            - Data files (excluded from Git)"
echo "  assets/          - Additional resources"
echo
