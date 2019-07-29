class Kitap():
    def __init__(self, adi, dil, kiralanabilir=True, satilabilir=False):
        self.adi = adi
        self.dil = dil
        self.kiralanabilir = kiralanabilir
        self.satilabilir = satilabilir 
    
    def __str__(self):
        return f"'{self.adi}'"
