# Spotify EDA Streamlit Dashboard

## 🚀 Quick Start

### 1. Install Required Packages
```bash
pip install -r requirements.txt
```

### 2. Run the Dashboard
```bash
streamlit run streamlit_app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

---

## 📊 Features

### Interactive Filters (Sidebar)
- **Year Selection**: Filter data by specific years
- **Artist Selection**: Focus on specific artists
- **Album Type**: Filter by album, single, or compilation
- **Explicit Content**: Toggle between explicit, non-explicit, or all content

### Dashboard Tabs

#### 1️⃣ Overview Tab
- Key Performance Indicators (KPIs)
- Popularity distribution histogram
- Duration distribution histogram
- Album type pie chart
- Explicit vs Non-Explicit comparison
- Popularity box plots by content type

#### 2️⃣ Artists Tab
- Top N artists by popularity (adjustable slider)
- Artist statistics table
- Artist deep dive with individual analysis
- Top songs for selected artist

#### 3️⃣ Time Trends Tab
- Monthly popularity trends
- Yearly song release counts
- Average popularity by year
- Heatmap of album types over years

#### 4️⃣ Song Analysis Tab
- Top 20 most popular songs
- Correlation matrix
- Popularity vs Duration scatter plot
- Statistical summary

#### 5️⃣ Data Table Tab
- Searchable raw data table
- Column selection
- Download filtered data as CSV

---

## 🎨 Visual Features

- **Interactive charts** using Plotly (zoom, pan, hover details)
- **Spotify-themed colors** (green: #1DB954)
- **Responsive layout** that works on different screen sizes
- **Real-time filtering** - all charts update based on sidebar selections

---

## 📝 Usage Tips

1. **Start broad**: Use default settings to see overall trends
2. **Filter down**: Select specific years or artists for focused analysis
3. **Compare**: Toggle filters to compare different segments
4. **Export**: Download filtered data from the Data Table tab
5. **Explore**: Click and drag on charts to zoom in on specific areas

---

## 🔧 Customization

You can customize the app by editing `streamlit_app.py`:
- Change color schemes
- Add new visualizations
- Modify KPI calculations
- Add additional filters
- Include more statistical analyses

---

## 💡 Example Use Cases

- **Client Presentations**: Use filters to show specific artist performance
- **Trend Analysis**: Identify seasonal patterns in popularity
- **Content Strategy**: Compare explicit vs non-explicit content performance
- **Artist Research**: Deep dive into specific artists' catalogs
- **Data Exploration**: Search and filter raw data with custom criteria

---

## 📦 Data Requirements

The app expects a CSV file at: `E:\Project\spotify\spotify .csv`

Required columns:
- `song`: Song name
- `artist`: Artist name
- `popularity`: Popularity score (0-100)
- `duration_ms`: Song duration in milliseconds
- `release_date`: Release date
- `date`: Chart date
- `album_type`: Type of album (album/single/compilation)
- `is_explicit`: Boolean for explicit content

---

## 🐛 Troubleshooting

**Dashboard won't start:**
- Ensure all requirements are installed: `pip install -r requirements.txt`
- Check that the CSV file path is correct

**Slow performance:**
- The app uses caching for faster loading
- First load may be slower, subsequent interactions are fast

**Charts not displaying:**
- Verify your browser supports JavaScript
- Try refreshing the page (Ctrl+R or Cmd+R)

---

**Enjoy exploring your Spotify data! 🎵**
