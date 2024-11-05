#özet: bir kaç kitap yazıcam, uygulama bana rastgele hangi kitabı okumamı söylicek
# bunun için python random modülünü kullanıcıaz
import random
books = [
        "Kendime Düşünceler	",
        "Mutlu Yaşam Üzerine - Yaşamın Kısalığı Üzerine",
        "Aklından Bir Sayı Tut",
        "Kadınlar Ülkesi",
        "Labirentindeki General",
    ]

pick_random_book = random.choice(books)
print("Okuman gereken ilk kitap: ", pick_random_book)




#özet: kullanıcıdan harf alır diziyi kontrol eder varsa uyar yoksa ekle.
char = input("Enter a char: ")
alphabet = ["a", "b", "c", "d", "e"]

if char in alphabet:
    print("This char already exist pls try another one.")
else:
    alphabet.append(char)
    print("added")
    print(alphabet)



#özet: email ve password doğrulama
email = input("E-posta adresin: ")
password = input("Şifre: ")
correct_email = "email"
correct_password = "password"

if email == correct_email and password == correct_password:
    print("Giriş başarılı")
else:
    print("Şİfre veya Email Hatalı. Tekrar deneyin")



#özet: şifre girmesi için kullanıcıya 3 hak ver
number = 1

while number <= 3:
    password = input("Enter your password: ")
    if password == "python":
        print("şifrenizi doğru girdiniz")
        break
    else:
        print(f"Bu {number}. denemeniz ve password yanlış")
    number += 1
print("")

