from zar_kutuphanesi import iki_zar_at, iyi_mi   #from modülü zar_kutuphanesi.py uzantısından import edilir
                                                 #import fonksiyon veya classları diğer .py uzantılı dosyada kullanılır
kazanc = 0
kayip = 0

while kazanc != 2 and kayip != 2:
    input("Zar atmak için <Enter>'a basın.")
    zar_1, zar_2 = iki_zar_at()
    zar_durumu = iyi_mi(zar_1, zar_2)
    if zar_durumu:
        kazanc += 1
    else:
        kayip += 1
   
if kazanc > kayip:
    print("Kazandın.")
else:
    print("Kaybettin.")
