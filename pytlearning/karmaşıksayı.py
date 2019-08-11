print("Karmaşık Sayıyı Koordinat Düzleminde Gösterme")
complex_nums = []
reel_sayi = int(input("Karmaşık Sayının Reel Kısmını yazınız : "))
im_sayi = int(input("Karmaşık Sayının İmajener Kısmını yazınız : "))

uzaklikkaresi = pow(reel_sayi,2) + pow(im_sayi,2)
uzaklık = uzaklikkaresi ** 0.5
complex_nums = [reel_sayi,im_sayi,uzaklık]
print("{} + {}i karmaşık sayının aralarındaki uzaklığı {} birimdir.".format(complex_nums[0],complex_nums[1],complex_nums[2]))