# ism = "Umid"
# print("Mening ismim " + ism)


# ism = "Umid"
# familiya = "G'aybullayev"
# print(ism + " " + familiya)

# text = "Hello, World!"
# uzunlik = len(text)  # 13
# print(uzunlik)

# text = "Hello world!"
# first_char = text[0] # H
# last_char = text[-1]  # '!'
# substring = text[6:12]  # 'Hello'
# print(first_char)
# print(last_char)
# print(substring)

# text = "Hello"
# text_repeated = text * 3
# print(text_repeated)

# ism = "Umid"
# yosh = 20
# message = "Salom, Mening ismim " + ism + " Yoshim " + str(yosh) + "da"
# message_2 = f"Salom, Mening ismim {ism}. Yoshim {yosh}da"
# print(message_2)

# text = "hello"
# print(text.upper()) #HELLO

# text = "HELLO"
# print(text.lower()) #hello

# text = "hello world"
# print(text.capitalize()) # Hello world

# text = "hello world python base"
# print(text.title()) # Hello World

# text = "    hello world    "
# print(text)
# print(text.lstrip()) # "hello world    "
# print(text.rstrip())
# print(text.strip())


# text = "hello world"
# print(text)
# print(text.replace("hello", "hayr"))  # "hello Python"
# print(text.replace("world", "Python"))  # "hello Python"

# text = "hello world python salom"
# print(text.split()) # ['hello', 'world']

# words = ['hello', 'world', 'apple', 'car']
# print(" ".join(words))  # "hello world"


# text = "hello world"
# print(text.find("world"))  # 6


# text = "hello world"
# print(text.startswith("hello"))  # True


# text = "hello world"
# print(text.endswith("and"))  # True

# x = 10
# y = -5
# z = 0
# a = 12345678901234567890
#
# print(type(x))  # <class 'int'>
# print(type(y))  # <class 'int'>
# print(type(z))  # <class 'int'>
# print(type(a))  # <class 'int'>


# son = 4_032_903_290
# print(son)

# PI = 3.14
# print(PI)

# x, y, z = 10, -7.25, -30


# x = 10
# y = float(x)  # 10.0
#
# print(type(y))  # <class 'float'>
# print(y)        # 10.0

# x = 3.14
# y = int(x)  # 3
#
# print(type(y))  # <class 'int'>
# print(y)        # 3


# s = "123"
# x = float(s)  # 123
# print(type(s))
# print(type(x))  # <class 'int'>
# print(x)        # 123

# x = 3.14
# s = str(x)  # "3.14"
#
# print(type(s))  # <class 'str'>
# print(s)        # "3.14"


# #1 foydalanuvchining tug'ilgan yilini so'raymiz
# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# #2 foydalanuvchi yoshini xisoblaymiz
# yosh = 2024 - t_yil #
# #3 foydalanuvchi yoshini konsolga chiqaramiz
# print(f"Siz {yosh} yoshda ekansiz")


# pi = 3.14159 # o'nlik son (float)
# radius = 10  # butun son (integer)
# diametr = 2*radius
# print("Aylana uzunligi ", pi*diametr, " ga teng.")

# my_list = [1, 2, 3, 4, 5]
# uzunlik = len(my_list)
# print(uzunlik)
# # print(my_list[3])
# # print(my_list)

# meva = 'olma'
# mevalar = ['olma', 'anor']
#
# my_list = [1, 2, 3]
# my_list.append(6)
# print(my_list)

# my_list = [1, 2, 3]
# my_list.append([4, 5])  # List ichiga yana bir list qo'shish
# print(my_list)

# my_list = [1, 2, 3]
# my_list.extend([4, 5])
# print("extend() natijasi:", my_list) # Bu ro'yxatning elementlarini alohida qo'shadi

# my_list = [1, 2, 3]
# my_list.insert(1, 99)  # 2-pozitsiyaga 99 ni qo'shish
# print(my_list)

# my_list = [1, 2, 3]
# # my_list = my_list + [4,5]
# my_list += [4, 5]
# print(my_list)

# my_list = [1, 2, 3, 4, 3, 5]
# my_list.remove(3)  # Ro'yxatdan birinchi 3 ni o'chiradi
# print(my_list)
# my_list = [1, 2, 3, 4, 3, 5]
# # my_list.pop()
# # my_list.pop(4)
# my_list.clear()
# print(my_list)

# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# my_list.sort()
# print(my_list)

# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list)
# print(sorted_list)  # [1, 1, 3, 4, 5, 9]
# print(my_list)      # [3, 1, 4, 1, 5, 9]


# my_list = [3, 1, 4, 1, 5, 9]
# my_list.sort(reverse=False)
# print(my_list)  # [9, 5, 4, 3, 1, 1]


my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list, reverse=True)
# print(sorted_list)  # [9, 5, 4, 3, 1, 1]
# print(my_list)      # [3, 1, 4, 1, 5, 9]


# my_list.reverse()
# print(my_list)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1 += list2
# # merged_list = list1 + list2
# print(list1)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# import itertools
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined_list = list(itertools.chain(list1, list2))
# print(combined_list)

# multi_dimensional_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# multi_dimensional_list.append([10, 11, 12])
# print(multi_dimensional_list)


# print(multi_dimensional_list[1][1])


# multi_dimensional_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# change = multi_dimensional_list[2][1] = 10
# print(multi_dimensional_list)


# my_list = [1, 2, 3]
# multiplied_list = my_list * 3
# print(multiplied_list)

