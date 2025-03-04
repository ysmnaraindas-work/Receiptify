import pandas as pd
import streamlit as st
import plotly.express as px
from openai import OpenAI
from PIL import Image
import os
from dotenv import load_dotenv
import io
import base64

# Load environment variables
load_dotenv()

# Inisialisasi OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Prompt untuk OCR processing
PROMPT = """
    Kamu adalah AI yang mengubah teks hasil OCR dari struk belanja menjadi csv yang rapi.
    Instruksi:
    1. Baca semua data Tanggal,Nama Toko,Nama Barang,Jumlah,Harga,Total Harga dalam foto struk belanja.
    2. Tulis tanggal dalam tabel dengan berformat %Y/%m/%d, pastikan kamu membaca data tanggal dan jam dari struk dengan benar.
    3. Tentukan kategori yang berisi Makanan, Minuman, Rumah Tangga, Lainnya.
    4. Format angka adalah integer, perbaiki jika ada kesalahan format angka.
    5. Jika ada barang cancel, tambahkan di bawah tabel dengan menggunakan kata cancel sebelum nama barang.
    6. Jika ada diskon atau voucher, tambahkan di bawah tabel dengan isi tanggal dan toko yang sama.
    7. Contoh format yang benar:
    Tanggal,Nama Toko,Nama Barang,Jumlah,Harga,Total Harga,Kategori
    2025/12/31,Indomaret,ABC ORANGE 525ML,1,13500,13500,Minuman
    2025/12/31,Indomaret,I/F BISC.WNDRLND 300,1,20900,20900,Makanan
    2025/12/31,Indomaret,Lexus Sandw Cokl 190,2,26800,53600,Makanan
    2025/12/31,Indomaret,Cancel Lexus Sandw Cokl 190,2,-26800,-53600,Makanan
    2025/12/31,Indomaret,Voucher Unilever Indonesia PT.,1,-10000,10000,Lainnya
    
    Jangan tambahkan teks lain di luar tabel
"""

# Function untuk menyimpan data ke Excel
def save_to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Receipt Data")
    output.seek(0)
    return output

# Inisialisasi session state jika belum ada
if "df" not in st.session_state or st.session_state.df is None:
    st.session_state.df = pd.DataFrame(columns=["Tanggal", "Nama Toko", "Nama Barang", "Jumlah", "Harga", "Total Harga", "Kategori"])
if "scanned_df" not in st.session_state:
    st.session_state.scanned_df = None
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

def run():
    col1, col2 = st.columns(2)
    
    with col1:
        file = st.file_uploader("Upload Struk Belanja", type=["jpg", "png"])
        
        if file is not None:
            st.session_state.uploaded_file = file
            st.image(file, caption="Preview Struk", use_container_width=True)
        
        st.write("❗ **Pastikan foto struk belanja lurus, cahaya cukup, dan tulisan jelas.**")
        
        if st.button("Scan"):
            if st.session_state.uploaded_file is not None:
                with st.spinner("Scanning image..."):
                    image_bytes = st.session_state.uploaded_file.getvalue()
                    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
                    
                    response = client.chat.completions.create(
                        model="gpt-4-turbo",
                        messages=[
                            {"role": "system", "content": PROMPT},
                            {"role": "user", "content": [
                                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                            ]}
                        ],
                        max_tokens=2000
                    )
                    result_text = response.choices[0].message.content.strip()
                    
                    if result_text:
                        data = [row.split(',') for row in result_text.split('\n')]
                        columns = data[0]
                        scanned_df = pd.DataFrame(data[1:], columns=columns)
                        
                        # Pastikan kolom angka dalam format integer
                        scanned_df["Jumlah"] = scanned_df["Jumlah"].astype(int)
                        scanned_df["Harga"] = scanned_df["Harga"].astype(int)
                        scanned_df["Total Harga"] = scanned_df["Total Harga"].astype(int)
                        
                        st.session_state.scanned_df = scanned_df
                        st.success("Scan berhasil!")
            else:
                st.error("Silakan upload file struk terlebih dahulu!")
    
    with col2:
        st.subheader("Hasil Scan & Simpan")
        if st.session_state.scanned_df is not None:
            st.dataframe(st.session_state.scanned_df, use_container_width=True)
            st.write("""❗ 
                    **Jika tabel hasil scan belum sesuai, silahkan lakukan scan ulang.**
                    Jika tidak berhasil, silahkan coba upload foto baru yang lebih jelas.
                    Jika tanggal tidak sesuai dengan struk belanja, bantu kami dengan **menghapus tulisan di sekitar area tanggal** dalam struk sebelum diupload kembali.
                    """)
            if st.button("Commit"):
                if st.session_state.df.empty:
                    st.session_state.df = st.session_state.scanned_df.copy()
                else:
                    st.session_state.df = pd.concat([st.session_state.df, st.session_state.scanned_df], ignore_index=True)
                st.session_state.scanned_df = None  # Hapus hasil scan setelah disimpan
                st.success("Data berhasil disimpan!")
    
    if not st.session_state.df.empty:
        st.subheader("Visualisasi Data")
        
        col_v1, col_v2, col_v3 = st.columns(3)
        
        with col_v1:
            fig1 = px.bar(st.session_state.df, x="Nama Toko", y="Total Harga", title="Total Pengeluaran per Toko")
            st.plotly_chart(fig1, use_container_width=True)
        
        with col_v2:
            fig2 = px.pie(st.session_state.df, names="Kategori", values="Total Harga", title="Distribusi Pengeluaran per Kategori")
            st.plotly_chart(fig2, use_container_width=True)
        
        with col_v3:
            st.session_state.df["Tanggal"] = pd.to_datetime(st.session_state.df["Tanggal"])
            df_trend = st.session_state.df.groupby("Tanggal")["Total Harga"].sum().reset_index()
            fig3 = px.line(df_trend, x="Tanggal", y="Total Harga", title="Tren Pengeluaran Harian")
            st.plotly_chart(fig3, use_container_width=True)
        
        st.dataframe(st.session_state.df, use_container_width=True)
        
        excel_data = save_to_excel(st.session_state.df)
        st.download_button(
            label="Download as Excel",
            data=excel_data,
            file_name="receipt_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    run()
