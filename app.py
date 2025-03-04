import streamlit as st

# Konfigurasi halaman harus berada paling atas
st.set_page_config(
    layout="wide",
    page_title="OCR Group Team 003",
    # page_icon="https://cdn-icons-png.freepik.com/256/2553/2553642.png?semt=ais_hybrid",
)

# Import modul setelah konfigurasi halaman
import home
import program

# Judul utama
st.markdown("<h1 style='text-align: center;'>RECEIPTIFY</h1>", unsafe_allow_html=True)
    
# Informasi halaman
st.markdown("<h6 style='text-align: center; color: grey;'>FTDS-024-HCK-group-003</h6>", unsafe_allow_html=True)

# Setup Tabs
tab1, tab2 = st.tabs(["Home", "Program"])

# Tab 1: Home
with tab1:
    home.run()

# Tab 2: Exploratory Data Analysis
with tab2:
    program.run()