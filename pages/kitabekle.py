import streamlit as st
st.write("Kitap Kayıt Bölümü 📖")
kitap_isim = st.text_input("Kitap ismi")
yazar = st.text_input("Yazar İsmi")
yayin_evi = st.text_input("Yayin evi")
uploaded_file = st.file_uploader("Choose a file")

btn = st.button("Kayıt Et")
btnClear = st.button("Formu temizle")