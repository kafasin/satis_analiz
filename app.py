import streamlit as st

st.title("Kar/Zarar Tablosu")

st.subheader("Lütfen Gerekli Bilgileri giriniz!")
st.write("--------------")

col1, col2, col3 = st.beta_columns(3)

with col1:
    mal_agirlik_kg = int(st.number_input("Kac ton mal alinacak (ton)",
                                    value=20,
                                    step=1)) * 1000

    alis_fiyati_kg = float(st.number_input("Alis Fiyati (euro/kg)",
                                    value=0.5,
                                    step=0.05))

    nakliyat = int(st.number_input("Nakliyat Masrafi (euro)",
                                min_value=0,
                                max_value=15000,
                                value=7500,
                                step=500))

    gumruk = int(st.number_input("Gümrük Masrafi (euro)",
                                min_value=0,
                                max_value=15000,
                                value=1500,
                                step=500))

with col3:
    extra = int(st.number_input("Ongörülemeyen Masraflar (%)",
                                    value=5,
                                    step=1)) / 100

    beklenen_kar = int(st.number_input("Beklenen Kar (%)",
                                    value=20,
                                    step=1)) / 100


    diger_kar = int(st.number_input("Diger Saticilarin Tahmini Kar Oranlari (%)",
                                    value=20,
                                    step=1)) / 100

    telef = int(st.number_input("Malin Telef Olma Yuzdesi (%)",
                                    value=5,
                                    step=1)) / 100

    hesapla = st.button("Hesapla")





st.write("--------------------")

col11, col22, col33 = st.beta_columns(3)

if hesapla:
    with col22:
        toplam_maliyet = (mal_agirlik_kg * alis_fiyati_kg + nakliyat + gumruk) * (1 + extra)
        kar = toplam_maliyet * beklenen_kar
        hale_satis_fiyati = (toplam_maliyet * (1 + beklenen_kar)) / (mal_agirlik_kg * (1 - telef))

        halin_satis_fiyati = hale_satis_fiyati * (1 + diger_kar)

        market_satis_fiyati = halin_satis_fiyati * (1 + diger_kar)

        st.write("Toplam Maliyet (Euro)", round(toplam_maliyet))
        st.write("Kar (Euro)", round(kar))
        st.write("Hale Satis Fiyati (Euro)", round(hale_satis_fiyati, 2))
        st.write("Halin Satis Fiyati (Euro)", round(halin_satis_fiyati, 2))
        st.write("Market Fiyati (Euro)", round(market_satis_fiyati, 2))
