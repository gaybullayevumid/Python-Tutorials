# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# my_list.sort()
# print(my_list)

# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list)
# print(sorted_list)  # [1, 1, 3, 4, 5, 9]
# print(my_list)      # [3, 1, 4, 1, 5, 9]

# my_list = [3, 1, 4, 1, 5, 9]
# my_list.sort(reverse=True)
# # my_list.sort()
# print(my_list)  # [9, 5, 4, 3, 1, 1]

# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list, reverse=True)
# print(sorted_list)  # [9, 5, 4, 3, 1, 1]
# print(my_list)      # [3, 1, 4, 1, 5, 9]

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged_list = list1 + list2
# print(merged_list)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# import itertools

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined_list = list(itertools.chain(list1, list2))
# print(combined_list)

# multi_dimensional_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     'hello',
#     ["Hello", "python"],

# ]

# print(multi_dimensional_list[4][1])  # 3
# multi_dimensional_list.append([10, 11, 12])
# multi_dimensional_list.insert(2, ['Behruz', 'Umid'])
# print(multi_dimensional_list)

# multi_dimensional_list[0] = [13, 14, 15]
# print(multi_dimensional_list)

# multi_dimensional_list[1][1] = 99
# print(multi_dimensional_list)

# my_list = [1, 2, 3]
# multiplied_list = my_list * 2
# print(multiplied_list)

# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)  # True
# print(6 in my_list)  # False


# my_list = input("sonlarni taqoslsh uchun ikkta son kiriting:").split("")
# a = int(n[0])
# b = int(n[1])
# if a>b: max= a
# else:

# my_list = [1, 2, 3, 5, 8, 6, ]
# my_list.sort( reverse=True)
# # print(sorted_list)
# print(my_list)

# list1= [1, 2, 23,]
# list2 = [8, 12, 1]

# merged_list = list1 + list2
# merged_list.sort()
# print(merged_list)


# davlatlar = ["Uzbekistan", "India", "Japan"]
# sorted_list = sorted(davlatlar, reverse=False )
# print(sorted_list)

# raqamlar = [2, 8, 1, 9]
# eng_katta = max(raqamlar)
# eng_kichik = min(raqamlar)
# print(f"Raqamlar ro'yhatimiz ichida eng kattasi {eng_katta}")
# print(f"Raqamlar ro'yhatimiz ichida eng kichigi {eng_kichik}")

# yigindi = sum(raqamlar)
# print(yigindi)

# sonlar = list(range(10)) # 0dan 10gacha oraliqda sonlar yaratadi
# sonlar.sort(reverse=True)
# print(sonlar)

# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# # Oddiy tuplam yaratish
# my_tuple = (1, 2, 3)
# print(my_tuple)  # (1, 2, 3)

# # list dan tuplam yaratish
# another_tuple = tuple([4, 5, 6])
# print(another_tuple)  # (4, 5, 6)

# # bo'sh tuplam yaratish
# empty_tuple = ()
# print(empty_tuple)  # ()

# # bitta elementli tuplam yaratish uchun vergul qo'yish kerak
# single_element_tuple = (1,)
# print(single_element_tuple)  # (1,)

# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple[0])  # 10
# print(my_tuple[2])  # 30
# print(my_tuple[-1]) # 50 (oxirgi element)

# my_tuple = (1, 2, 3, 4, 5)
# print(len(my_tuple))  # 5

# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)

# animals = ("rabit","tigr","lion")
# print(animals)

# animals = ("rabit","tigr","lion")
# animals = list(animals)
# print(animals[0])


# animals = ("rabit","tigr","lion")
# animals = list(animals)
# print(len(animals))

# animals = ("rabit","tigr","lion","dog","cat")


# ismlar = ["Behruz", "Shahrizoda", "Hamidjon"]
# print(f"Salom {ismlar[0].upper()}, bugun birga dars qilamizmi")
# print(f"Salom {ismlar[1].upper()}, bugun birga dars qilamizmi")
# print(f"Salom {ismlar[2].upper()}, bugun birga dars qilamizmi")