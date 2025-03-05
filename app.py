import streamlit as st
import os

# ========================= 🔥 KONFIGURASI HALAMAN UTAMA ========================= #
st.set_page_config(page_title="Kuesioner Analitik", layout="wide")

# HEADER INTERAKTIF
st.markdown("<h1 style='text-align: center; color: #FF5733;'>📊 Aplikasi Analisis Kuesioner</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #33FFBD;'>Silakan navigasi ke halaman lain dari sidebar atau tombol di bawah.</h3>", unsafe_allow_html=True)

st.markdown("---")

# ========================= 🔥 NAVIGASI VIA SIDEBAR ========================= #
st.sidebar.title("🔍 Navigasi Aplikasi")

if st.sidebar.button("🏠 Home"):
    st.experimental_rerun()

if st.sidebar.button("📝 Isi Form"):
    os.system("streamlit run pages/form.py")

if st.sidebar.button("📊 Dashboard"):
    os.system("streamlit run pages/dashboard.py")

st.sidebar.markdown("---")
st.sidebar.success("📍 Pilih halaman di sidebar untuk mulai eksplorasi!")

# ========================= 🔥 NAVIGASI KE HALAMAN LAIN (DENGAN TOMBOL) ========================= #
st.subheader("🔍 Ayo Mulai Analisis!")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Isi Form Kuesioner"):
        os.system("streamlit run pages/form.py")

with col2:
    if st.button("📊 Lihat Dashboard Analitik"):
        os.system("streamlit run pages/dashboard.py")

st.markdown("---")

# ========================= 🔥 FOOTER ========================= #
st.markdown("<h5 style='text-align: center; color: #888;'>🚀 Created by Lammy Tutur Miaw</h5>", unsafe_allow_html=True)
