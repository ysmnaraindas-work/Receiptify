import streamlit as st

def run():
    st.markdown("""
    ## Selamat Datang di Aplikasi Pencatat Pengeluaran  
    Aplikasi ini dirancang untuk membantu Anda mengelola pengeluaran dengan lebih mudah. Dengan memindai struk belanja, aplikasi ini akan mencatat dan memberikan **visualisasi pengeluaran** Anda secara otomatis, serta menyimpannya langsung ke **Google Sheets** Anda.

    ---

    #### Kenapa Menggunakan Aplikasi Ini?
    - **Pencatatan Otomatis**: Tidak perlu input manual, cukup scan struk belanja.
    - **Visualisasi Pengeluaran**: Data pengeluaran disajikan dalam bentuk grafik untuk membantu pemahaman yang lebih baik.
    - **Integrasi dengan Google Sheets**: Data pengeluaran akan tersimpan di Google Drive Anda secara otomatis, memudahkan Anda untuk melacak dan merencanakan keuangan.

    ---

    #### Flow Sistem OCR Struk Belanja
    1.  **Upload struk ke dalam platform** → Menggunakan Hugging Face  
    2.  **Model membaca struk** → Menggunakan API LLM untuk membaca isi struk  
    3.  **Menampilkan tabel di frontend** → Backend pakai pandas untuk proses data  
    4.  **Jika sudah benar, tekan tombol "Input"** → Data ditambahkan ke Google Sheet  
    5.  **Jika tabel salah, upload ulang** → Kembali ke tahap awal  
    6.  **Data dibuat visualisasi** → Backend buat visualisasi dari Google Sheet  

    ---
                
    #### Cara Menggunakan:
    1. **Klik tombol "Mulai"** untuk memulai proses pemindaian struk belanja.
    2. **Upload gambar struk belanja Anda** ke platform.
    3. **Model OCR akan membaca struk dan menampilkan ringkasan data belanja** dalam bentuk tabel.
    4. **Visualisasi pengeluaran** akan ditampilkan dalam bentuk grafik berdasarkan data yang ada.
    5. **Simpan data ke Google Sheets** dengan sekali klik.

    ---
    

    """)

    # Gambar ilustrasi
    st.image(
        "Receiptify_Flowchart_Long.png",
        caption="Proses OCR dari gambar ke teks",
        use_container_width=True
    )
