sayı = int(input("Sayı: "))

i = 1
toplam = 0
while(i < sayı):
   if(sayı % i == 0):
       toplam += i
   i += 1
if(toplam == sayı): 
    print("{} sayı mükemmel sayıdır.".format(sayı))
else:
    print("{} sayı mükemmel sayı değildir.".format(sayı))