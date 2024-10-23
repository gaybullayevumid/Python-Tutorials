# son = 20
# sonlar = [1,2,3,4,5,6]


# my_list = [1, 2, 3, 4, 5]

# my_list.extend([6, 7])
# print("extend() natijasi:", my_list) # Bu ro'yxatning elementlarini alohida qo'shadi
# my_list.append([6,7,8])
# print(my_list)




# print(my_list[0])  # Birinchi element
# print(my_list[-1])  # Oxirgi element
# print(my_list)


# my_list = [1, 2, 3]
# my_list.insert(2, 99)  # 2-pozitsiyaga 99 ni qo'shish
# print(my_list)

# my_list = [1, 2, 3]
# my_list += [4, 5]
# print(my_list)


# my_list = [1, 2, 3, 4, 3, 5]
# my_list.clear()
# print(f"Tozalangan list {my_list}")

# my_list.pop(1)
# print(my_list)


# my_list.remove(3)  # Ro'yxatdan birinchi 3 ni o'chiradi
# print(my_list)


# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# my_list.sort()
# print(my_list)


# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list)
# print(sorted_list)  # [1, 1, 3, 4, 5, 9]
# print(my_list)      # [3, 1, 4, 1, 5, 9]

# my_list = [3, 1, 4, 1, 5, 9]
# my_list.sort(reverse=True)
# print(my_list)  # [9, 5, 4, 3, 1, 1]

# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list, reverse=True)
# print(sorted_list)  # [9, 5, 4, 3, 1, 1]
# print(my_list)      # [3, 1, 4, 1, 5, 9]

# my_list = [3, 1, 4, 1, 5, 9]
# my_list.reverse()
# print(my_list)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged_list = list2 + list1
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
#     [7, 8, 9]
# ]

# change = multi_dimensional_list[1] = [10, 11, 12]
# print(multi_dimensional_list)
# print(change)



# my_list = [1, 2, 3]
# multiplied_list = my_list * 3
# print(multiplied_list)

# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)  # True
# print(6 in my_list)  # False


my_list = [10, 20, 30, 40, 50]
# # Ro'yxatdagi elementlar yig'indisini hisoblash
# sum_of_list = sum(my_list)
# print(f"Ro'yxatdagi elementlar yig'indisi: {sum_of_list}")


# Ro'yxatdagi eng katta qiymatni topish
# max_value = max(my_list)
# print(f"Ro'yxatdagi eng katta qiymat: {max_value}")

# Ro'yxatdagi eng kichik qiymatni topish
# min_value = min(my_list)
# print(f"Ro'yxatdagi eng kichik qiymat: {min_value}")


# sonlar = list(range(5, 11)) # 
# print(sonlar)


# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)


# # Oddiy tuple yaratish
# my_tuple = (1, 2, 3)
# print(my_tuple)  # (1, 2, 3)

# # list dan tuple yaratish
# another_tuple = tuple([4, 5, 6])
# print(another_tuple)  # (4, 5, 6)

# # bo'sh tuple yaratish
# empty_tuple = ()
# print(empty_tuple)  # ()

# # bitta elementli tuple yaratish uchun vergul qo'yish kerak
# single_element_tuple = (1,)
# print(type(single_element_tuple))  # (1,)



# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple[0])  # 10
# print(my_tuple[2])  # 30
# print(my_tuple[-1]) # 50 (oxirgi element)


# tuple1 = (1, 2)
# tuple2 = (3, 4)
# new_tuple = tuple1 + tuple2
# print(new_tuple)  # (1, 2, 3, 4)


# tuple1 = (1, 2, 3)

# # tuple1 ni o'z-o'zidan ikki marta birlashtirish
# result = tuple1 + tuple1
# print(result)


# tuple1 = ("hello", "World")
# new_tuple = tuple1 * 3
# print(new_tuple)  # ('hello', 'hello', 'hello')



# my_tuple = (1, 2, 3, 4, 5, 6, 7)
# print(len(my_tuple))  # 5


# mevalar = ("apple", "banana", "cherry")
# print("bananaadads" in mevalar)  # True


# my_tuple = ("apple", "banana", "cherry")
# (fruit1, fruit2, fruit3) = my_tuple
# print(fruit1)  # 'apple'
# print(fruit2)  # 'banana'
# print(fruit3)  # 'cherry'



# nested_tuple = (1, 2, (3, 4), 5)
# print(nested_tuple[2][0])  # (3, 4)



# my_tuple = (1, 2, 2, 3,2,4,5,2,6,3, "hello", 'hello')
# print(my_tuple.count('hello'))  # 2


# my_tuple = (1, 2, 3)
# print(my_tuple.index(3))  # 1


# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)


