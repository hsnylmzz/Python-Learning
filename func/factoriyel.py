def factoriyel(girdi):
    sonuc = 1
    for i in range(1,girdi+1):
        sonuc = sonuc * i
    return sonuc

print(factoriyel(5))
     