class Yazılımcı():
    def __init__(self,ad,soyad,no,maaş,diller):
        self.ad = ad
        self.soyad = soyad
        self.no = no
        self.maaş = maaş
        self.diller = diller
    def bilgilerini_göster(self):
        print("""
        Çalışan Bilgisi :

        Adı : {}

        Soyadı : {}

        Numara : {}

        Maaşı : {}

        Diller : {}
        
        """.format(self.ad,self.soyad,self.no,self.maaş,self.diller))
    
    def dil_ekle(self,yenidil):
        print("Yeni bir dil ekleniyor..")
        self.diller.append(yenidil)

    def maaş_arttır(self,zam_miktarı):
        print("Maaşınız artıyor...")
        self.maaş += 500

yazılımcı1 = Yazılımcı("Hasan","Yılmaz",12345,10000,["C","Java"])
yazılımcı1.dil_ekle("C++")
yazılımcı1.maaş_arttır(5000)
yazılımcı1.bilgilerini_göster()