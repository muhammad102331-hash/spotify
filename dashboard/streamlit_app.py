import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Spotify EDA Dashboard",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1DB954;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv(r"E:\Project\spotify\data\spotify .csv")
    df['date'] = pd.to_datetime(df['date'])
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df = df.dropna(subset=['release_date'])
    df['year'] = df['release_date'].dt.year
    df['month'] = df['release_date'].dt.month
    df['month_name'] = df['release_date'].dt.strftime('%B')
    return df

# Load data
df = load_data()

# Header
st.markdown('<p class="main-header">🎵 Spotify Data Analysis Dashboard</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Year filter
years = sorted(df['year'].dropna().unique())
selected_years = st.sidebar.multiselect(
    "Select Years",
    options=years,
    default=years
)

# Artist filter
artists = sorted(df['artist'].unique())
selected_artists = st.sidebar.multiselect(
    "Select Artists",
    options=artists,
    default=[]
)

# Album type filter
album_types = df['album_type'].unique()
selected_album_types = st.sidebar.multiselect(
    "Select Album Types",
    options=album_types,
    default=album_types
)

# Explicit filter
explicit_filter = st.sidebar.radio(
    "Explicit Content",
    options=["All", "Explicit Only", "Non-Explicit Only"]
)

# Apply filters
filtered_df = df.copy()
if selected_years:
    filtered_df = filtered_df[filtered_df['year'].isin(selected_years)]
if selected_artists:
    filtered_df = filtered_df[filtered_df['artist'].isin(selected_artists)]
if selected_album_types:
    filtered_df = filtered_df[filtered_df['album_type'].isin(selected_album_types)]
if explicit_filter == "Explicit Only":
    filtered_df = filtered_df[filtered_df['is_explicit'] == True]
elif explicit_filter == "Non-Explicit Only":
    filtered_df = filtered_df[filtered_df['is_explicit'] == False]

# KPI Section
st.header("📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_songs = filtered_df['song'].nunique()
    st.metric("Total Songs", f"{total_songs:,}")

with col2:
    distinct_artists = filtered_df['artist'].nunique()
    st.metric("Distinct Artists", f"{distinct_artists:,}")

with col3:
    avg_popularity = filtered_df['popularity'].mean()
    st.metric("Avg Popularity", f"{avg_popularity:.2f}")

with col4:
    avg_duration = filtered_df['duration_ms'].mean() / 1000 / 60
    st.metric("Avg Duration (min)", f"{avg_duration:.2f}")

st.markdown("---")

# Tabs for different sections
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Overview", 
    "🎤 Artists", 
    "📅 Time Trends", 
    "🎵 Song Analysis",
    "📋 Data Table"
])

