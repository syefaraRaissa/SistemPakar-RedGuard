import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Sistem Pakar Cabai", layout="wide")

# Navigasi halaman
halaman = st.sidebar.selectbox("📌 Menu", ["Diagnosa Penyakit", "Informasi Penyakit & Tips"])

# Basis gejala & penyakit
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
        "solusi": "Semprot tanaman dengan insektisida berbahan aktif imidakloprid dan jaga kebersihan tanaman.",
        "informasi": "Serangan kutu daun (Aphids) adalah gangguan pada tanaman yang disebabkan oleh serangga kecil berukuran 0,5–2 mm dengan tubuh lunak dan warna bervariasi seperti hijau, kuning, cokelat, atau hitam. Kutu daun hidup berkelompok di bagian bawah daun muda, pucuk tanaman, atau batang muda, dan menyerang dengan cara menghisap cairan tanaman menggunakan mulutnya yang panjang. Serangan ini menyebabkan daun menjadi keriput, menguning, menggulung, serta pertumbuhan tanaman terhambat bahkan dapat menyebabkan kematian. Selain kerusakan langsung, kutu daun juga mengeluarkan cairan manis yang memicu tumbuhnya jamur jelaga yang menghambat fotosintesis. Lebih parah lagi, kutu daun dapat menjadi vektor penyebaran berbagai virus tanaman seperti Virus Kentang Y (PVY) dan Virus Mosaik Kacang Umum (BCMV), yang dapat menurunkan hasil dan kualitas panen secara signifikan. Oleh karena itu, pengendalian kutu daun sangat penting untuk menjaga kesehatan tanaman dan mencegah kerugian agronomis.",
        "gambar": "kutu-daun.jpg"
    },
    "Serangan Ulat Grayak (Spodoptera litura)": {
        "gejala": ["G4", "G5"],
        "solusi": "Gunakan insektisida nabati atau Bacillus thuringiensis, dan lakukan sanitasi lahan.",
        "informasi": "Serangan ulat grayak (Spodoptera litura) merupakan gangguan hama yang serius pada berbagai tanaman budidaya seperti kedelai, kubis, dan umbi-umbian. Larva ulat grayak ini aktif memakan daun secara berkelompok, meninggalkan lubang-lubang besar dan hanya menyisakan tulang daun, sehingga menghambat fotosintesis dan pertumbuhan tanaman. Serangan pada tanaman muda dapat menyebabkan tanaman menjadi kerdil dan buah berukuran kecil atau terlambat berkembang. Siklus hidup ulat grayak dari telur hingga ngengat berlangsung sekitar 25-30 hari, dengan larva yang memiliki ciri khas berupa bintik hitam berbentuk bulan sabit pada setiap ruas abdomen. Hama ini dapat menyerang sepanjang tahun tanpa dipengaruhi musim secara signifikan, dan serangannya dapat menyebabkan kerugian besar hingga kehilangan hasil panen. Pengendalian ulat grayak dapat dilakukan dengan metode ramah lingkungan seperti penggunaan virus, cendawan entomopatogen, parasitoid, predator, dan pestisida nabati untuk menjaga keseimbangan ekosistem dan mengurangi residu kimia.",
        "gambar": "Ulat_Grayak.jpg"
    },
    "Busuk Batang (Phytophthora capsici)": {
        "gejala": ["G6", "G7", "G8"],
        "solusi": "Gunakan fungisida sistemik dan hindari genangan air di sekitar tanaman.",
        "informasi": "Penyakit busuk batang yang disebabkan oleh Phytophthora capsici adalah penyakit serius pada tanaman seperti lada dan cabai yang menyerang akar, batang, dan buah. Infeksi ini menyebabkan pembusukan pada pangkal batang dan akar sehingga mengganggu transportasi air dan nutrisi dari tanah ke seluruh tanaman, mengakibatkan daun menguning, layu, dan akhirnya tanaman dapat mati mendadak dalam waktu singkat. Gejala khas meliputi kulit batang yang terkelupas, jaringan pembuluh yang berubah coklat, serta keluarnya lendir berwarna hitam atau biru muda pada kondisi lembap. Penyakit ini sering diperparah oleh kondisi lahan yang tergenang air dan drainase buruk. Phytophthora capsici juga dapat bertahan lama di tanah melalui spora yang tahan lingkungan ekstrem, sehingga sulit diberantas. Pengendalian penyakit ini dapat dilakukan dengan pengelolaan lahan yang baik dan penggunaan agen hayati seperti Trichoderma sp. dan Bacillus spp. yang efektif menekan perkembangan patogen",
        "gambar": "busuk_batang.jpg"
    },
    "Penyakit Bercak Daun (Cercospora)": {
        "gejala": ["G9", "G2", "G10"],
        "solusi": "Semprotkan fungisida berbahan aktif mankozeb atau klorotalonil secara berkala.",
        "informasi": "Penyakit bercak daun (Cercospora) adalah penyakit tanaman yang disebabkan oleh jamur dari genus Cercospora, yang menyerang berbagai tanaman seperti padi, kacang-kacangan, dan cabai. Gejalanya berupa bercak-bercak kecil hingga sempit memanjang berwarna coklat kemerahan atau coklat pucat dengan tepian coklat kemerahan pada daun, yang dapat meluas dan menyebabkan daun menguning, kering, serta rontok. Pada padi, bercak ini sering muncul sejajar dengan tulang daun dan dapat mengganggu proses fotosintesis sehingga menurunkan hasil panen. Jamur penyebab penyakit ini menyebar melalui konidium yang terbawa angin dan bertahan di sisa tanaman atau benih, dengan perkembangan penyakit yang dipengaruhi oleh kondisi lingkungan seperti kelembapan tinggi dan kekurangan unsur hara nitrogen dan kalium. Pengendalian penyakit bercak daun Cercospora umumnya dilakukan dengan penyemprotan fungisida dan pengelolaan nutrisi tanaman secara tepat untuk mengurangi kerugian hasil panen.",
        "gambar": "bercak_daun.jpg"
    },
    "Busuk Akar (Fusarium)": {
        "gejala": ["G2", "G11"],
        "solusi": "Gunakan fungisida sistemik dan rotasi tanaman untuk memutus siklus patogen.",
        "informasi": "JPenyakit busuk akar yang disebabkan oleh jamur Fusarium merupakan penyakit serius yang menyerang sistem perakaran tanaman dengan gejala awal berupa akar yang berwarna coklat gelap, lembek, dan berair. Infeksi jamur ini menyebabkan terganggunya aliran air dan nutrisi dari akar ke bagian tanaman lainnya, sehingga daun bawah menguning, layu, dan akhirnya tanaman menjadi kerdil serta dapat mati. Pada batang, sering muncul lesi coklat tua atau hitam yang dapat mengelilingi batang dan menyebabkan kanker lunak. Jamur Fusarium dapat bertahan lama di tanah melalui spora yang tahan terhadap kondisi lingkungan ekstrem, sehingga penyakit ini sulit dikendalikan dan dapat menyebar melalui benih, tanah, air, dan alat pertanian. Kondisi tanah yang lembap dan drainase buruk mempercepat perkembangan penyakit ini. Pengendalian busuk akar Fusarium dapat dilakukan dengan pendekatan terpadu, termasuk penggunaan agen hayati seperti Trichoderma spp. dan bakteri antagonis, perbaikan drainase tanah, serta penggunaan fungisida yang tepat untuk membatasi penyebaran penyakit.",
        "gambar": "busuk_akar.jpg"
    }
}

