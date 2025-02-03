# kullanıcıdan eşyanın alındığı tarihi al ve servis zamanını hesapla
import datetime

date = input("Eşyanızı aldığınız tarihi girin (ör: 2000/12/12)")
date = date.split("/") #istenilen yerden metni bölüyor

time_used = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
now_date = datetime.datetime.now()

calculate = (now_date - time_used)
print(calculate)