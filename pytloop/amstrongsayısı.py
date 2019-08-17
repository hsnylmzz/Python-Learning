sayı = input("Sayı: ")
basamak_sayısı = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

temp = sayı

while(temp > 0):
    basamak = temp % 10
    toplam += basamak ** basamak_sayısı
    temp //= 10

if(toplam == sayı):
    print("{} bir armstrong sayısıdır.".format(sayı))
else:
    print("{} bir armstrong sayısı değildir.".format(sayı))