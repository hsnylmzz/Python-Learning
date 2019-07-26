def camasir_yikama(degree, kirlilik, sikma=True, yikama=True):
    if kirlilik == "low":
        if degree >= 30 and yikama == True :
            return 1
        else:
            return 0
    elif kirlilik == "high":
        if degree > 40 and yikama == True and sikma == True :
            return 1
        else:
            return 0
    elif kirlilik == "middle":
        if degree > 35 and yikama == True and sikma == True :
            return 1
        else:
            return 0
result = camasir_yikama(36,"middle",False)
if result == 1 :
    print("Camasir mis gibi temiz")
else :
    print("Beceremedin.Bi daha yika")