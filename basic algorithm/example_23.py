#özet: kullanıcı formu classı yap
class Form():
    def __init__(self, isim, soyad, adres, telefon):
        self.isim = isim
        self.soyad = soyad
        self.adres = adres
        self.telefon = telefon

    def fill_form(self):
        print("Form dolduruluyor...")
        print(self.isim, self.soyad, self.adres, self.telefon)


kullanici = Form("Zehra", "Soyad", "Ankara", 18188181)
kullanici.fill_form()


#özet: kullanıcı formu classı yap ama telefon zorunlu olmasın
class Form():
    def __init__(self, isim, soyad, adres, telefon=None):
        self.isim = isim
        self.soyad = soyad
        self.adres = adres
        self.telefon = telefon

    def fill_form(self):
        print("Telefon bilgisi zorunlu değil, harici yerler zorunlu")
        print(self.isim, self.soyad, self.adres, self.telefon)


kullanici = Form("Zehra", "Soyad", "Ankara")
kullanici.fill_form()


#özet:  kullanıcı formu classı yap ama telefon zorunlu olmasın ve ekisk parametre olsun (belirt)
class Form():
    def __init__(self, isim="()", soyad="()", adres="()", telefon="()"):
        self.isim = isim
        self.soyad = soyad
        self.adres = adres
        self.telefon = telefon

    def fill_form(self):
        print("Zorunlu olmayan alanlar var karışık girecekseniz, lütfen belirtin (adres="") gibi")
        print(self.isim, self.soyad, self.adres, self.telefon)


kullanici = Form("Zehra", adres="Ankara")
kullanici.fill_form()