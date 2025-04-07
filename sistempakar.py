import streamlit as st

st.set_page_config(page_title="Sistem Pakar Tanaman Cabai", layout="wide")

st.title("🌶️ Sistem Pakar Diagnosa Hama dan Penyakit Tanaman Cabai")
st.subheader("Metode: Forward Chaining")
st.write("Silakan pilih gejala yang terlihat pada tanaman cabai Anda:")

# Gejala input dari user
gejala_terpilih = []

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

# Form gejala
with st.form("form_gejala"):
    for kode, nama in gejala_list.items():
        if st.checkbox(nama, key=kode):
            gejala_terpilih.append(kode)
    submitted = st.form_submit_button("Diagnosa")

# Basis Pengetahuan (aturan forward chaining)
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

# Diagnosis
if submitted:
    st.subheader("🩺 Hasil Diagnosa")
    ditemukan = False

    for penyakit, data in penyakit_list.items():
        if all(gejala in gejala_terpilih for gejala in data["gejala"]):
            st.success(f"🌱 Penyakit: {penyakit}")
            st.write("**Solusi:**", data["solusi"])
            ditemukan = True

    if not ditemukan:
        st.warning("❗ Tidak ditemukan penyakit yang cocok dengan gejala yang Anda pilih.")
        st.info("Silakan periksa kembali gejala atau konsultasikan ke ahli pertanian.")

# Footer
st.markdown("---")
st.caption("Dibuat oleh: Sistem Pakar Cabai | Metode Forward Chaining | Streamlit")
