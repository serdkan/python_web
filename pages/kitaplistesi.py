import streamlit as st

arama = st.text_input("Aramak istediğiniz kitabın baş harfini giriniz")
if arama:
    ilk_harf = arama[0].upper()
    with open(F"{ilk_harf}.txt", "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
        liste = icerik.split("\n")
        for kitap in liste:
                ayrinti = kitap.split("-")
                if ayrinti[0] != "":
                    st.write(F" Kitap Adı: :red[{ayrinti[0]}] Yazar Adı: :blue[{ayrinti[1]}] Yayın Evi :green[{ayrinti[2]}] Yayın Tarihi: :blue[ {ayrinti[3]} -{ayrinti[4]}]")
    
