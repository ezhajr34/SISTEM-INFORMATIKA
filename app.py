import streamlit as st
from styles import load_styles
from modules.auth import show_login, show_signup
from modules.input_data import show_input_data
from modules.lihat_data import show_lihat_data

st.set_page_config(page_title="Sistem Rekomendasi Informatika", layout="wide")
load_styles()

# ── DATABASE ──
if "users"      not in st.session_state: st.session_state.users = {"fahriel": "fahriel589", "eja": "eja617"}
if "data"       not in st.session_state: st.session_state.data  = {"fahriel": [], "eja": []}
if "login"      not in st.session_state: st.session_state.login = False
if "edit_index" not in st.session_state: st.session_state.edit_index = None

# ── SIDEBAR ──
if not st.session_state.login:
    menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])
else:
    st.sidebar.success(f"Login sebagai: {st.session_state.user}")
    menu    = None
    halaman = st.sidebar.selectbox("Menu Utama", ["Input Data", "Lihat Data"])
    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.session_state.edit_index = None
        st.rerun()

# ── ROUTING ──
if not st.session_state.login:
    if menu == "Sign Up":
        show_signup()
    else:
        show_login()
else:
    if halaman == "Input Data":
        show_input_data()
    elif halaman == "Lihat Data":
        show_lihat_data()
