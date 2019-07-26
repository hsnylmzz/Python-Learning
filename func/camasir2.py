argumanlar = ["yeter", "artik", "yetheeer"]
anahtarli_argumanlar = {"tarhana":True, "cacik":False}

def neler_oluyor_ya(*args, **kwargs):
    print(args)
    print(kwargs)

neler_oluyor_ya(*argumanlar, **anahtarli_argumanlar)
neler_oluyor_ya(argumanlar[0], argumanlar[1], argumanlar[2], tarhana = anahtarli_argumanlar.get("tarhana"), cacik = anahtarli_argumanlar.get("cacik"))