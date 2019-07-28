import random

def iki_zar_at():
    birinci_zar = random.randint(1,6)
    ikinci_zar = random.randint(1,6)
    return birinci_zar, ikinci_zar
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
