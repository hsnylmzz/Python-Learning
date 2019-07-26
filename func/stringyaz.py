turkish_cowboys = ["hamdi","cagri","yakup","sebnem","burhan"]
turkish_chars = "gusIİcOCOGuS"

def get_turks(cowboys):
    for cowboy in cowboys:
        for i in cowboy:
            if i in turkish_chars:
                print(cowboy)
                break

turks=get_turks(turkish_cowboys)
print(f"turks: {turks}")
cap = "kelime".capitalize()
print(cap)

def capatalize(kelime):
    tmp = kelime[0].upper()
    return f"{tmp}{kelime[1::]}"

print(capatalize("ahmet"))