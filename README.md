# ☁️ Air Quality Dashboard - Wanshouxigong Station

Proyek ini adalah sebuah *dashboard* interaktif berbasis web yang dibangun menggunakan **Streamlit**. *Dashboard* ini bertujuan untuk melakukan analisis dan visualisasi data kualitas udara di stasiun Wanshouxigong sepanjang tahun **2015**. 

## ✨ Fitur Utama

Aplikasi ini menyediakan berbagai fitur interaktif untuk mengeksplorasi data:
*   **Filter Rentang Waktu:** Pengguna dapat menyesuaikan rentang tanggal yang ingin dianalisis melalui *sidebar*.
*   **Filter Kategori AQI (PM2.5):** Pengguna dapat memfilter data berdasarkan kategori kualitas udara (Sangat Baik hingga Sangat Berbahaya).
*   **Metrik Utama:** Menampilkan ringkasan metrik secara instan (Rata-rata PM2.5, Curah Hujan Maksimal, dan Rata-rata NO2).
*   **Visualisasi Tren Waktu:** 
    *   Grafik garis untuk tren rata-rata PM2.5 bulanan.
    *   Grafik garis untuk siklus harian rata-rata konsentrasi NO2 (dilengkapi sorotan pada jam-jam kritis).
*   **Analisis Korelasi Cuaca:** 
    *   Curah hujan vs Konsentrasi PM10.
    *   Kecepatan angin vs Konsentrasi PM2.5.
*   **Distribusi Kategori AQI:** Grafik batang yang menunjukkan distribusi jumlah jam untuk masing-masing kategori kualitas udara.

## 🛠️ Teknologi yang Digunakan

Proyek ini menggunakan bahasa pemrograman **Python** dengan beberapa *library* utama:
*   [Streamlit](https://streamlit.io/): Untuk membangun antarmuka web interaktif.
*   [Pandas](https://pandas.pydata.org/): Untuk manipulasi dan analisis data.
*   [NumPy](https://numpy.org/): Untuk komputasi numerik.
*   [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/): Untuk pembuatan visualisasi grafik.

## 🚀 Cara Menjalankan Proyek di Komputer Lokal

Jika kamu ingin menjalankan *dashboard* ini di komputermu sendiri, ikuti langkah-langkah berikut:

**1. Clone Repository**
```bash
git clone [https://github.com/username-kamu/nama-repository-kamu.git](https://github.com/username-kamu/nama-repository-kamu.git)
cd nama-repository-kamu

**2. Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # Untuk Linux/Mac
env\Scripts\activate     # Untuk Windows

**3. Install Library**
```bash
pip install pandas numpy matplotlib seaborn streamlit

**4. Siapkan Dataset**
Pastikan file dataset ⁠PRSA_Data_Wanshouxigong_20130301-20170228.csv⁠ berada di dalam direktori yang sama dengan file aplikasi Python (misalnya ⁠app.py⁠).

**5. Jalankan Streamlit**
streamlit run app.py

