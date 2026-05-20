import streamlit as st

RATIO  = [0.35, 1.8, 0.8, 0.8, 1.0, 2.0, 1.5]
LABELS = ["#", "Nama", "Logika", "Desain", "Minat", "Rekomendasi", "Aksi"]
MINATS = ["Coding", "Desain", "Data", "Keamanan", "Game"]

BADGE_COLOR = {
    "Teknik Informatika":          "#6610f2",
    "Rekayasa Perangkat Lunak":    "#0d6efd",
    "Cyber Security":              "#dc3545",
    "Data Science":                "#0dcaf0",
    "Desain Komunikasi Visual":    "#fd7e14",
    "UI/UX Design":                "#d63384",
    "Game Development":            "#198754",
    "Sistem Informasi":            "#20c997",
    "Ilmu Komputer":               "#0d6efd",
    "Konsultasi Lebih Lanjut":     "#6c757d",
}

def _rekomendasikan(logika, desain, minat):
    if logika >= 80 and desain >= 80:
        return "Teknik Informatika"
    elif logika >= 80 and minat == "Coding":
        return "Rekayasa Perangkat Lunak"
    elif logika >= 80 and minat == "Keamanan":
        return "Cyber Security"
    elif logika >= 80 and minat == "Data":
        return "Data Science"
    elif desain >= 80 and minat == "Desain":
        return "Desain Komunikasi Visual"
    elif desain >= 80:
        return "UI/UX Design"
    elif minat == "Game":
        return "Game Development"
    elif minat == "Data":
        return "Sistem Informasi"
    elif minat == "Coding":
        return "Ilmu Komputer"
    else:
        return "Konsultasi Lebih Lanjut"

def _render_header():
    hcols = st.columns(RATIO)
    for j, (col, lbl) in enumerate(zip(hcols, LABELS)):
        left_cls = "sel-left" if j == 0 else ""
        top_cls  = ("sel-top-left"  if j == 0 else
                    "sel-top-right" if j == len(LABELS) - 1 else "sel-top")
        col.markdown(
            f'<div class="sel sel-head {left_cls} {top_cls}">{lbl}</div>',
            unsafe_allow_html=True)

def _render_row(i, row, n, user):
    is_last = (i == n - 1)
    bot_l   = "sel-bot-left"  if is_last else ""
    rek     = row.get("Rekomendasi", "")
    color   = BADGE_COLOR.get(rek, "#6c757d")

    st.markdown('<div class="row-tabel">', unsafe_allow_html=True)
    rcols = st.columns(RATIO)

    rcols[0].markdown(f'<div class="sel sel-left {bot_l}">{i+1}</div>',  unsafe_allow_html=True)
    rcols[1].markdown(f'<div class="sel">{row["Nama"]}</div>',           unsafe_allow_html=True)
    rcols[2].markdown(f'<div class="sel">{row["Logika"]}</div>',         unsafe_allow_html=True)
    rcols[3].markdown(f'<div class="sel">{row["Desain"]}</div>',         unsafe_allow_html=True)
    rcols[4].markdown(f'<div class="sel">{row["Minat"]}</div>',          unsafe_allow_html=True)
    rcols[5].markdown(
        f'<div class="sel"><span class="badge" style="background:{color};font-size:0.75em;white-space:nowrap">{rek}</span></div>',
        unsafe_allow_html=True)

    with rcols[6]:
        ca, cb = st.columns(2)
        with ca:
            if st.button("✏️ Edit", key=f"e{i}", use_container_width=True):
                st.session_state.edit_index = i
                st.rerun()
        with cb:
            if st.button("🗑️ Hapus", key=f"h{i}", use_container_width=True, type="primary"):
                st.session_state.data[user].pop(i)
                if st.session_state.edit_index == i:
                    st.session_state.edit_index = None
                st.success("Data berhasil dihapus")
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def _render_edit_form(user, data_user):
    idx = st.session_state.edit_index
    if idx >= len(data_user):
        return
    dt = data_user[idx]
    st.divider()
    st.subheader(f"✏️ Edit Data: {dt['Nama']}")
    ne = st.text_input("Nama",         value=dt["Nama"],  key="ne")
    le = st.slider("Nilai Logika",     0, 100, value=dt["Logika"], key="le")
    de = st.slider("Nilai Desain",     0, 100, value=dt["Desain"], key="de")
    me = st.selectbox("Minat", MINATS, index=MINATS.index(dt["Minat"]), key="me")
    cs, cc, _ = st.columns([1, 1, 4])
    if cs.button("💾 Simpan", type="primary", use_container_width=True):
        st.session_state.data[user][idx] = {
            "Nama": ne, "Logika": le, "Desain": de,
            "Minat": me, "Rekomendasi": _rekomendasikan(le, de, me)}
        st.session_state.edit_index = None
        st.success("Data berhasil diupdate")
        st.rerun()
    if cc.button("❌ Batal", use_container_width=True):
        st.session_state.edit_index = None
        st.rerun()

def show_lihat_data():
    st.title("📁 Data Rekomendasi Jurusan")
    user      = st.session_state.user
    data_user = st.session_state.data[user]

    if not data_user:
        st.warning("Belum ada data siswa.")
        return

    # Ringkasan
    from collections import Counter
    terbanyak = Counter(d["Rekomendasi"] for d in data_user).most_common(1)[0][0]
    c1, c2 = st.columns(2)
    c1.metric("Total Siswa",        len(data_user))
    c2.metric("Rekomendasi Terbanyak", terbanyak)
    st.divider()

    st.markdown('<div class="tbl-shadow">', unsafe_allow_html=True)
    _render_header()
    for i, row in enumerate(data_user):
        _render_row(i, row, len(data_user), user)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.edit_index is not None:
        _render_edit_form(user, data_user)
