sum = 0
while True:
    sayı = input("Sayı: ")
    if(sayı == "q"):
        break
    sayı = int(sayı)

    sum += sayı
print("Girilen sayının toplamı: ",sum)