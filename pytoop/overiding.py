class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan Sınıfının init fonksiyonu....")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgileri_göster(self):
        print("Çalışan Sınıfın Bilgileri....")
        print("İsim : {} \nMaaş : {} \nDepartman : {} ".format(self.isim,self.maaş,self.departman))
    
    def departman_değiştir(self,yeni_departman):
        print("Departman değiştiriyor....")
        self.departman = yeni_departman
    
class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,kişi_sayısı):
        print("Yönetici Sınıfının init fonksiyonu.... ")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı
    
    def zam_yap(self,zam_miktarı):
        print("Maaş arttırılıyor....")
        self.maaş += zam_miktarı

yönetici2 = Yönetici("Hasan Yılmaz",10000,"Bilgisayar Mühendisliği",10)
yönetici2.zam_yap(5000)
yönetici2.bilgileri_göster()
