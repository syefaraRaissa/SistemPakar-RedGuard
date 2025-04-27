import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Sistem Pakar Cabai", layout="wide")

# Navigasi halaman
halaman = st.sidebar.selectbox("📌 Menu", ["Diagnosa Penyakit", "Informasi Penyakit & Tips", "Profil Kelompok"])

# CSS untuk mempercantik tampilan dan card layout
st.markdown("""
    <style>
    image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        height: auto;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .card:hover {
        background-color: #e2f2e2;
    }
    .card h3 {
        color: #007a33;
    }
    .card p {
        font-size: 14px;
        color: #555;
    }
   .card img {
        border-radius: 10px;
        width: 50%;  # Membuat gambar mengisi lebar card
        height: auto;  # Menjaga proporsi gambar
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Data gejala dan penyakit
gejala_list = {
    "G1": "Apakah daun tanaman cabai terlihat keriting?",
    "G2": "Apakah daun tanaman cabai menguning?",
    "G3": "Apakah pertumbuhan tanaman cabai lambat?",
    "G4": "Apakah daun tanaman cabai terlihat berlubang?",
    "G5": "Apakah terdapat ulat pada tanaman cabai?",
    "G6": "Apakah daun pada tanaman cabai sering gugur?",
    "G7": "Apakah buah dari tanaman cabai sering busuk?",
    "G8": "Apakah batang tanaman cabai layu?",
    "G9": "Apakah terdapat bintik pada daun?",
    "G10": "Apakah daun tanaman cabai mengering?",
    "G11": "Apakah akar tanaman cabai membusuk?"
}

penyakit_list = {
    "Serangan Kutu Daun (Aphids)": {
        "gejala": ["G1", "G2", "G3"],
        "solusi": "Semprot tanaman dengan insektisida berbahan aktif imidakloprid.",
        "informasi": "Serangan Kutu Daun (Aphids) adalah salah satu masalah serius yang menyerang berbagai jenis tanaman, terutama tanaman hortikultura. Kutu daun merupakan serangga kecil yang hidup berkelompok di bagian bawah daun, batang muda, atau tunas tanaman. Serangannya ditandai dengan gejala seperti daun menggulung, menguning, pertumbuhan tanaman terhambat, hingga munculnya embun madu yang lengket di permukaan tanaman, yang kemudian bisa mengundang pertumbuhan jamur hitam (sooty mold). Aphids merusak tanaman dengan cara menghisap cairan sel tanaman sehingga mengurangi vitalitas tanaman. Selain itu, kutu daun juga dapat menjadi vektor penyebaran berbagai penyakit virus tanaman. Untuk mengendalikan serangan kutu daun, disarankan melakukan penyemprotan insektisida berbahan aktif imidakloprid secara teratur, serta menjaga kebersihan lingkungan sekitar tanaman agar tidak menjadi tempat berkembang biaknya hama ini.",
        "gambar": "kutu-daun.jpg"
    },
    "Serangan Ulat Grayak (Spodoptera litura)": {
        "gejala": ["G4", "G5"],
        "solusi": "Gunakan insektisida nabati atau Bacillus thuringiensis.",
        "informasi": "Serangan Ulat Grayak (Spodoptera litura) adalah salah satu serangan hama yang paling merusak pada berbagai jenis tanaman budidaya, terutama sayuran dan tanaman hortikultura. Ulat grayak menyerang dengan cara memakan daun, batang muda, dan kadang-kadang buah tanaman, sehingga menyebabkan daun berlubang, rusak, bahkan rontok. Serangan ini biasanya dimulai dengan gejala seperti daun berlubang tidak beraturan dan kerusakan berat pada pucuk tanaman. Ulat grayak aktif terutama di malam hari, sementara pada siang hari mereka bersembunyi di tanah atau di bawah daun. Jika tidak dikendalikan, populasi ulat bisa meningkat dengan cepat dan menyebabkan kerugian besar.",
        "gambar": "Ulat_Grayak.jpg"
    },
    "Busuk Batang (Phytophthora capsici)": {
        "gejala": ["G6", "G7", "G8"],
        "solusi": "Gunakan fungisida sistemik dan hindari genangan air.",
        "informasi": "Busuk Batang (Phytophthora capsici) adalah penyakit tanaman yang disebabkan oleh jamur patogen dan sering menyerang tanaman seperti cabai, terung, tomat, dan beberapa tanaman hortikultura lainnya. Penyakit ini ditandai dengan munculnya bercak cokelat kehitaman pada batang dekat permukaan tanah, yang lama-kelamaan membusuk dan melemahkan struktur tanaman. Daun tanaman yang terserang biasanya akan layu mendadak, meskipun tanah masih tampak basah, dan jika infeksi parah, tanaman bisa mati seluruhnya. Phytophthora capsici berkembang cepat di kondisi lembab dan basah, sehingga sering muncul setelah hujan deras atau sistem pengairan yang buruk. Untuk mengendalikan penyakit ini, penting melakukan sanitasi lahan, menggunakan varietas tahan penyakit, memperbaiki sistem drainase, serta melakukan aplikasi fungisida berbahan aktif sesuai anjuran untuk mencegah penyebaran lebih lanjut.",
        "gambar": "busuk_batang.jpg"
    },
    "Penyakit Bercak Daun (Cercospora)": {
        "gejala": ["G9", "G2", "G10"],
        "solusi": "Semprotkan fungisida mankozeb atau klorotalonil.",
        "informasi": "Penyakit Bercak Daun (Cercospora) adalah salah satu penyakit tanaman yang disebabkan oleh jamur dari genus Cercospora, dan menyerang berbagai jenis tanaman, termasuk sayuran dan tanaman hortikultura. Gejala serangan ini ditandai dengan munculnya bercak-bercak kecil berwarna cokelat hingga abu-abu pada permukaan daun, yang lama-kelamaan membesar dan dapat menyebabkan daun menguning, kering, dan rontok. Penyakit ini biasanya berkembang cepat di lingkungan yang lembab dan hangat. Jika tidak segera dikendalikan, infeksi bercak daun dapat menghambat fotosintesis, memperlambat pertumbuhan tanaman, dan menurunkan hasil panen secara signifikan. Pengendalian penyakit ini dapat dilakukan dengan menjaga sirkulasi udara di sekitar tanaman, menghindari penyiraman dari atas yang memperlama kelembaban daun, serta menggunakan fungisida berbahan aktif sesuai anjuran untuk menghentikan penyebarannya.",
        "gambar": "bercak_daun.jpg"
    },
    "Busuk Akar (Fusarium)": {
        "gejala": ["G2", "G11"],
        "solusi": "Gunakan fungisida sistemik dan rotasi tanaman.",
        "informasi": "Busuk Akar (Fusarium) adalah penyakit tanaman yang disebabkan oleh jamur Fusarium spp., yang menyerang sistem perakaran dan menyebabkan kerusakan serius pada banyak jenis tanaman, termasuk sayuran, tanaman buah, dan tanaman hias. Penyakit ini ditandai dengan gejala akar yang membusuk, berubah warna menjadi cokelat hingga kehitaman, serta tanaman yang tampak layu meskipun kondisi tanah cukup lembab. Infeksi Fusarium juga dapat menyebabkan pertumbuhan tanaman terhambat, daun menguning, dan akhirnya kematian tanaman. Penyakit ini berkembang pesat di tanah yang lembab, kurang drainase, serta pada kondisi lingkungan yang panas. Untuk mengendalikan Busuk Akar Fusarium, perlu dilakukan sanitasi lahan, penggunaan benih sehat, rotasi tanaman, serta aplikasi fungisida sistemik sesuai anjuran. Menjaga kebersihan area tanam dan memperbaiki sistem drainase juga sangat penting untuk mencegah penyebaran penyakit ini.",
        "gambar": "busuk_akar.jpg"
    }
}

# =================== HALAMAN DIAGNOSA ===================
if halaman == "Diagnosa Penyakit":
    st.markdown("<h1 style='color:Red;'>🌶️ Diagnosa Penyakit Tanaman Cabai</h1>", unsafe_allow_html=True)
    st.markdown("#### Metode: <span style='color:green;'>Forward Chaining</span>", unsafe_allow_html=True)
    st.image("cabai.jpg", caption="Tanaman Cabai Sehat", use_container_width=True)

    st.markdown("### ✅ Jawab pertanyaan berikut:")

    gejala_terpilih = []
    with st.form("form_diagnosa"):
        for kode, pertanyaan in gejala_list.items():
            jawaban = st.radio(pertanyaan, ("Tidak", "Ya"), key="radio_" + kode)
            if jawaban == "Ya":
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

            # Kemungkinan penyakit lain
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
        st.markdown(f'<div class="card"><h3>{nama}</h3><p>{data["informasi"]}</p><p><strong>💡 Solusi:</strong> {data["solusi"]}</p>', unsafe_allow_html=True)
        try:
            st.image(data["gambar"], use_container_width=True)
        except:
            st.warning("Gambar tidak tersedia.")
        st.markdown("</div>", unsafe_allow_html=True)

# =================== HALAMAN PROFIL KELOMPOK ===================
elif halaman == "Profil Kelompok":
    st.markdown("## 👨‍👩‍👧‍👦 Profil Kelompok")
    st.write("""
    **Kelompok Redguard adalah kelompok mahasiswa yang berfokus pada pengembangan teknologi dan solusi berbasis AI untuk mendukung keberlanjutan dan peningkatan kualitas hidup masyarakat. Kami berkomitmen untuk menciptakan inovasi yang dapat memperbaiki berbagai sektor kehidupan, mulai dari pertanian hingga kesehatan, dengan pendekatan yang ramah lingkungan dan berorientasi pada masa depan. Kami percaya bahwa teknologi adalah kunci untuk menghadapi tantangan global yang semakin kompleks.

    **Anggota:**
    - Syefara Raissa Ramadhan   221506012
    - Dita Ayu Cahaya Apria     2215061014
    - Muhammad Haikal Batubara	2255061010

    
    """)
     st.markdown("🌶️KELOMPOK REDGUARD🌶️,📍 Lokasi: Universitas Lampung, Fakultas Teknik - Teknik Informatika")

