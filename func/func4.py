def capitalize(*kelimeler):
    capital_kelimeler = []
    for kelime in kelimeler:
        tmp = kelime[0].upper()
        capital_kelimeler.append(f"{tmp}{kelime[1::]}")
    return capital_kelimeler

print(capitalize("ahmet","mehmet"))
