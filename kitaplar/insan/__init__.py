class Insan():
    def __init__(self, adi):
        self.adi = adi
        self.bildigi_diller = set()
        self.okudugu_kitaplar = list()
        self.satin_aldigi_kitaplar = list()
        self.kiraladigi_kitaplar = list()
    
    def __str__(self):
        return self.adi

    def kitap_satin_al(self, kitap):
        if kitap.satilabilir:
            self.satin_aldigi_kitaplar.append(kitap)
        else:
            print(f"{kitap} satın alınamaz.")

    def kitap_kirala(self, kitap):
        if kitap.kiralanabilir:
            self.kiraladigi_kitaplar.append(kitap)
        else:
            print(f"{kitap} kiralanamaz.")
    
    def okudugum_kitaplari_listele(self):
        [print(f"Okuduğum kitaplar: {kitap}") for kitap in self.okudugu_kitaplar]

    def kitap_oku(self, kitap):
        if kitap in self.kiraladigi_kitaplar or kitap in self.satin_aldigi_kitaplar:
            self.okudugu_kitaplar.append(kitap)
            print(f"{kitap} okundu.")
        else:
            print(f"{kitap} envarterinizde yok.")
