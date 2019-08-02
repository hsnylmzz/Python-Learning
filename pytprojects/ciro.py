def calculateCiro(sell_amount, sell_value):
    return sell_amount-sell_value

def writeCiro(name, ciro):
    try:
        with open("ciro.txt","r+") as ciroText:
            allData = ciroText.readlines()
            already = False 
            for i in allData:
                if i.startswith(name):
                    allData[allData.index(i)] = name + " " + str(round(ciro, 2)) + "\n"
                    already = True
                    break
                if not already:
                    allData.append(name + " " + str(round(ciro, 2)) + "\n")
                ciroText.seek(0)
                ciroText.writelines(allData)

    except Exception:
        with open("ciro.txt","r+") as ciroText:
            ciroText.write(name + " " + str(round(ciro, 2)) + "\n")

def getCiro(name):
    try:
        with open("ciro.txt","r") as ciroText:
            allData = ciroText.readlines() 
            for i in allData:
                if i.startswith(name):
                    product = list(i.split())
                    return float(product[1])
            return 0
    except Exception as e:
        return 0

def printCiro():
    try:
        with open("ciro.txt","r") as ciroText:
            allData = ciroText.readlines() 
            for i in allData:
                if i.startswith(name):
                    print(i[:-1])
    except Exception:
        print("Orada ciro verisi yok.")
