import streamlit as st

def _rekomendasikan(logika, desain, minat):
    # Rule-Based IF–THEN: Sistem Rekomendasi Pemilihan Jurusan
    if logika >= 80 and desain >= 80:
        return "Teknik Informatika",   "Logika dan desain keduanya tinggi"
    elif logika >= 80 and minat == "Coding":
        return "Rekayasa Perangkat Lunak", "Logika tinggi dan minat coding"
    elif logika >= 80 and minat == "Keamanan":
        return "Cyber Security",       "Logika tinggi dan minat keamanan sistem"
    elif logika >= 80 and minat == "Data":
        return "Data Science",         "Logika tinggi dan minat analisis data"
    elif desain >= 80 and minat == "Desain":
        return "Desain Komunikasi Visual", "Kemampuan desain tinggi dan minat desain"
    elif desain >= 80:
        return "UI/UX Design",         "Kemampuan desain tinggi"
    elif minat == "Game":
        return "Game Development",     "Minat di pengembangan game"
    elif minat == "Data":
        return "Sistem Informasi",     "Minat di bidang pengelolaan data"
    elif minat == "Coding":
        return "Ilmu Komputer",        "Minat di bidang pemrograman"
    else:
        return "Konsultasi Lebih Lanjut", "Belum cukup data untuk rekomendasi pasti"

def show_input_data():
    st.title("🎓 Input Data Siswa")
    st.caption("Isi data berikut untuk mendapatkan rekomendasi jurusan yang sesuai.")

    nama   = st.text_input("Nama Siswa")
    logika = st.slider("Nilai Logika / Matematika", 0, 100, 50)
    desain = st.slider("Nilai Seni / Desain",       0, 100, 50)
    minat  = st.selectbox("Minat Utama", ["Coding", "Desain", "Data", "Keamanan", "Game"])

    if st.button("Proses & Simpan", type="primary"):
        if not nama:
            st.warning("Nama harus diisi!")
        else:
            rekomendasi, alasan = _rekomendasikan(logika, desain, minat)
            st.success(f"✅ Rekomendasi Jurusan: **{rekomendasi}**")
            st.info(f"💡 Alasan: {alasan}")
            st.session_state.data[st.session_state.user].append({
                "Nama":         nama,
                "Logika":       logika,
                "Desain":       desain,
                "Minat":        minat,
                "Rekomendasi":  rekomendasi,
            })
