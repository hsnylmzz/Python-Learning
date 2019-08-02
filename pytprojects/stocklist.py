import product_class

def getOlder():
    with open("products.txt","r") as stock:
        allData = stock.readlines()
        products = []
        for i in allData:
            data = list(i[:-1].split())
            data[2] = int(data[2])
            data[3] = float(data[3])
            data[4] = float(data[4])
            product = [data[0], data[1], data[2], data[3], data[4]]
            products.append(product)
        productObjects = []
        for product in products:
            productObjects[product[1]] = product_class.Product(product[1])
            productObjects[product[1]].buyProduct(product[2], product[3], product[4], product[0])
        return productObjects

def getList():
    with open("stock.txt","r") as stock:
        allData = stock.readlines()
        products = []
        for i in allData:
            data = list(i[:-1].split())
            data[1] = float(data[1])
            data[2] = float(data[2])
            product = [data[0], data[1], data[2]]
            products.append(product)
        return products

def updateList(productList : list):
    with open("products.txt","w") as stock:
        allData = []
        for productDict in productList:
            info = ""
            info += productDict["name"] + " " + str(productDict["price"]) + " " + str(productDict["tax"]) + "\n"
            allData.insert(productList.index(productDict), info)
        stock.seek(0)
        stock.writelines(allData)

def endProgram(products: dict):
    with open("products.txt","w") as stock:
        allData = []
        for i in products:
            info = ""
            info += products[i].productValues[0] + " " + i
            info += " " + str(products[i].productValues[1])
            info += " " + str(products[i].productValues[2])
            info += " " + str(products[i].productValues[3]) + "\n"
            allData.append(info)
        stock.seek(0)
        stock.writelines(allData)