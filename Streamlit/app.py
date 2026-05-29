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
    pilihan = st.selectbox("Pilih Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran"])
    st.caption("Dibuat dengan :fire: oleh **Chandra**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi")
        sisi = st.number_input("Masukkan panjang sisi")
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
        panjang = st.number_input("Masukkan panjang")
        lebar = st.number_input("Masukkan lebar")
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
        jari_jari = st.number_input("Masukkan jari-jari")
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

    case _ :
        st.error("Terjadi kesalahan")
