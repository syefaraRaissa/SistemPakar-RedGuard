import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Sistem Pakar Cabai", layout="wide")

# Navigasi halaman
halaman = st.sidebar.selectbox("📌 Menu", ["Diagnosa Penyakit", "Informasi Penyakit & Tips", "Profil Kelompok"])

# Data gejala dan penyakit
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

penyakit_list = {
    "Serangan Kutu Daun (Aphids)": {
        "gejala": ["G1", "G2", "G3"],
        "solusi": "Semprot tanaman dengan insektisida berbahan aktif imidakloprid.",
        "informasi": "Serangan kutu daun (Aphids)...",
        "gambar": "kutu-daun.jpg"
    },
    "Serangan Ulat Grayak (Spodoptera litura)": {
        "gejala": ["G4", "G5"],
        "solusi": "Gunakan insektisida nabati atau Bacillus thuringiensis.",
        "informasi": "Serangan ulat grayak (Spodoptera litura)...",
        "gambar": "Ulat_Grayak.jpg"
    },
    "Busuk Batang (Phytophthora capsici)": {
        "gejala": ["G6", "G7", "G8"],
        "solusi": "Gunakan fungisida sistemik dan hindari genangan air.",
        "informasi": "Busuk batang (Phytophthora capsici)...",
        "gambar": "busuk_batang.jpg"
    },
    "Penyakit Bercak Daun (Cercospora)": {
        "gejala": ["G9", "G2", "G10"],
        "solusi": "Semprotkan fungisida mankozeb atau klorotalonil.",
        "informasi": "Penyakit bercak daun (Cercospora)...",
        "gambar": "bercak_daun.jpg"
    },
    "Busuk Akar (Fusarium)": {
        "gejala": ["G2", "G11"],
        "solusi": "Gunakan fungisida sistemik dan rotasi tanaman.",
        "informasi": "Busuk akar (Fusarium)...",
        "gambar": "busuk_akar.jpg"
    }
}

# =================== HALAMAN DIAGNOSA ===================
if halaman == "Diagnosa Penyakit":
    st.markdown("<h1 style='color:Tomato;'>🌶️ Diagnosa Penyakit Tanaman Cabai</h1>", unsafe_allow_html=True)
    st.markdown("#### Metode: <span style='color:green;'>Forward Chaining</span>", unsafe_allow_html=True)
    st.image("cabai.jpg", caption="Tanaman Cabai Sehat", use_container_width=True)

    st.markdown("### ✅ Pilih gejala yang terlihat:")
    gejala_terpilih = []

    with st.form("form_gejala"):
        for kode, nama in gejala_list.items():
            if st.checkbox(nama, key="cb_" + kode):
                gejala_terpilih.append(kode)
        submitted = st.form_submit_button("🔍 Diagnosa Sekarang")

    if submitted:
        st.markdown("## 🩺 Hasil Diagnosa")
        ditemukan = False
        for penyakit, data in penyakit_list.items():
            gejala_penyakit = data["gejala"]
            cocok = [g for g in gejala_penyakit if g in gejala_terpilih]

            if set(gejala_penyakit).issubset(set(gejala_terpilih)):
                akurasi = round((len(cocok) / len(gejala_penyakit)) * 100, 2)
                st.success(f"🌱 Penyakit: *{penyakit}*")
                st.markdown(f"*🧪 Solusi:* {data['solusi']}")
                st.markdown(f"*📊 Akurasi Diagnosa:* {akurasi}%")
                ditemukan = True

        if not ditemukan:
            st.warning("⚠️ Tidak ditemukan penyakit yang cocok dengan gejala yang Anda pilih.")
            st.info("💡 Coba cek kembali gejala atau konsultasikan ke ahli pertanian.")
            
    st.markdown("## 🌶️ Diagnosa Penyakit Tanaman Cabai")
    st.write("Jawab 'Ya' atau 'Tidak' untuk gejala berikut:")

    gejala_terpilih = []
    with st.form("form_diagnosa"):
        for kode, deskripsi in gejala_list.items():
            if st.radio(deskripsi, ("Tidak", "Ya"), key="radio_" + kode) == "Ya":
                gejala_terpilih.append(kode)
        submit = st.form_submit_button("🔍 Diagnosa Sekarang")

    if submit:
        st.subheader("🩺 Hasil Diagnosa:")
        hasil = []
        for penyakit, data in penyakit_list.items():
            cocok = [g for g in data["gejala"] if g in gejala_terpilih]
            persentase = len(cocok) / len(data["gejala"])
            if persentase == 1.0:
                hasil.append((penyakit, persentase))

        if hasil:
            nama_penyakit, akurasi = hasil[0]
            st.success(f"✅ Penyakit terdeteksi: **{nama_penyakit}**")
            st.markdown(f"**💡 Solusi:** {penyakit_list[nama_penyakit]['solusi']}")
            st.markdown(f"**📊 Akurasi Diagnosa:** {akurasi*100:.2f}%")
            try:
                st.image(penyakit_list[nama_penyakit]["gambar"], use_container_width=True)
            except:
                st.warning("Gambar tidak ditemukan.")

            # Penyakit lainnya (kemungkinan)
            st.markdown("### 🔍 Kemungkinan Penyakit Lain:")
            for penyakit, data in penyakit_list.items():
                cocok = [g for g in data["gejala"] if g in gejala_terpilih]
                prob = len(cocok) / len(data["gejala"])
                if 0 < prob < 1.0:
                    st.info(f"📌 {penyakit} → Probabilitas: {prob*100:.2f}%")

        else:
            st.warning("❌ Tidak ditemukan penyakit yang sesuai.")
            st.info("💡 Silakan periksa kembali gejala atau konsultasikan ke ahli.")

# =================== HALAMAN INFORMASI ===================
elif halaman == "Informasi Penyakit & Tips":
    st.markdown("## 📚 Informasi Penyakit & Tips Merawat Tanaman Cabai")
    for nama, data in penyakit_list.items():
        st.markdown(f"### 🔎 {nama}")
        st.write(data["informasi"])
        st.markdown(f"**💡 Solusi:** {data['solusi']}")
        try:
            st.image(data["gambar"], use_container_width=True)
        except:
            st.warning("Gambar tidak tersedia.")
        st.markdown("---")

# =================== HALAMAN PROFIL KELOMPOK ===================
elif halaman == "Profil Kelompok":
    st.markdown("## 👨‍👩‍👧‍👦 Profil Kelompok")
    st.write("""
    **Kelompok Tani Cabai Sejahtera** adalah kelompok mahasiswa yang berfokus pada pengembangan sistem pakar berbasis AI 
    untuk membantu petani mengenali dan mengatasi penyakit tanaman cabai. Kami percaya bahwa teknologi dapat membantu 
    meningkatkan produktivitas pertanian.

    **Anggota:**
    - Raissa Ramadhan (UI/UX & Front-End)
    - Dani Pratama (Back-End & Machine Learning)
    - Intan Permata (Database & Dokumentasi)
    - Budi Santoso (Manajemen & Integrasi)
    """)

    st.markdown("📍 Lokasi: Universitas Lampung, Fakultas Teknik - Teknik Informatika")

