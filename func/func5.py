def capitalize(*kelimeler):
    capital_kelimeler = []
    for kelime in kelimeler:
        yeni_kelime = ""
        for index, karakter in enumerate(kelime):
            if index != 0:
                yeni_kelime += karakter
            else:
                yeni_kelime += karakter.upper()
        capital_kelimeler.append(yeni_kelime)
    return capital_kelimeler

print(capitalize("ahmet","mehmet"))