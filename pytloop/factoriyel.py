print("************** Faktoriyel Hesaplama Programı ***************** ")
print("Çıkmak için q'ya basın.")

while True:
    sayı = input("Sayı: ")
    if (sayı == "q"):
        print("Programdan çıkılıyor...")
        break
    sayı = int(sayı)
    fact = 1

    for i in range(2,sayı+1):
        fact *= i
    
    print("Faktoriyel: ",fact)