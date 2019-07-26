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



def capatalize(*args):
    name = "hasan"
    surname = "yilmaz"
    name_surname = name + surname 
    return name_surname
print(capatalize("hasan","yilmaz"))