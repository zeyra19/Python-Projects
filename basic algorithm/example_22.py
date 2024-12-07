# Object Oriented Programming
#özet: class oluştur ve eleman(lar)ı çağır
class Car():
    marka = "Tesla"
    model = "Y"
    fiyat = 1_000_000
    sahibi = "Zeyra"

    def write_car(self):
        print(
            self.marka,
            self.model,
            self.fiyat,
            self.sahibi
        )

car = Car()
car.write_car()
print(car.sahibi)


#özet: clasa parametre vererek yap
class Car():
    def __init__(self, marka, model, fiyat, sahibi):
        self.marka = marka
        self.model = model
        self.fiyat = fiyat
        self.sahibi = sahibi

    def write_car(self):
        print(self.marka, self.model, self.fiyat, self.sahibi)

    def change_model(self, marka):
        self.marka = marka


zeyras_car = Car("Tesla", "Y", 1_000_000, "Zeyra")
zeyras_car.change_model("Bmw") #spesifik bir alt özelliği değiştirdim
zeyras_car.write_car()


# ogulcans_car = Car("Audi", "Qutro", 1_000_000, "Oğulcan")
# ogulcans_car.write_car()