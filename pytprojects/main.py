import stocklist
import product_class
import profit
import date
import requests

def getR():
    return requests.get("http://167.71.7.181/products").json()

products = []

try:
    products = stocklist.getOlder()

except Exception:
    stocklist.updateList(getR())

cevaplar = [" Huzur Market uygulamasına hoşgeldiniz ! ",
            " Ürün Satın almak için , type : BUY product_name product_amount_to_buy ",
            " Ürün satmak için , type : SELL product_name product_amount_to_sell product_value_to_sell ",
            " Kar edilenler listesi için , type : PROFIT ",
            " Ciro edilenler listesi için , type : CIRO ",
            " Üretilen ürün listesi için , type : PRODUCT ",
            " Çıkış için, type : 0"]

for i in cevaplar:
    print(i)

while True:
    cevaplar = list(input("Ne yapmak istiyorsunuz ?").split())
    cevaplar[0].lower()
    if cevaplar[0] == 'buy':
        try:
            r = getR()
            if cevaplar[1] in products.keys():
                for i in r:
                    if i["name"] == cevaplar[1]:
                        index = r.index(i)
                        break
                products[cevaplar[1]].buyProduct(int(cevaplar[2]), r[index]["price"], r[index]["tax"], date.getDate())
                stocklist.updateList(r)
            
            else:
                products[cevaplar[1]] = product_class.Product(cevaplar[1])
                for i in r:
                    if i["name"] == cevaplar[1]:
                        index = r.index(i)
                        break
                products[cevaplar[1]].buyProduct(int(cevaplar[2]), r[index]["price"], r[index]["tax"], date.getDate())
                stocklist.updateList(r)
        
        except Exception as e:
            print(f"Received {e} error, control you typed true !")
    
    elif cevaplar[0] == "sell":
        try:
            products[cevaplar[1]].sellProduct(int(cevaplar[2]), float(cevaplar[3]), date.getDate)
        
        except Exception as e:
            print(f"Received {e} error ,control you typed true !")

    elif cevaplar[0] == "product":
        try:
            for i in products:
                line = ""
                line += products[i].productValues[0] + " "
                line += "Amount: " + str(products[i].productValues[1]) + " "
                line += "Price: " + str(products[i].productValues[2]) + " "
                line += "Tax: " + str(products[i].productValues[3]) + "\n"
                print(line)
        except Exception as e:
            print(f"Received {e} error ,control you typed true !")
    
    elif cevaplar[0] == "q":
        stocklist.endProgram(products)
        break
    else:
        print("Her şey gerçek olsa")