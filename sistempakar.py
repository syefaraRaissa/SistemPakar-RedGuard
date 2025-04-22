import streamlit as st
import json
import os

st.set_page_config(page_title="Sistem Pakar Tanaman Cabai", layout="wide")

st.image("cabai.jpg", use_column_width=True)

st.title("🌶️ Sistem Pakar Diagnosa Hama dan Penyakit Tanaman Cabai")
st.subheader("Metode: Forward Chaining")
st.write("Silakan pilih gejala yang terlihat pada tanaman cabai Anda:")

# File untuk menyimpan gejala tambahan
GEJALA_FILE = "gejala_tambahan.json"

# Fungsi untuk membaca gejala tambahan
def load_gejala_tambahan():
    if os.path.exists(GEJALA_FILE):
        with open(GEJALA_FILE, "r") as f:
            return json.load(f)
    return {}

# Fungsi untuk menyimpan gejala tambahan
def simpan_gejala_tambahan(nama_gejala):
    gejala_data = load_gejala_tambahan()
    kode_baru = f"G{len(gejala_data)+12}"  # dimulai dari G12
    gejala_data[kode_baru] = nama_gejala
    with open(GEJALA_FILE, "w") as f:
        json.dump(gejala_data, f)
    return kode_baru

# Gejala bawaan
gejala_list = {
    "G1": "Daun keriting",
    "G2": "Daun menguning",
    "G3": "Pertumbuhan lambat",
    "G4": "Daun berlubang",
    "G5": "Terdapat ulat pada tanaman",
    "G6": "Daun gugur",
    "G7": "Buah busuk",
    "G8": "Batang layu",
    "G9": "Terdapat bintik pada daun",
    "G10": "Daun mengering",
    "G11": "Akar membusuk",
}

# Gabungkan dengan gejala tambahan
gejala_list.update(load_gejala_tambahan())

# Form gejala
gejala_terpilih = []
with st.form("form_gejala"):
    for kode, nama in gejala_list.items():
        if st.checkbox(nama, key=kode):
            gejala_terpilih.append(kode)
    submitted = st.form_submit_button("Diagnosa")

# Diagnosa berbasis forward chaining
penyakit_list = {
    "Serangan Kutu Daun (Aphids)": {
        "gejala": ["G1", "G2", "G3"],
        "solusi": "Semprot tanaman dengan insektisida berbahan aktif imidakloprid dan jaga kebersihan tanaman."
    },
    "Serangan Ulat Grayak (Spodoptera litura)": {
        "gejala": ["G4", "G5"],
        "solusi": "Gunakan insektisida nabati atau Bacillus thuringiensis, dan lakukan sanitasi lahan."
    },
    "Busuk Batang (Phytophthora capsici)": {
        "gejala": ["G6", "G7", "G8"],
        "solusi": "Gunakan fungisida sistemik dan hindari genangan air di sekitar tanaman."
    },
    "Penyakit Bercak Daun (Cercospora)": {
        "gejala": ["G9", "G2", "G10"],
        "solusi": "Semprotkan fungisida berbahan aktif mankozeb atau klorotalonil secara berkala."
    },
    "Busuk Akar (Fusarium)": {
        "gejala": ["G2", "G11"],
        "solusi": "Gunakan fungisida sistemik dan rotasi tanaman untuk memutus siklus patogen."
    }
}

# Hasil diagnosa
if submitted:
    st.subheader("🩺 Hasil Diagnosa")
    ditemukan = False
    for penyakit, data in penyakit_list.items():
        if all(gejala in gejala_terpilih for gejala in data["gejala"]):
            st.success(f"🌱 Penyakit: {penyakit}")
            st.write("**Solusi:**", data["solusi"])
            ditemukan = True
    if not ditemukan:
        st.warning("❗ Tidak ditemukan penyakit yang cocok.")
        st.info("Silakan periksa kembali gejala atau tambahkan gejala baru.")

# Form gejala tambahan
st.markdown("### ➕ Tambah Gejala Baru")
with st.form("form_tambah_gejala"):
    new_gejala = st.text_input("Masukkan nama gejala baru:")
    tambah = st.form_submit_button("Tambah Gejala")
    if tambah and new_gejala.strip() != "":
        kode_baru = simpan_gejala_tambahan(new_gejala.strip())
        st.success(f"Gejala '{new_gejala}' telah ditambahkan dengan kode {kode_baru}. Silakan centang pada daftar di atas.")
        st.experimental_rerun()

# Footer
st.markdown("---")
st.caption("Dibuat oleh: Sistem Pakar Cabai | Metode Forward Chaining | Streamlit")
