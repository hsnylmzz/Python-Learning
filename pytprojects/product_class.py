import profit
import ciro
import history
import date

class Product():
    defined_products = []
    onjected_products = []

    def __init__(self, name):
        self.name = name 
        self.amount = 0
        self.productValues = [date.getDate(), self , amount, 0, 0]
        Product.defined_products.append(name)
        Product.onjected_products[self.name] = self
    def buyProduct(self, amount, price, tax, datee):
        self.datee = datee
        self.amount = self.productValues[1] + amount
        self.price = price
        self.tax = tax
        self.productValues = [self.date, self.amount, self.price, self.tax]

    def sellProduct(self, sell_amount, sell_value, sell_date):
        if self.productValues[1] < sell_amount:
            print(f"Birden fazla ürün satılamaz.({self.productValues[self.name][1]}")
        else:
            preprofit = profit.calculateProfit(self, sell_amount, sell_value)
            productprofit = profit.getProfit(self.name) + preprofit
            profit.writeProfit(self.name, productprofit)
            giro.writeGiro(self.name, giro.getGiro(self.name) + giro.calculateGiro(sell_amount, sell_value))
            history.saveToHistory(self, sell_amount, sell_value, sell_date)
            self.productValues = [sell_date, self.productValues[1]- sell_amount, self.productValues[2], self.productValues[3]]

    def __str__(cls):
        data = []
        for i in cls.onjected_products:
            info = ""
            info += cls.onjected_products[i].productValues[0] + " " + i
            info += " " + str(cls.onjected_products[i].productValues[1])
            info += " " + str(cls.onjected_products[i].productValues[2])
            info += " " + str(cls.onjected_products[i].productValues[3]) + "\n"
            data.append(info)
        return data
    
    def __repr__(cls):
        data = []
        for i in cls.onjected_products:
            info = ""
            info += cls.onjected_products[i].productValues[0] + " " + i
            info += " " + str(cls.onjected_products[i].productValues[1])
            info += " " + str(cls.onjected_products[i].productValues[2])
            info += " " + str(cls.onjected_products[i].productValues[3]) + "\n"
            data.append(info)
        return data
    