class Pizza:
    def __init__(self, pizza_adi,musteri_adi):
        self.pizza_adi = pizza_adi
        self.musteri_adi = musteri_adi
        self.price = 50
    def get_description(self): #Pizzanın Çeşidi 
        print("Müşterinin Adı : " + self.musteri_adi)
        print("Pizza Adı : " + self.pizza_adi)
    def get_cost(self): #Sosa göre Toplam ücreti hesaplanır
        print("1.Zeytin\n2.Mantarlar\n3.Keçi Peyniri\n4.Et\n5.Soğan\n6.Mısır")
        secim = int(input("Sos Seçiniz : "))
        if secim == 1:
            self.price += 3
            f = open("musteri.txt","a")  #Müşterinin adı ve istediği menü bu dosyada tutulur.
            f.write(self.musteri_adi)
            f.write("\t")
            f.write(self.pizza_adi)
            f.write("\t")
            f.write("Zeytinli")
            f.write("\t")
            f.write(str(self.price))
            f.write("\n")
            f.close()
            print("Sayın {} Zeytinli Pizzanız Hazır Ücretiniz {} TL".format(self.musteri_adi,self.price))
        elif secim == 2:
            self.price += 3
            f = open("musteri.txt","a")
            f.write(self.musteri_adi)
            f.write("\t")
            f.write(self.pizza_adi)
            f.write("\t")
            f.write("Mantarlı")
            f.write("\t")
            f.write(str(self.price))
            f.write("\n")
            f.close()
            print("Sayın {} Mantarlı Pizzanız Hazır Ücretiniz {} TL".format(self.musteri_adi,self.price))
        elif secim == 3:
            self.price += 3
            f = open("musteri.txt","a")
            f.write(self.musteri_adi)
            f.write("\t")
            f.write(self.pizza_adi)
            f.write("\t")
            f.write("Keçi Peynirli")
            f.write("\t")
            f.write(str(self.price))
            f.write("\n")
            f.close()
            print("Sayın {} Keçi Peynirli Pizzanız Hazır Ücretiniz {} TL".format(self.musteri_adi,self.price))
        elif secim == 4:
            self.price += 3
            f = open("musteri.txt","a")
            f.write(self.musteri_adi)
            f.write("\t")
            f.write(self.pizza_adi)
            f.write("\t")
            f.write("Etli")
            f.write("\t")
            f.write(str(self.price))
            f.write("\n")
            f.close()
            print("Sayın {} Etli Pizzanız Hazır Ücretiniz {} TL".format(self.musteri_adi,self.price))
        elif secim == 5:
            self.price += 3
            f = open("musteri.txt","a")
            f.write(self.musteri_adi)
            f.write("\t")
            f.write(self.pizza_adi)
            f.write("\t")
            f.write("Soğanlı")
            f.write("\t")
            f.write(str(self.price))
            f.write("\n")
            f.close()
            print("Sayın {} Soğanlı Pizzanız Hazır Ücretiniz {} TL".format(self.musteri_adi,self.price))
        elif secim == 6:
            self.price += 3 
            f = open("musteri.txt","a")
            f.write(self.musteri_adi)
            f.write("\t")
            f.write(self.pizza_adi)
            f.write("\t")
            f.write("Mısırlı")
            f.write("\t")
            f.write(str(self.price))
            f.write("\n")
            f.close()
            print("Sayın {} Mısırlı Pizzanız Hazır Ücretiniz {} TL".format(self.musteri_adi,self.price))
        else:
            print("Bu tip pizzamız bulunmamaktadır")
            
class Klasik(Pizza):
    def __init__(self, pizza_adi,musteri_adi):
        super().__init__(pizza_adi,musteri_adi)
        self.price = 55
class Margarita(Pizza):
    def __init__(self, pizza_adi,musteri_adi):
        super().__init__(pizza_adi,musteri_adi)
        self.price = 55
class TurkPizzasi(Pizza):
    def __init__(self, pizza_adi,musteri_adi):
        super().__init__(pizza_adi,musteri_adi)
        self.price = 60
class Sade(Pizza):
    def __init__(self, pizza_adi,musteri_adi):
        super().__init__(pizza_adi,musteri_adi)

isim = input("Adınızı Yazınız : ")
isim = str(isim)
secenek = input("Hangi pizzadan almak istiyorsunuz? Almak için seçin : ")
secenek = int(secenek)

match secenek:
     case 1:
        pizza = Klasik("Klasik Pizza",isim)
        pizza.get_description()
        pizza.get_cost()
     case 2:
        pizza = Margarita("Margarita",isim)
        pizza.get_description()
        pizza.get_cost()
     case 3:
        pizza = TurkPizzasi("Turk Pizzası",isim)
        pizza.get_description()
        pizza.get_cost()
     case 4:
        pizza = Sade("Sade",isim)
        pizza.get_description()
        pizza.get_cost()
     case _:
        print("Böyle bir pizzamız bulunmamaktadır")
          
"""if secenek == 1:
    pizza = Klasik("Klasik Pizza")
    pizza.get_description()
    pizza.get_cost()
elif secenek == 2:
    pizza = Margarita("Margarita")
    pizza.get_description()
    pizza.get_cost()
elif secenek == 3:
    pizza = TurkPizzasi("Türk Pizzası")
    pizza.get_description()
    pizza.get_cost()
elif secenek == 4:
    pizza = Sade("Sade")
    pizza.get_description()
    pizza.get_cost()
else:
    print("Böyle bir pizzamız bulunmamaktadır")
    break
"""
