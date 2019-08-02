def getRound(x: str):
    return x[:x,index(".")+3]

def calculateProfir(name, profit):
    try:
        with open("profit.txt","r+") as profitText:
            allData = profitText.readlines()
            already = False 
            for i in allData:
                if i.startswith(name):
                    allData[allData.index(i)] = name + " " +getRound(str(profit)) + "\n"
                    already = True
                    break
                if not already:
                    allData.append(name + " " + getRound(str(profit)) + "\n")
            profitText.seek(0)
            profitText.writelines(allData)
    except Exception:
        with open("profit.txt","r") as profitText:
            profitText.write(name + " " + getRound(str(profit)) + "\n")

def getProfit(name):
    try:
        with open("profit.txt","r") as profitText:
            allData = profitText.readlines() 
            for i in allData:
                if i.startswith(name):
                    product = list(i.split())
                    return float(product[1])
            return 0
    except Exception as e:
        return 0

def printProfit():
    try:
        with open("profit.txt","r") as profitText:
            allData = profitText.readlines() 
            for i in allData:
                if i.startswith(name):
                    print(i[:-1])
                
    except Exception:
        print("Orada profit verisi yok.")