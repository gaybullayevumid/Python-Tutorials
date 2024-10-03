# def funksiya_nomi(parametrlar):
#     # Funksiya tanasi (bu yerda kod yoziladi)
#     return qaytadigan_qiymat

# def hello_world():
#     print("Hello world")

# hello_world()


# def yigindini_xisobla(a, b):
#     natija = a + b
#     return natija

# # Funksiyani chaqirish
# son = yigindini_xisobla(3, 5)
# print(son)  # Natija: 8

# def kvadratni_hisobla(son):
#     return son ** 2

# # Bu yerda 'son' parametr bo'lib, qiymat bilan to'ldiriladi.
# natija = kvadratni_hisobla(5)
# print(natija)  # Natija: 25

# def yigindini_xisobla(a, b):
#     return a + b

# # 'a' va 'b' parametrlar uchun beriladigan qiymatlar bu yerda argumentlar bo'ladi.
# natija = yigindini_xisobla(3, 7)
# print(natija)  # Natija: 10

# def yigindini_xisobla(a, b):
#     return a + b

# # Bu yerda 'b' birinchi, 'a' esa ikkinchi bo'lib berilmoqda.
# natija = yigindini_xisobla(b=3, a=2)
# print(natija)  # Natija: 5

# def kvadratni_xisobla(son):
#     return son ** 2

# natija = kvadratni_xisobla(4)
# print(natija)  # Natija: 16

# def salomlash(ism="Sirojbek"):
#     print(f"Salom, {ism}!")

# # salomlash()  # Natija: Salom, Do'stim!
# salomlash("Ali")  # Natija: Salom, Ali!

# def summa(*args):
#     return sum(args)
# # *args bilan foydalanish
# print(summa(1, 2, 3, 4))  # Natija: 10

# def malumot_korsat(**kwargs):
#     for kalit, qiymat in kwargs.items():
#         print(f"{kalit}: {qiymat}")

# # **kwargs bilan foydalanish
# malumot_korsat(ism="Ali", yosh=25, shahar="Toshkent")
# # Natija:
# # ism: Ali
# # yosh: 25
# # shahar: Toshkent

# lambda argumentlar: ifoda

# yigindi = lambda x, y: print(x + y)
# yigindi(5, 3)

# sonlar = [1, 2, 3, 4]
# kvadratlar = list(map(lambda x: x ** 2, sonlar))
# print(kvadratlar)  # Natija: [1, 4, 9, 16]

# sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
# juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
# print(juft_sonlar)  # Natija: [2, 4, 6, 8]

# mevalar = ["olma", "banan", "apelsin", "anor"]
# tartiblangan = sorted(mevalar, key=lambda x: len(x))
# print(tartiblangan)  # Natija: ['olma', 'anor', 'banan', 'apelsin']

# def tashqi_funksiya(karrali):
#     return lambda x: x * karrali

# ikki = tashqi_funksiya(2)
# # uch = tashqi_funksiya(3)

# print(ikki(5))  # Natija: 10
# # print(uch(5))  # Natija: 15

# def tashqi_funksiya(x):
#     def ichki_funksiya(y):
#         return y ** 2
#     return ichki_funksiya(x) + 5

# natija = tashqi_funksiya(3)
# print(natija)  # Natija: 14

