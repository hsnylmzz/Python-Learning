sayı1 = int(input("Birinci Sayı: "))
sayı2 = int(input("İkinci Sayı: "))
sayı3 = int(input("Üçüncü Sayı: "))

if (sayı1 >= sayı2 and sayı1 >= sayı3):
    print("Max Deger: {}".format(sayı1))
elif (sayı2 >= sayı1 and sayı2 >= sayı3):
    print("Max Deger: {}".format(sayı2))
elif (sayı3 >= sayı1 and sayı3 >= sayı2):
    print("Max Deger: {}".format(sayı3))