# RECEIPTIFY - Aplikasi Pencatat Pengeluaran Berbasis OCR

## 📌 Deskripsi Proyek
**RECEIPTIFY** adalah aplikasi berbasis Streamlit yang dirancang untuk membantu pengguna dalam mencatat dan menganalisis pengeluaran dengan mudah. Dengan menggunakan teknologi **OCR (Optical Character Recognition)**, aplikasi ini dapat membaca struk belanja, mengonversi data ke dalam format tabel yang rapi, serta menampilkan **visualisasi data pengeluaran** secara otomatis.

## 🚀 Fitur Utama
- 📸 **Scan Struk Otomatis**: Upload struk belanja dalam format gambar dan aplikasi akan mengekstrak informasinya.
- 📊 **Visualisasi Data**: Menampilkan pengeluaran berdasarkan toko, kategori, dan tren harian.
- 📂 **Ekspor ke Excel**: Data hasil scan dapat diunduh dalam format Excel.
- ☁ **Integrasi Google Sheets**: Menyimpan data pengeluaran ke Google Drive.
- 🔍 **Analisis Kepatuhan SLA**: Analisis pengeluaran menggunakan statistik dan AI.

## 🏗️ Arsitektur Sistem
1. **Upload struk belanja** ke aplikasi.
2. **OCR Processing** dengan model AI yang membaca dan mengubah teks dalam struk menjadi tabel.
3. **Data Cleansing & Formatting** menggunakan pandas.
4. **Visualisasi Data** dengan Plotly dan Streamlit.
5. **Simpan Data** ke Google Sheets atau unduh sebagai Excel.

## 📜 Cara Instalasi & Menjalankan Aplikasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/receiptify.git
cd receiptify
```

### 2️⃣ Install Dependencies
Pastikan Python dan pip telah terinstall, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 3️⃣ Jalankan Aplikasi
```bash
streamlit run app.py
```

## 🖥️ Teknologi yang Digunakan
- **Python** (Streamlit, Pandas, OpenAI, Plotly, PIL)
- **OCR API** (Hugging Face + OpenAI GPT-4 Turbo)
- **Cloud Storage** (Google Sheets API)
- **Visualization** (Plotly, Streamlit Charts)

## 📎 Struktur Folder
```
receiptify/
│── app.py          # Main aplikasi Streamlit
│── home.py         # Halaman Home
│── program.py      # Modul analisis dan visualisasi
│── README.md       # Dokumentasi proyek
│── requirements.txt # Dependensi proyek
│── .env            # API Key untuk OpenAI (jika diperlukan)
└── assets/         # Folder untuk gambar atau data tambahan
```

## 📢 Kontribusi
Kami sangat terbuka untuk kontribusi dari komunitas! Silakan fork repository ini dan buat **Pull Request** jika ingin menambahkan fitur atau memperbaiki bug.

## 📄 Lisensi
Proyek ini menggunakan lisensi **MIT License**.

## 📞 Kontak & Portofolio
Jika Anda memiliki pertanyaan atau ingin berdiskusi, silakan hubungi:
- 📧 Email: [email@example.com](mailto:ysmnaraindas.work@gmail.com)
- 💼 LinkedIn: [linkedin.com/in/username](https://linkedin.com/in/yasminenaraindas-setiadi/)

---
⭐ **Jangan lupa untuk memberi star di repository ini jika bermanfaat!** ⭐

