from random import random
print("Para atan program")
n=int(input("Kaç kez para atıyoz:"))
tura=0
yazi=0

para = []
for i in range(1, n + 1):
    x=random()
    if (x < 0.5):
        tura=tura+1
        para.insert(i, 'T')
    elif (x >= 0.5):
        yazi=yazi+1
        para.insert(i, 'Y')
print(para)
print('Tura sayısı', tura)
print('Yazı sayısı', yazi)
