import pandas as pd
import numpy as np
import random

# Set seed agar data konsisten
np.random.seed(42)
random.seed(42)

# Mengembangkan kota dan kondisi berdasarkan 2 sampel awal (Jakarta & Bandung)
kotas = ['Jakarta', 'Bandung', 'Surabaya', 'Yogyakarta', 'Medan']
kondisis = ['Cerah', 'Berawan', 'Hujan', 'Gerimis']

data = []

# Generate 1000 baris data
for _ in range(1000):
    kota = random.choice(kotas)
    
    # Logika suhu dan kelembaban agar serealistis mungkin berdasarkan kota
    # Jakarta/Surabaya/Medan cenderung panas. Bandung/Jogja lebih sejuk.
    if kota in ['Jakarta', 'Surabaya', 'Medan']:
        base_suhu = random.uniform(28.0, 35.0)
    else: 
        base_suhu = random.uniform(22.0, 28.0)
        
    kondisi = random.choice(kondisis)
    
    # Kelembaban naik jika hujan, Suhu naik jika cerah
    if kondisi == 'Hujan':
        suhu = base_suhu - random.uniform(1.0, 3.0)
        kelembaban = random.uniform(80, 95)
    elif kondisi == 'Cerah':
        suhu = base_suhu + random.uniform(0.0, 2.0)
        kelembaban = random.uniform(60, 75)
    else:
        suhu = base_suhu
        kelembaban = random.uniform(70, 85)
        
    data.append([kota, round(suhu, 1), int(kelembaban), kondisi])

# Membuat DataFrame
df = pd.DataFrame(data, columns=['Kota', 'Suhu (°C)', 'Kelembaban (%)', 'Kondisi'])

# Proses Analisis Detail Menggunakan Python
print("=== ANALISIS CUACA 1000 DATA ===")
print("1. Rata-rata Suhu & Kelembaban per Kota:")
print(df.groupby('Kota')[['Suhu (°C)', 'Kelembaban (%)']].mean().round(1))

print("\n2. Frekuensi Kondisi Cuaca Keseluruhan:")
print(df['Kondisi'].value_counts())

print("\n3. Cuaca Ekstrem Tercatat:")
print(f"Suhu Tertinggi: {df['Suhu (°C)'].max()}°C")
print(f"Suhu Terendah: {df['Suhu (°C)'].min()}°C")

# Simpan ke CSV
df.to_csv('dataset_cuaca_1000.csv', index=False)
print("\n[SUCCESS] File dataset_cuaca_1000.csv berhasil dibuat!")