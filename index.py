import streamlit as st
# import wikipedia as wp
st.header("Kursa Katılmak için 0 554 468 97 18", divider=True)
st.title("Python Kursuna hoşgeldiniz...👋")
st.write(":red[Kursumuz nisan ayında :blue[başlayacaktır].]")

# Burdaki butonla verileri getiriyoruz "r" readonly yani, okuma modunda açıoyruz
btn = st.button("Verileri Getir")
if btn :
    st.toast('Veriler Getiriliyor',icon='🎉')
    with open("bilgi.txt", "r", encoding="utf-8") as dosya:
     icerik = dosya.read()
     st.markdown(icerik)

btnRm = st.button("Verileri Sil",type="primary")
if btnRm : 
     st.toast('Veriler siliniyor🗑️')
     with open("bilgi.txt","w",encoding="utf-8") as dosya:
        dosya.writelines("")

x = st.chat_input("Aramık istediğiniz bilgi")
if x :
    with open("bilgi.txt","a",encoding="utf-8") as dosya:
        dosya.writelines(x + "\n") #\n enter tuşuna basmış
        st.write("Dosya oluştu") 
    
