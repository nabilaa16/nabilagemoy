import streamlit as st

st.title("🎈 nabilagemoy ")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG_20250527_084454.jpg", width=200)
st.image("file_00000000c2b061f7a933c095c260bbda.png", width=200)
st.image("IMG-20250526-WA0148.jpg", width=200)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
