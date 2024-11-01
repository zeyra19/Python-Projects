#özet: kullanıcıdan renk alır ve listeye ekler
renkler = ["kırmızı", "mavi", "sarı", "yeşil"]

for i in range(1):
    renk_gir = input("Sorgulamak istediğiniz rengi yazın::: ")
    if renk_gir in renkler:
        print("Bu renk zaten var")
    else:
        print("Bu renk gözümden kaçmış ekleyelim")
        renkler.append(renk_gir)
print(renkler)



#özet: kullanıcıdan aldığı bilgiyle bir dizi oluşturur ve son elemanını siler pop()
renkler = []
for i in range(5):
    renkler.append(input("Eklemek istediğiniz rengi girin"))
renkler.pop()
print(renkler)



#özet: kullanıcıdan başlangıç ve bitiş sayısı al, arasındaki sayıları yazdır
sayi_1 = int(input("Başlangıç sayısı girin: "))
sayi_2 = int(input("Bitiş sayısı girin: "))
for i in range(sayi_1, sayi_2):
    print(i, end=" ")



#özet: bir diziye ders notu ekleme
a = []
ad = input("Öğrenci adınızı girin")

for i in range(5):
    ders_notu = int(input("Ders Notunuzu girin"))
    a.append(ders_notu)

print(f"Öğrenci adı: {ad} ve ders notları:", a)
