import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Cuaca", page_icon="🌤️", layout="wide")
st.title("🌤️ Dashboard Bedah Kasus 3 - Raffi Kurniawan (241041001)")
st.markdown("Visualisasi Pengamatan Cuaca berdasarkan tipe data Interval, Rasio, dan Nominal.")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('dataset_cuaca_1000.csv')

df = load_data()

# Tampilkan Metrik Rata-rata Keseluruhan
col1, col2, col3 = st.columns(3)
col1.metric("Suhu Rata-rata Keseluruhan", f"{df['Suhu (°C)'].mean():.1f} °C")
col2.metric("Kelembaban Rata-rata", f"{df['Kelembaban (%)'].mean():.0f} %")
col3.metric("Total Pengamatan", f"{len(df)} Data")
st.divider()

# GRAFIK BARIS 1: Fokus pada Numerik
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Distribusi Suhu per Kota (Numerik Interval)")
    st.caption("Box plot membandingkan sebaran suhu antar wilayah.")
    fig_box = px.box(df, x='Kota', y='Suhu (°C)', color='Kota')
    st.plotly_chart(fig_box, use_container_width=True)

with col_b:
    st.subheader("Korelasi Suhu & Kelembaban (Interval vs Rasio)")
    st.caption("Scatter plot untuk melihat hubungan suhu dan kelembaban di berbagai kondisi.")
    fig_scatter = px.scatter(df, x='Suhu (°C)', y='Kelembaban (%)', color='Kondisi', opacity=0.7)
    st.plotly_chart(fig_scatter, use_container_width=True)

# GRAFIK BARIS 2: Fokus pada Kategorik
col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Frekuensi Kondisi Cuaca (Kategorik Nominal)")
    st.caption("Bar chart menghitung jumlah tiap kategori kondisi cuaca.")
    kondisi_count = df['Kondisi'].value_counts().reset_index()
    kondisi_count.columns = ['Kondisi', 'Jumlah']
    fig_bar = px.bar(kondisi_count, x='Kondisi', y='Jumlah', color='Kondisi', text_auto=True)
    st.plotly_chart(fig_bar, use_container_width=True)

with col_d:
    st.subheader("Proporsi Pengamatan per Kota")
    st.caption("Pie chart untuk melihat persentase distribusi data nominal kota.")
    kota_count = df['Kota'].value_counts().reset_index()
    kota_count.columns = ['Kota', 'Jumlah']
    fig_pie = px.pie(kota_count, values='Jumlah', names='Kota', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# Tabel Data
st.subheader("Tabel Dataset Mentah")
st.dataframe(df, use_container_width=True)