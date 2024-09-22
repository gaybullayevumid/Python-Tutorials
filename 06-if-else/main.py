# if shart:
#     # Bu yerda shart bajarilganda bajariladigan kodlar

# x = 10
# if x > 5:
#     print("x 5 dan katta")

# age = input('Enter your age:')
# if int(age) >= 18:
#     print("Siz ovoz bera olasiz!")

# if shart:
#     # Bu yerda shart bajarilganda bajariladigan kodlar
# else:
#     # Bu yerda shart bajarilmaganda bajariladigan kodlar

# x = 3
# if x > 5:
#     print("x 5 dan katta")
# else:
#     print("x 5 dan kichik yoki teng")

# age = input('Enter your age:')
# if int(age) >= 18:
#     print("You're eligible to vote.")
# else:
#     print("You're not eligible to vote.")


# my_list = [1, 2, 3]

# if my_list:  # Ro'yxat bo'sh bo'lmasa
#     print("Ro'yxat to'la")
# else:
#     print("Ro'yxat bo'sh")

# my_list = [1, 2, 3, 4, 5]
# Element mavjudligini tekshirish
# num = int(input('son kiriting>>>'))
# if num in my_list:
#     print(f"{num} ro'yxatda mavjud")
# else:
#     print(f"{num} ro'yxatda mavjud emas")

#! Ro'yxat uzunligini tekshirish
# if len(my_list) >= 5:
#     print("Ro'yxatdagi elementlar soni 5 dan ko'p")
# else:
#     print("Ro'yxatdagi elementlar soni 5 yoki undan kam")


# my_list = [1, 2, 3, 4, 5]

# if len(my_list) > 3 and 7 in my_list:  # Ro'yxat uzunligi 3 dan katta va 2 elementi mavjud bo'lsa
#     print("Ro'yxatda 3 dan ortiq element va 2 elementi mavjud")
# else:
#     print("Shartlar bajarilmadi")


# my_tuple = ()

# if my_tuple:  # Tuple bo'sh bo'lmasa
#     print("Tuple to'la")
# else:
#     print("Tuple bo'sh")

# my_dict = {"name": "Alice", "age": 25}

# if my_dict:  # Dictionary bo'sh bo'lmasa
#     print("Dictionary to'la")
# else:
#     print("Dictionary bo'sh")


# my_dict = {'a': 1, 'b': 2, 'c': 3}

# Kalit mavjudligini tekshirish
# if 'b' in my_dict:
#     print("'b' kaliti lug'atda mavjud")
# else:
#     print("'b' kaliti lug'atda mavjud emas")

# Qiymat mavjudligini tekshirish
# if 2 in my_dict.values():
#     print("2 qiymati lug'atda mavjud")
# else:
#     print("2 qiymati lug'atda mavjud emas")

# my_dict = {
#     "name": "Alice", 
#     "age": 25, 
#     "city": "New York"
#     }

# if "age" in my_dict and my_dict["age"] > 20:  # "age" kaliti mavjud va qiymati 20 dan katta bo'lsa
#     print("Yoshi 20 dan katta")
# else:
#     print("Shart bajarilmadi")


# my_dict = {
#     "name": "Alice", 
#     "age": 25, 
#     "city": "New York"}

# if len(my_dict) > 3:  # Dictionaryda 2 dan ortiq kalit mavjud bo'lsa
#     print("Dictionaryda 2 dan ortiq kalit mavjud")
# else:
#     print("Dictionaryda 2 yoki undan kam kalit mavjud")


# if shart1:
#     # Bu yerda shart1 bajarilganda bajariladigan kodlar
# elif shart2:
#     # Bu yerda shart2 bajarilganda bajariladigan kodlar
# else:
#     # Bu yerda hech qaysi shart bajarilmaganda bajariladigan kodlar

# x = 10
# if x > 10:
#     print("x 10 dan katta")
# elif x > 5:
#     print("x 5 dan katta lekin 10 dan kichik yoki teng")
# else:
#     print("x 5 dan kichik yoki teng")

# my_list = [1, 2, 3, 4, 5]
# #       5
# if len(my_list) == 0:
#     print("Ro'yxat bo'sh")
#     #     5                    5
# elif len(my_list) > 0 and len(my_list) <= 3:
#     print("Ro'yxatda 3 yoki undan kam element bor")
# else:
#     print("Ro'yxatda 3 dan ortiq element bor")

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# if set1 == set2:  # Ikkala set bir xil bo'lsa
#     print("Setlar teng")
# elif set1 and set2:  # Ikkala setda umumiy elementlar bo'lsa
#     print("Setlarda umumiy elementlar mavjud")
# else:
#     print("Setlarda umumiy elementlar yo'q")


# my_dict = {"name": "Alice", "age": 25}

# if "name" not in my_dict:
#     print("Ism kiritilmagan")
# elif my_dict["age"] < 18:
#     print("Yosh kichikroq")
# else:
#     print("Ism va yosh mos")

# x = 7
# y = 10
# if x > 5 and y > 5:
#     print("x va y har ikkalasi ham 5 dan katta")
    
# if x > 5 or y < 5:
#     print("yoki x 5 dan katta yoki y 5 dan kichik")

# #       7 > 10
# if not (x > 10):
#     print("x 10 dan katta emas")

# x = 8
# if x > 5:
#     if x < 10:
#         print("x 5 dan katta va 10 dan kichik")
#     else:
#         print("x 10 dan katta yoki teng")
# else:
#     print("x 5 dan kichik yoki teng")

# x = 10
# y = 20
# z = 30
# if x > 5:  # Birinchi darajadagi shart
#     if y > 15:  # Ikkinchi darajadagi shart
#         if z > 25:  # Uchinchi darajadagi shart
#             print("x 5 dan katta, y 15 dan katta, va z 25 dan katta")
#         else:
#             print("x 5 dan katta, y 15 dan katta, lekin z 25 dan kichik yoki teng")
#     else:
#         print("x 5 dan katta, lekin y 15 dan kichik yoki teng")
# else:
#     print("x 5 dan kichik yoki teng")


# username = input("Username ni kiriting>\n>>>")
# password = input("Parolni kiriting\n>>>")

# if username == "admin" and password == "1234":  # Birinchi darajadagi shart
#     print("Tizimga kirdingiz!")
# else:
#     print("Parol yoki username xato")
