def capatalize(kelime):
    tmp = kelime[0].upper()
    return f"{tmp}{kelime[1::]}"

print(capatalize("ahmet"))