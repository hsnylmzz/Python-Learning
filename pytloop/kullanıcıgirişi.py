print("**********\nKullanıcı Girişi\n**********\n")

# Kullanıcı Adı Girişi örneğinin gerçek versiyonunu PyQT5 derslerinde bulabilirsiniz.

sys_kul_adı = "hasan" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Kullanıcı Adı

sys_parola  = "12345" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Parola

giriş_hakkı = 3

while True:
    kul_adı = input("Kullanıcı Adı: ")
    parola = input("Şifre: ")
    
    if (kul_adı != sys_kul_adı and parola == sys_parola):
        print("Kullanıcı Adı Yanlış")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ",giriş_hakkı)
    elif (kul_adı == sys_kul_adı and parola != sys_parola):
        print("Şifre Yanlış")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ",giriş_hakkı)
    elif (kul_adı != sys_kul_adı and parola != sys_parola):
        print("Hepsi Yanlış")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ",giriş_hakkı)
    else:
        print("Giriş doğru")
        break
    if(giriş_hakkı == 0):
        print("Giriş hakkınızı kaybettiniz.")
        break
