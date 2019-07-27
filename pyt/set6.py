def kume_dondur(str_kume: str):
        if str_kume.startswith("{") and str_kume.endswith("}"):
            kume_elemanlari = str_kume[1:len(str_kume) -1]
            elemanlar = kume_elemanlari.split(", ")
            try:
                return {int(eleman) for eleman in elemanlar}
            except ValueError:
                raise ValueError("Küme elemanları geçerli değil")
        else:
            raise ValueError("Geçerli bir küme değil")
           
kume = input("küme girin: ")      
yeni_kume = kume_dondur(kume)
print(yeni_kume, type(yeni_kume))
