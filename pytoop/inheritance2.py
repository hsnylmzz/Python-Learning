class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan Sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgileri_göster(self):
        print("Çalışan Sınıfın Bilgileri....")
        print("İsim : {} \nMaaş : {} \nDepartman : {} ".format(self.isim,self.maaş,self.departman))
    
    def departman_değiştir(self,yeni_departman):
        print("Departman değiştiriyor....")
        self.departman = yeni_departman
    
    def maaş_arttır(self,zam_miktarı):
        print("Maaş arttırılıyor....")
        self.maaş += zam_miktarı
class Yönetici(Çalışan):
    pass

yönetici1 = Yönetici("Hasan Yılmaz",10000,"Bilgisayar Mühendisi")
yönetici1.departman_değiştir("Elektrik Elektronik Mühendisi")
yönetici1.maaş_arttır(5000)
yönetici1.bilgileri_göster()