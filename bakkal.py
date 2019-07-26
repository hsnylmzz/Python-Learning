stok = {
    "elma": 10
}

fiyatlar = {
    "elma":{
        "alış": 1,
        "satış": 2
    } 
}

kar_zarar = {
    "elma": 4
}

def stok_yazdir():
    print(stok)

def stoga_urun_ekle(adi, adet, alis, satis):
    if stok.get(adi):
        print(f"{adi} urununden {stok[adi]['adet']} adet var.")
        stok[adi] += int(adet)
       # stok[adi]['adet'] = stok[adi]['adet'] + int (adet)
        fiyatlar[adi]['adet'] = float(alis)
        fiyatlar[adi]['satis'] = float(satis)
    else:
        stok[adi] = int(adet)
        fiyatlar[adi] = {
            
            "alış": float(alis),
            "satış": float(satis)
        }
    print(f"{adi} stogu guncellendi. Guncel adet : {stok[adi]}")

#def satis_yap(adi, adet):


while True:
    print("""
    0. Stoklara yeni urun girisi 
    1. Urun satisi 
    2. Karlilik hesapla
    3. Urun bazli karlilik hesapla
    4. Gun sonu""")
    secenek = input("Yapmak istediginiz eylemi girin: ")
    secenek = int(secenek)
    if secenek == 0:
        urun_adi = input("Urun adini girin: ")
        urun_adeti = input("Urun adetini girin: ")
        urun_alis = input("Urun alis fiyatini girin: ")
        urun_satis = input("Urun satis fiyatini girin: ")
        stoga_urun_ekle(urun_adi, urun_adeti,
                        urun_alis, urun_satis)
