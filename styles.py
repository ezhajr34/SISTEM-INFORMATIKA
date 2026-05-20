import streamlit as st

def load_styles():
    st.markdown("""
<style>
/* Hapus SEMUA padding/margin/gap bawaan Streamlit di dalam tabel */
div[data-testid="stHorizontalBlock"] {
    gap: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    align-items: stretch !important;
}
div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
    padding: 0 !important;
    margin: 0 !important;
    overflow: visible !important;
}
/* Hapus padding dalam elemen markdown di dalam kolom tabel */
div[data-testid="stColumn"] > div[data-testid="stVerticalBlock"] {
    gap: 0 !important;
    padding: 0 !important;
}
div[data-testid="stColumn"] > div > div[data-testid="stMarkdownContainer"] {
    margin: 0 !important;
    padding: 0 !important;
    line-height: 0 !important;
}
/* Sembunyikan label kosong tombol */
div[data-testid="stColumn"] > div > div > div[data-testid="stVerticalBlock"] {
    gap: 0 !important;
    padding: 0 !important;
}

/* Khusus untuk baris tabel: paksa tinggi seragam */
.row-tabel div[data-testid="stHorizontalBlock"] {
    min-height: 48px !important;
    max-height: 48px !important;
}

/* Tombol Edit & Hapus */
.row-tabel button {
    height: 48px !important;
    min-height: 48px !important;
    max-height: 48px !important;
    border-radius: 0 !important;
    margin: 0 !important;
    padding: 0 6px !important;
    font-size: 0.82em !important;
    font-weight: 700 !important;
    width: 100% !important;
    border: none !important;
    border-left: 1px solid #dee2e6 !important;
}
.row-tabel button[kind="primary"] {
    background-color: #DC3545 !important;
    color: white !important;
}
.row-tabel button[kind="secondary"] {
    background-color: #FFC107 !important;
    color: #333 !important;
}

/* Sel tabel */
.sel {
    background: white;
    border-bottom: 1px solid #dee2e6;
    border-right: 1px solid #dee2e6;
    padding: 0 12px;
    font-size: 0.91em;
    color: #333;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin: 0;
    line-height: 1;
}
.sel-left  { border-left: 1px solid #dee2e6; }
.sel-head  { background: #f1f3f5 !important; font-weight: 700; color: #222; border-bottom: 2px solid #ced4da !important; }
.sel-top-left  { border-top: 1px solid #dee2e6; border-radius: 10px 0 0 0; }
.sel-top-right { border-top: 1px solid #dee2e6; border-radius: 0 10px 0 0; }
.sel-top       { border-top: 1px solid #dee2e6; }
.sel-bot-left  { border-radius: 0 0 0 10px; }
.sel-bot-right { border-radius: 0 0 10px 0; }

.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.80em;
    font-weight: 700;
    color: white;
    background: #198754;
}

/* Shadow seluruh tabel */
.tbl-shadow {
    box-shadow: 0 2px 12px rgba(0,0,0,0.10);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)