# TAB 1: Overview
with tab1:
    st.header("Data Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Popularity Distribution")
        fig = px.histogram(
            filtered_df, 
            x='popularity', 
            nbins=30,
            title='Song Popularity Distribution',
            labels={'popularity': 'Popularity Score'},
            color_discrete_sequence=['#1DB954']
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Album Type Distribution")
        album_counts = filtered_df['album_type'].value_counts()
        fig = px.pie(
            values=album_counts.values,
            names=album_counts.index,
            title='Album Type Distribution',
            color_discrete_sequence=px.colors.sequential.Greens_r
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Duration Distribution")
        fig = px.histogram(
            filtered_df, 
            x=filtered_df['duration_ms']/1000/60, 
            nbins=30,
            title='Song Duration Distribution',
            labels={'x': 'Duration (minutes)'},
            color_discrete_sequence=['#1DB954']
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Explicit vs Non-Explicit")
        explicit_counts = filtered_df['is_explicit'].value_counts()
        fig = px.bar(
            x=['Non-Explicit', 'Explicit'],
            y=[explicit_counts.get(False, 0), explicit_counts.get(True, 0)],
            title='Explicit vs Non-Explicit Songs',
            labels={'x': 'Content Type', 'y': 'Count'},
            color_discrete_sequence=['#1DB954', '#FF6B6B']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Popularity comparison
    st.subheader("Popularity by Content Type")
    fig = px.box(
        filtered_df,
        x='is_explicit',
        y='popularity',
        title='Popularity Comparison: Explicit vs Non-Explicit',
        labels={'is_explicit': 'Is Explicit', 'popularity': 'Popularity Score'},
        color='is_explicit',
        color_discrete_map={True: '#FF6B6B', False: '#1DB954'}
    )
    st.plotly_chart(fig, use_container_width=True)

# TAB 2: Artists
with tab2:
    st.header("Artist Analysis")
    
    # Top artists
    col1, col2 = st.columns([2, 1])
    
    with col1:
        n_artists = st.slider("Number of top artists to display", 5, 20, 10)
        top_artists = filtered_df.groupby('artist')['popularity'].mean().nlargest(n_artists).sort_values()
        
        fig = px.bar(
            x=top_artists.values,
            y=top_artists.index,
            orientation='h',
            title=f'Top {n_artists} Artists by Average Popularity',
            labels={'x': 'Average Popularity', 'y': 'Artist'},
            color=top_artists.values,
            color_continuous_scale='Greens'
        )
        fig.update_layout(showlegend=False, height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Top Artists Stats")
        top_artists_df = filtered_df.groupby('artist').agg({
            'song': 'count',
            'popularity': 'mean'
        }).round(2).sort_values('popularity', ascending=False).head(10)
        top_artists_df.columns = ['Song Count', 'Avg Popularity']
        st.dataframe(top_artists_df, use_container_width=True)
    
    # Artist deep dive
    st.subheader("Artist Deep Dive")
    selected_artist = st.selectbox("Select an artist for detailed analysis", options=sorted(filtered_df['artist'].unique()))
    
    if selected_artist:
        artist_data = filtered_df[filtered_df['artist'] == selected_artist]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Songs", len(artist_data))
        with col2:
            st.metric("Average Popularity", f"{artist_data['popularity'].mean():.2f}")
        with col3:
            st.metric("Most Popular Song", artist_data.nlargest(1, 'popularity')['song'].values[0])
        
        # Top songs for selected artist
        st.subheader(f"Top 10 Songs by {selected_artist}")
        top_songs = artist_data.nlargest(10, 'popularity')[['song', 'popularity', 'release_date', 'album_type']]
        st.dataframe(top_songs, use_container_width=True)

# TAB 3: Time Trends
with tab3:
    st.header("Time-Based Analysis")
    
    # Monthly trends
    st.subheader("Average Popularity by Month")
    monthly_data = filtered_df.groupby('month_name')['popularity'].mean().reindex([
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    
    fig = px.line(
        x=monthly_data.index,
        y=monthly_data.values,
        title='Average Popularity Across Months',
        labels={'x': 'Month', 'y': 'Average Popularity'},
        markers=True
    )
    fig.update_traces(line_color='#1DB954', marker=dict(size=10))
    st.plotly_chart(fig, use_container_width=True)
    
    # Yearly trends
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Songs Released by Year")
        yearly_songs = filtered_df.groupby('year')['song'].count()
        fig = px.bar(
            x=yearly_songs.index,
            y=yearly_songs.values,
            title='Number of Songs by Year',
            labels={'x': 'Year', 'y': 'Number of Songs'},
            color_discrete_sequence=['#1DB954']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Average Popularity by Year")
        yearly_popularity = filtered_df.groupby('year')['popularity'].mean()
        fig = px.line(
            x=yearly_popularity.index,
            y=yearly_popularity.values,
            title='Average Popularity Trend',
            labels={'x': 'Year', 'y': 'Average Popularity'},
            markers=True
        )
        fig.update_traces(line_color='#1DB954', marker=dict(size=8))
        st.plotly_chart(fig, use_container_width=True)
    
    # Heatmap: Album type by year
    st.subheader("Album Type Distribution Over Years")
    heatmap_data = filtered_df.groupby(['year', 'album_type']).size().reset_index(name='count')
    heatmap_pivot = heatmap_data.pivot(index='album_type', columns='year', values='count').fillna(0)
    
    fig = px.imshow(
        heatmap_pivot,
        title='Album Type Distribution by Year',
        labels=dict(x="Year", y="Album Type", color="Count"),
        color_continuous_scale='Greens',
        aspect='auto'
    )
    st.plotly_chart(fig, use_container_width=True)

# TAB 4: Song Analysis
with tab4:
    st.header("Song-Level Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top 20 Most Popular Songs")
        top_songs = filtered_df.nlargest(20, 'popularity')[['song', 'artist', 'popularity', 'release_date']]
        top_songs['release_date'] = top_songs['release_date'].dt.strftime('%Y-%m-%d')
        st.dataframe(top_songs.reset_index(drop=True), use_container_width=True, height=600)
    
    with col2:
        st.subheader("Correlation Analysis")
        numeric_cols = ['popularity', 'duration_ms']
        corr_data = filtered_df[numeric_cols].corr()
        
        fig = px.imshow(
            corr_data,
            text_auto='.2f',
            title='Correlation Matrix',
            color_continuous_scale='RdYlGn',
            aspect='auto'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Popularity vs Duration")
        fig = px.scatter(
            filtered_df,
            x=filtered_df['duration_ms']/1000/60,
            y='popularity',
            title='Popularity vs Song Duration',
            labels={'x': 'Duration (minutes)', 'y': 'Popularity'},
            color='popularity',
            color_continuous_scale='Greens',
            opacity=0.6
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Statistical summary
    st.subheader("Statistical Summary")
    st.dataframe(filtered_df[['popularity', 'duration_ms']].describe(), use_container_width=True)

# TAB 5: Data Table
with tab5:
    st.header("Raw Data")
    st.subheader(f"Showing {len(filtered_df)} rows")
    
    # Search functionality
    search_term = st.text_input("🔍 Search songs or artists", "")
    if search_term:
        display_df = filtered_df[
            filtered_df['song'].str.contains(search_term, case=False, na=False) |
            filtered_df['artist'].str.contains(search_term, case=False, na=False)
        ]
    else:
        display_df = filtered_df
    
    # Select columns to display
    all_columns = display_df.columns.tolist()
    selected_columns = st.multiselect(
        "Select columns to display",
        options=all_columns,
        default=['song', 'artist', 'popularity', 'album_type', 'release_date', 'duration_ms']
    )
    
    if selected_columns:
        st.dataframe(display_df[selected_columns], use_container_width=True, height=600)
    
    # Download data
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=display_df.to_csv(index=False).encode('utf-8'),
        file_name='spotify_filtered_data.csv',
        mime='text/csv',
    )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>🎵 Spotify EDA Dashboard | Data Analysis Tool | Built with Streamlit</p>
    </div>
    """, unsafe_allow_html=True)
