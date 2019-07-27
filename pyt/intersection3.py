name = "çağrı"
print(name, set(name))
turkish_char = set("çÇşŞıİÖöÖüÜğĞ")
print(turkish_char)
print(turkish_char.intersection(set(name)))
print(turkish_char.intersection_update(set(name))) #İki metodun kesişimi alır
print(turkish_char.discard(set(name))) #remove() metodu gibi kümede istenilen elemanı silme yarıyor ama bu silmek istenilen eleman eğer kümenin içinde yoksa hata vermez.
print(turkish_char.difference_update(set(name))) #Bu metot hem iki küme arasındaki farkı bulur hemde kümeyi günceller
