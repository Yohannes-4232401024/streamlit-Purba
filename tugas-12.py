import streamlit as st
import pandas as pd

st.write(
    """
    # Assignment 12
    Hello Word, it is my Project Streamlit [Yohannes Paruntungan Purba & 4232401024]!
    """
)

# Title
st.title("Dashboard Visualisasi Data Mahasiswa")

st.caption("Tugas Pertemuan 12 | Streamlit Web App")

st.divider()

# =========================
# HEADER & SUBHEADER
# =========================
st.header("Data Akademik Mahasiswa")
st.subheader("Rekap Nilai Semester")

# =========================
# TEXT (PARAGRAF)
# =========================
st.markdown(
    """
    Aplikasi web ini dibuat menggunakan **Streamlit** sebagai media pembelajaran
    untuk menampilkan data akademik mahasiswa dalam bentuk **tabel** dan **grafik**.
    
    Data yang digunakan merupakan **data simulasi**, sehingga tidak merepresentasikan
    data mahasiswa yang sebenarnya.
    """
)

st.caption("Catatan: Data hanya digunakan untuk keperluan akademik")

st.divider()

# =========================
# CODE (POTONGAN KODE)
# =========================
st.subheader("Contoh Potongan Kode")

st.code(
    """
import pandas as pd

data = {
    "Nama": ["Andi", "Budi", "Citra"],
    "Nilai": [85, 90, 88]
}

df = pd.DataFrame(data)
    """,
    language="python"
)

st.divider()

# =========================
# DATA
# =========================
data = {
    "Nama": ["Andi", "Budi", "Citra", "Dina", "Eka"],
    "Nilai": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

# =========================
# LAYOUT: TABEL & CHART
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tabel Nilai Mahasiswa")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("Grafik Nilai Mahasiswa")
    st.bar_chart(df.set_index("Nama"))

# =========================
# FOOTER
# =========================
st.divider()
st.caption("Dibuat menggunakan Streamlit | Teknik Elektro")