# HALAMAN DIAGNOSA
if halaman == "Diagnosa Penyakit":
    st.markdown("<h1 style='color:Tomato;'>🌶️ Diagnosa Penyakit Tanaman Cabai</h1>", unsafe_allow_html=True)
    st.markdown("#### Metode: <span style='color:green;'>Forward Chaining</span>", unsafe_allow_html=True)
    st.image("cabai.jpg", caption="Tanaman Cabai Sehat", use_container_width=True)

    st.markdown("### ✅ Pilih gejala yang terlihat:")
    gejala_terpilih = []

    with st.form("form_gejala"):
        for kode, nama in gejala_list.items():
            if st.checkbox(nama, key=kode):
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
                st.success(f"🌱 Penyakit: **{penyakit}**")
                st.markdown(f"**🧪 Solusi:** {data['solusi']}")
                st.markdown(f"**📊 Akurasi Diagnosa:** {akurasi}%")
                ditemukan = True

        if not ditemukan:
            st.warning("⚠️ Tidak ditemukan penyakit yang cocok dengan gejala yang Anda pilih.")
            st.info("💡 Coba cek kembali gejala atau konsultasikan ke ahli pertanian.")

# HALAMAN INFORMASI
elif halaman == "Informasi Penyakit & Tips":
    st.markdown("<h1 style='color:green;'>📚 Informasi Penyakit & Tips Merawat Cabai</h1>", unsafe_allow_html=True)

    for nama, data in penyakit_list.items():
        st.markdown(f"### 🔎 {nama}")
        st.write(data["informasi"])
        st.markdown(f"**💡 Solusi:** {data['solusi']}")

        try:
            image = Image.open(data["gambar"])
            st.image(image, caption=f"📸 Gambar {nama}", use_container_width=True)
        except FileNotFoundError:
            st.warning(f"Gambar untuk {nama} tidak ditemukan: {data['gambar']}")

        st.markdown("---")

    st.markdown("### 🌱 Tips & Trik Merawat Tanaman Cabai:")
    st.markdown("""
    - 🌞 Pastikan tanaman mendapat cukup sinar matahari minimal 6 jam/hari.
    - 💧 Siram tanaman secara teratur, hindari kelebihan air.
    - 🌾 Gunakan pupuk organik untuk meningkatkan kesuburan tanah.
    - 🔄 Lakukan rotasi tanaman untuk menghindari serangan patogen tanah.
    - ✂️ Pangkas daun tua & rusak untuk mencegah penyebaran penyakit.
    - 🧼 Jaga kebersihan lingkungan sekitar tanaman dari gulma & sisa tanaman yang sakit.
    """)

# Footer
st.markdown("---")
st.caption("👨‍🌾 Dibuat oleh Sistem Pakar Cabai | Forward Chaining | Streamlit App")
