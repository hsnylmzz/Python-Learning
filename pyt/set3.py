def kume_dondur(str_kume: str):
    if str_kume.startswith("{") and str_kume.endswith("}"):
        kume_elemanlari = str_kume[1:len(str_kume) -1]
        v = kume_elemanlari.replace(", "," ")
        print(v)
       
kume_dondur("{1, 2, 3, 17}")
