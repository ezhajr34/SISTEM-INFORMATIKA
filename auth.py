import streamlit as st

def show_signup():
    st.title("📝 Sign Up")
    nu = st.text_input("Username")
    np = st.text_input("Password", type="password")
    if st.button("Daftar"):
        if not nu or not np:
            st.warning("Isi semua field!")
        elif nu in st.session_state.users:
            st.warning("Username sudah ada")
        else:
            st.session_state.users[nu] = np
            st.session_state.data[nu]  = []
            st.success("Akun berhasil dibuat")

def show_login():
    st.title("🔐 Login")
    un = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        if un in st.session_state.users and st.session_state.users[un] == pw:
            st.session_state.login = True
            st.session_state.user  = un
            st.success(f"Login berhasil sebagai {un}")
            st.rerun()
        else:
            st.error("Username / Password salah")
