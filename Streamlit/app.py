import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = "🏆" 
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("Streamlit/foto.jpeg")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilih Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Belah Ketupat"])
    st.caption("Dibuat dengan :fire: oleh **Chandra**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi")
        sisi = st.number_input("Masukkan panjang sisi", min_value=0.0)
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"Luas Persegi: {luas}")
            st.success(f"Keliling Persegi: {keliling}")
            st.toast("Perhitungan selesai!")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi panjang")
        panjang = st.number_input("Masukkan panjang", min_value=0.0)
        lebar = st.number_input("Masukkan lebar", min_value=0.0)
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas Persegi Panjang: {luas}")
            st.success(f"Keliling Persegi Panjang: {keliling}")
            st.snow()
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung 'luas' dan 'keliling' lingkaran")
        jari_jari = st.number_input("Masukkan jari-jari", min_value=0.0)
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            st.success(f"Luas Lingkaran: {luas}")
            st.success(f"Keliling Lingkaran: {keliling}")
            st.balloons()
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung 'luas' dan 'keliling' segitiga")
        alas = st.number_input("Masukkan alas", min_value=0.0)
        tinggi = st.number_input("Masukkan tinggi", min_value=0.0)
        sisi_a = st.number_input("Masukkan panjang sisi A", min_value=0.0)
        sisi_b = st.number_input("Masukkan panjang sisi B", min_value=0.0)
        sisi_c = st.number_input("Masukkan panjang sisi C", min_value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi_a + sisi_b + sisi_c
            st.success(f"Luas Segitiga: {luas}")
            st.success(f"Keliling Segitiga: {keliling}")
            st.toast("Perhitungan segitiga selesai!")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)

    case "Belah Ketupat":
        st.title("Belah Ketupat")
        st.markdown("Menghitung 'luas' dan 'keliling' belah ketupat")
        d1 = st.number_input("Masukkan diagonal 1", min_value=0.0)
        d2 = st.number_input("Masukkan diagonal 2", min_value=0.0)
        sisi = st.number_input("Masukkan panjang sisi", min_value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = 0.5 * d1 * d2
            keliling = 4 * sisi
            st.success(f"Luas Belah Ketupat: {luas}")
            st.success(f"Keliling Belah Ketupat: {keliling}")
            st.toast("Perhitungan belah ketupat selesai!")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)

    case _ :
        st.error("Terjadi kesalahan")
