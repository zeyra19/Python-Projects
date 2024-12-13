# # özet: dışardan etkilenen, bağımlı fonskiyon ve bağımsız fonksiyon
#
# A = 10
#
#
# def impure_sum(b):
#     return b + A
#
#
# print(impure_sum(5))
#
#
# def pure_sum(a, b):
#     return a + b
#
#
# print(pure_sum(5, 3))


# özet: lambda (isimsiz fonksiyon)
sırasız_liste = [("c", 3), ("a", 1), ("b", 2)]
sırasız_liste

print(sorted(sırasız_liste, key=lambda x: x[1]))
# Her bir öğeden (örneğin ("c", 3)), sadece ikinci kısmı (yani x[1] olan kısmı) al
# ve sıralamayı buna göre yap. ilk öğe ("c", 3) burada ikinci kısım 3”
# key parametresi, sıralamanın hangi kısmına veya kriterine göre yapılacağını belirtir. yani ikincilere göre sıralatıcam

