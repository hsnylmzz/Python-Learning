from kitap import Kitap
from insan import Insan

kitap1 = Kitap("Beyaz Geceler", "Türkçe")
kitap2 = Kitap("Sefiller", "İngilizce", kiralanabilir=False, satilabilir=True)
kitap3 = Kitap("Savaş ve Barış", "Türkçe", False)

insan1 = Insan("Hamdi")
insan2 = Insan("Fatma")

insan1.kitap_kirala(kitap1)
insan1.kitap_satin_al(kitap2)
insan1.kitap_oku(kitap1)
insan1.kitap_oku(kitap2)

insan1.okudugum_kitaplari_listele()