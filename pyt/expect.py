while True:
    try:
        x = int(input("Sayi girin: "))
        break
    except ValueError:
        print("Bu bir sayi degildir.Sayi gir: ")