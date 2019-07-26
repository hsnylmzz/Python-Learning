def factoriyel(girdi):
    sonuc = 1
    for i in range(1,girdi+1):
        sonuc = sonuc * i
    return sonuc



def recursive_factoriyel(girdi):
    if girdi < 1:
        return 1
    else :
        sonuc = girdi * recursive_factoriyel(girdi -1)
        return sonuc
print(recursive_factoriyel(3))
print(f"""Recursive Result {recursive_factoriyel(5)} 
Duz sonuc {factoriyel(3)}""")