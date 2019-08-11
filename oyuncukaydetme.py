print("Oyuncu kaydetme Programı")
oyuncu_listesi = []
adi = input("Oyuncu Adı : ")
soyadi = input("Oyuncu Soyadı : ")
film_ismi = input("Oyuncunun Oynadığı Film İsmi : ")

oyuncu_listesi = [adi,soyadi,film_ismi]

print("{} {} adlı oyuncu {} filminde rol almıştır.".format(oyuncu_listesi[0],oyuncu_listesi[1],oyuncu_listesi[2]))