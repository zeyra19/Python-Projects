#özet: Inheritance çalışanların zamı ve yazılımıların zamı farklı olsun. Sadece yazılımcı da olan özel şeyler olsun

class Calisan:
    zam_oranı = 1.1
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@mail.com"

    def bilgi_goster(self):
        return [self.isim, self.soyisim, self.maas, self.email]

# calisan1 = Calisan("zehra", "çalşan", 10_000)


class Yazılımcı(Calisan):
    def __init__(self, isim, soyisim, maas, bildigi_dil):
        # üstten aldık ismi maaşı vs bildiği dili de kendimiz oluşturduk
        super().__init__(isim, soyisim, maas)
        self.bildigi_dil = bildigi_dil

    def dilini_söyle(self):
        print(f"Bildiğim dil {self.bildigi_dil}")

    zam_oranı = 1.2


class Yonetici(Calisan):

    def __init__(self, isim, soyisim, maas, calisanlar=None):
        super().__init__(isim, soyisim, maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self, *calisanlar):
        for calisan in calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self, calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisan_göster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgi_goster())


yazılımcı1 = Yazılımcı("Zehra", "yazılımcı", 60_000, "Python")
yazılımcı2 = Yazılımcı("Zehra", "Frontend", 20_000, "React")
yazılımcı3 = Yazılımcı("Zehra", "Backend", 40_000, "Python")

yönetici1 = Yonetici("OĞulcan", "Yönetici", 100_000)
yönetici1.calisan_ekle(yazılımcı1, yazılımcı2, yazılımcı3)
yönetici1.calisan_göster()
print("***********************************************************************")
yönetici1.calisan_sil(yazılımcı2)
yönetici1.calisan_göster()

print(isinstance(yönetici1, Calisan)) # Yönetici'nin base classı calisan bu yüzden true
print(isinstance(yönetici1, Yazılımcı))

print(issubclass(Yonetici, Calisan)) # yönetici classının ana basei Çalışan classı mı
