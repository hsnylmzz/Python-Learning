def saveToHistory(product, sell_amount, sell_value, sell_date):
    with open("history.txt","a") as history:
        history.write(sell_date + "Name:" + product_name)
        history.write(" Stock: " + str(product.name))
        history.write(" Buy Price: " + str(product.amount))
        history.write(" Tax : " + str(product.tax))
        history.write(" Selled Amount : " + str(sell_amount))
        history.write(" Sell Price : " + str(sell_value))
