import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Air Quality Dashboard", page_icon="🌤️", layout="wide")
sns.set_theme(style="whitegrid")

@st.cache_data
def load_and_clean_data():
    df = pd.read_csv("PRSA_Data_Wanshouxigong_20130301-20170228.csv")

    cols_to_fill = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'wd', 'WSPM']
    df[cols_to_fill] = df[cols_to_fill].ffill().bfill()
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df_2015 = df[df['year'] == 2015].copy()
    bins = [0, 35, 75, 115, 150, 250, np.inf]
    labels = ['Sangat Baik', 'Baik', 'Tercemar Ringan', 'Tercemar Sedang', 'Tercemar Berat', 'Sangat Berbahaya']
    df_2015['AQI_Category'] = pd.cut(df_2015['PM2.5'], bins=bins, labels=labels, include_lowest=True)

    return df_2015

df_2015 = load_and_clean_data()

# SIDEBAR
st.sidebar.title("☁️ Air Quality Dashboard")
st.sidebar.markdown("**Stasiun Wanshouxigong**")
st.sidebar.markdown("Proyek Analisis Data ini berfokus pada kualitas udara sepanjang tahun **2015**.")
st.sidebar.markdown("---")
st.sidebar.markdown("**Dibuat oleh:** Prianto Sanema Wau")

# HALAMAN UTAMA (HEADER)
st.title("☁️ Dashboard Analisis Kualitas Udara (Tahun 2015)")
st.markdown("Visualisasi metrik polutan dan pengaruh cuaca di stasiun Wanshouxigong.")

# Menampilkan metrik sederhana
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rata-rata PM2.5 Tahunan", f"{df_2015['PM2.5'].mean():.2f} µg/m³")
with col2:
    st.metric("Curah Hujan Maksimal", f"{df_2015['RAIN'].max():.1f} mm")
with col3:
    st.metric("Rata-rata NO2 Tahunan", f"{df_2015['NO2'].mean():.2f} µg/m³")

st.markdown("---")

# ROW 1: TREN WAKTU (BULANAN & HARIAN)
st.subheader("Tren Waktu Polusi: Musiman vs Harian")
fig1_col, fig2_col = st.columns(2)

with fig1_col:
    # Pertanyaan 1: PM2.5 Bulanan
    monthly_pm25 = df_2015.groupby('month')['PM2.5'].mean().reset_index()
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='month', y='PM2.5', data=monthly_pm25, marker='o', color='crimson', linewidth=2.5, ax=ax1)
    ax1.set_title("Tren Rata-rata PM2.5 Bulanan", fontweight='bold')
    ax1.set_xlabel("Bulan")
    ax1.set_ylabel("Rata-rata PM2.5 (µg/m³)")
    ax1.set_xticks(range(1, 13))
    st.pyplot(fig1)

with fig2_col:
    # Pertanyaan 4: NO2 Jam-jaman
    hourly_no2 = df_2015.groupby('hour')['NO2'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='hour', y='NO2', data=hourly_no2, marker='s', color='purple', linewidth=2.5, ax=ax2)
    ax2.axvspan(18, 22, color='red', alpha=0.1, label='Jam Kritis')
    ax2.set_title("Siklus Harian Rata-rata Konsentrasi NO2", fontweight='bold')
    ax2.set_xlabel("Jam (00:00 - 23:00)")
    ax2.set_ylabel("Rata-rata NO2 (µg/m³)")
    ax2.set_xticks(range(0, 24, 3))
    ax2.legend()
    st.pyplot(fig2)

st.markdown("---")

# ROW 2: KORELASI CUACA (HUJAN & ANGIN)
st.subheader("Pengaruh Cuaca Terhadap Kualitas Udara")
fig3_col, fig4_col = st.columns(2)

with fig3_col:
    # Pertanyaan 2: Curah Hujan vs PM10
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x='RAIN', y='PM10', data=df_2015, alpha=0.4, color='teal', ax=ax3)
    sns.regplot(x='RAIN', y='PM10', data=df_2015, scatter=False, color='red', ax=ax3)
    ax3.set_title("Curah Hujan vs Konsentrasi PM10", fontweight='bold')
    ax3.set_xlabel("Curah Hujan (mm)")
    ax3.set_ylabel("PM10 (µg/m³)")
    st.pyplot(fig3)

with fig4_col:
    # Pertanyaan 3: Kecepatan Angin vs PM2.5
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x='WSPM', y='PM2.5', data=df_2015, alpha=0.4, color='darkorange', ax=ax4)
    sns.regplot(x='WSPM', y='PM2.5', data=df_2015, scatter=False, color='red', ax=ax4)
    ax4.set_title("Kecepatan Angin vs Konsentrasi PM2.5", fontweight='bold')
    ax4.set_xlabel("Kecepatan Angin (m/s)")
    ax4.set_ylabel("PM2.5 (µg/m³)")
    st.pyplot(fig4)

st.markdown("---")

# ROW 3: ANALISIS LANJUTAN (CLUSTERING)
st.subheader("Distribusi Kategori Kualitas Udara (PM2.5)")
aqi_distribution = df_2015['AQI_Category'].value_counts().reset_index()
aqi_distribution.columns = ['Kategori Kualitas Udara', 'Jumlah Jam']

fig5, ax5 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x='Jumlah Jam',
    y='Kategori Kualitas Udara',
    data=aqi_distribution,
    palette='magma',
    hue='Kategori Kualitas Udara',
    legend=False,
    ax=ax5
)
ax5.set_title("Distribusi Jumlah Jam Berdasarkan Kategori AQI", fontweight='bold')
ax5.set_xlabel("Jumlah Jam")
ax5.set_ylabel("Kategori AQI")
st.pyplot(fig5)
