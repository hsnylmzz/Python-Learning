import random

def iki_zar_at():
    birinci_zar = random.randint(1,6)
    ikinci_zar = random.randint(1,6)
    return birinci_zar, ikinci_zar

def iyi_mi(ilk_zar, ikinci_zar):
    if ilk_zar + ikinci_zar == 2:
        print("Kötü zar ama fena değil.")
        return False
    elif ilk_zar + ikinci_zar == 3:
        print("Rezalet!")
        return False
    elif ilk_zar < 3 or ikinci_zar < 3:
        print("Kötü zar.Öğren de gel.")
        return False
    elif ilk_zar + ikinci_zar == 12:
        print("İyi zar. Çok şanşlısın!!!")
        return True
    else:
        print("İyi zar. Bu sefer şansın yaver gitti.")
        return True

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

