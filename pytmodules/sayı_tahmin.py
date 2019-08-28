import random
import time

print(""" ***********************
SAYI TAHMIN OYUNU 

1 ile 40 arasında sayıyı tahmin edin.

******************************""")
rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:

    tahmin = int(input("Tahmininiz:"))

    if(tahmin < rastgele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin...")

        tahmin_hakkı -= 1
    elif(tahmin > rastgele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin...")

        tahmin_hakkı -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler ! Sayımız",rastgele_sayı)
        break
    if(tahmin_hakkı == 0):
        print("Tahmin hakkınız bitti...")
        print("Sayımız:",rastgele_sayı)
        break



