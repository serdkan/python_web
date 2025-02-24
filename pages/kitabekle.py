import streamlit as st
import uuid

st.write("Kitap Kayıt Bölümü 📖")
kitap_isim = st.text_input("Kitap ismi")
yazar = st.text_input("Yazar İsmi")
yayin_evi = st.text_input("Yayin evi")
yayin_tarihi = st.date_input("Yayın Tarihi")

btn = st.button("Kayıt Et")
if btn : 
    basharf = kitap_isim[0].upper()
    kimlik = uuid.uuid4()
    with open(F"{basharf}.txt","a",encoding="utf-8") as dosya:
        dosya.writelines("\n"+str(kimlik).replace("-","")+"-"+kitap_isim + "-" + yazar + "-" + yayin_evi + "-" +str(yayin_tarihi)+  "\n")
        st.write("Kitap Kaydedildi")
        st.toast("Kitap Kaydedildi",icon="📖")


btnClear = st.button("Formu temizle")
