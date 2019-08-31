class Yazılımcı():
    def __init__(self,ad,soyad,no,maaş,diller):
        self.ad = ad
        self.soyad = soyad
        self.no = no
        self.maaş = maaş
        self.diller = diller
    
    def maaş_arttır(self,zam_miktarı):
        self.maaş += zam_miktarı

yazılımcı1 = Yazılımcı("Hasan","Yılmaz",12345,10000,["C","Java"])
yazılımcı1.maaş_arttır(15000)
print(yazılımcı1.ad)
print(yazılımcı1.soyad)
print(yazılımcı1.no)
print(yazılımcı1.maaş)
print(yazılımcı1.diller)