class Magaza():
    kitaplar = []
    
    @classmethod 
    def kitap_ekle(cls, kitap):
        cls.kitaplar.append(kitap)

Magaza.kitap_ekle("1")
print(Magaza.kitaplar)
m1 = Magaza()
m1.kitap_ekle("2")
print(Magaza.kitaplar)
