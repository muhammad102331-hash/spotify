# 🎵 Spotify Data Analysis Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive exploratory data analysis (EDA) project on Spotify music data, featuring interactive visualizations, statistical insights, and an automated Streamlit dashboard.

![Spotify Analysis](https://img.shields.io/badge/Music-Analysis-1DB954?style=for-the-badge&logo=spotify)

---

## 📊 Project Overview

This project analyzes Spotify music data to uncover insights about:
- Song popularity patterns
- Artist performance metrics
- Temporal trends in music releases
- Content type analysis (explicit vs non-explicit)
- Album type distributions
- Duration patterns

**Key Metrics:**
- 📈 **783** unique songs analyzed
- 🎤 **335** distinct artists
- ⭐ **89.65** average popularity score
- ⏱️ **3.28** minutes average song duration

---

## 🚀 Features

### 1. Interactive Streamlit Dashboard
- Real-time data filtering and exploration
- 5 comprehensive analysis tabs
- Interactive Plotly visualizations
- Export functionality for filtered data

### 2. Jupyter Notebook Analysis
- Step-by-step exploratory data analysis
- Statistical summaries and visualizations
- Detailed insights and findings

### 3. Professional Reporting
- Executive summary document
- Business insights and recommendations
- Ready-to-present findings

---

## 📁 Project Structure

```
spotify/
│
├── 📊 Data/
│   └── spotify .csv                    # Dataset (not included in repo)
│
├── 📓 Notebooks/
│   └── spotify.ipynb                   # Jupyter notebook with full EDA
│
├── 🖥️ Dashboard/
│   └── streamlit_app.py                # Streamlit web application
│
├── 📄 Reports/
│   └── Spotify_Analysis_Summary.md     # Executive summary report
│
├── 📋 Documentation/
│   ├── README_STREAMLIT.md             # Streamlit app documentation
│   └── Bussiness Requirements.docx     # Project requirements
│
├── 📦 Configuration/
│   ├── requirements.txt                # Python dependencies
│   └── .gitignore                      # Git ignore rules
│
└── README.md                           # This file
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/spotify-analysis.git
cd spotify-analysis
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your data**
- Place your Spotify CSV file in the project root
- Update the file path in `streamlit_app.py` if needed

---

## 🎯 Usage

### Run Streamlit Dashboard
```bash
streamlit run streamlit_app.py
```
The dashboard will open automatically at `http://localhost:8501`

### Explore Jupyter Notebook
```bash
jupyter notebook spotify.ipynb
```

---

## 📊 Dashboard Features

### Overview Tab
- Key Performance Indicators (KPIs)
- Popularity and duration distributions
- Album type breakdown
- Explicit vs non-explicit comparison

### Artists Tab
- Top N artists by popularity (adjustable)
- Artist statistics and metrics
- Individual artist deep-dive analysis
- Top songs per artist

### Time Trends Tab
- Monthly popularity patterns
- Yearly release trends
- Average popularity over time
- Heatmap visualizations

### Song Analysis Tab
- Top 20 most popular songs
- Correlation analysis
- Popularity vs duration relationships
- Statistical summaries

### Data Table Tab
- Searchable data interface
- Column selection
- CSV export functionality

---

## 📈 Key Findings

### Top Performing Artists
1. **Grupo Frontera & Bad Bunny**
2. **Jung Kook & Latto**
3. **leftovermax**
4. **Yng Lvcas & Peso Pluma**
5. **FIFTY FIFTY**

### Content Insights
- **59.7%** of tracks are non-explicit
- **62.0%** of releases are full albums
- **37.9%** are singles
- Average song duration aligns with industry standards (3.28 min)

### Popularity Trends
- High overall popularity (89.65 average)
- Seasonal variations in song performance
- Year-over-year growth in releases

---

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Static visualizations
- **Plotly** - Interactive charts
- **Streamlit** - Web dashboard framework
- **Jupyter** - Interactive development environment

---

## 📝 Requirements

```txt
streamlit
pandas
numpy
matplotlib
seaborn
plotly
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- Spotify for providing the data platform
- The Python data science community
- All contributors to the open-source libraries used

---

## 📧 Contact

For questions or feedback, please open an issue or contact [your.email@example.com](mailto:your.email@example.com)

---

## 🔮 Future Enhancements

- [ ] Add genre-based analysis
- [ ] Implement predictive modeling for song popularity
- [ ] Include audio feature analysis (tempo, key, energy)
- [ ] Add geographic/regional comparisons
- [ ] Integrate with Spotify API for real-time data
- [ ] Create automated reporting pipeline
- [ ] Add machine learning recommendations

---

<div align="center">

**Made with ❤️ and 🎵**

⭐ Star this repo if you find it helpful!

</div>
