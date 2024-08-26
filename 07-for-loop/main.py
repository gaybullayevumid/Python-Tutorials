# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

# # Mevalar ro'yxati
# fruits = ["olma", "banan", "gilos"]

# # Ro'yxat bo'yicha tsikl
# for fruit in fruits:
#     print(fruit)

# # Misol ro'yxat
# numbers = [1, 2, 3, 4, 5]

# # Har bir sonning kvadratini hisoblash uchun tsikl
# for number in numbers:
#     square = number ** 2
#     print(f"{number} ning kvadrati {square}")

# # Misol ro'yxat
# numbers = [10, 20, 30, 40, 50]

# # Yig'indini hisoblash uchun o'zgaruvchi
# total = 0

# # For tsikli bilan ro'yxat bo'ylab yurish
# for number in numbers:
#     total = total + number

# print(f"Yig'indi: {total}")


# # Misol ro'yxat
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Juft sonlarni saqlash uchun yangi ro'yxat
# even_numbers = []

# # For tsikli bilan ro'yxat bo'ylab yurish
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print(f"Juft sonlar: {even_numbers}")

# # Misol ro'yxat
# fruits = ["olma", "banan", "gilos"]

# # For tsikli bilan ro'yxat bo'ylab yurish
# for i in range(len(fruits)):
#     fruits[i] = fruits[i].upper()

# print(f"Katta harfdagi mevalar: {fruits}")

# for i in range(5):
#     print(i)

# for index in range(0, 11, 2):
#     print(index)

# person = {
#     "name": "John", 
#     "age": 30, 
#     "city": "New York"
#     }

# for key in person:
#     print(key, ":", person[key])

# person = {
#     'name':'Umid',
#     'age':20,
#     'job':'teacher'
# }

# for keys in person:
#     print(keys)

# person = {
#     'name':'Umid',
#     'age':20,
#     'job':'teacher'
# }

# for qiymat in person.values():
#     print(qiymat)

# person = {
#     'name':'Umid',
#     'age':20,
#     'job':'teacher'
# }
# for kalit, qiymat in person.items():
#     print(f"{kalit}: {qiymat}")

# numbers = {1, 2, 3, 4, 5}

# for num in numbers:
#     print(num)

# mevalar = {"olma", "banan", "uzum"}

# for meva in mevalar:
#     print(meva)

# coordinates = (10, 20, 30)

# for coordinate in coordinates:
#     print(coordinate)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()  # Qator oxirida yangi qatorga o'tish

# for i in range(5):
#     print(i)
# else:
#     print("Tsikl tugadi")

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     if number == 3:
#         break  # Agar son 3 ga teng bo'lsa, loop to'xtaydi
#     print(number)

# mevalar = ['olma', 'banan', 'apelsin', 'anjir']

# for meva in mevalar:
#     if meva == 'apelsin':
#         print('Apelsin topildi!')
#         break

# sonlar = [7, 11, 2, 6, 11]

# for son in sonlar:
#     if son % 2 == 0:
#         print(f'Juft son topildi: {son}')
#         break

# sonlar = [1, 2, 3, 4, 5]

# for son in sonlar:
#     if son % 2 == 0:
#         continue
#     print(son)

# sonlar = [-1, 2, -3, 4, -5]

# for son in sonlar:
#     if son > 0:
#         continue
#     print(son)

# mevalar = ['olma', 'banan', 'apelsin', 'anjir']

# for i in range(len(mevalar)):
#     if i % 2 != 0:
#         continue
#     print(mevalar[i])

# for son in range(5):
#     if son == 3:
#         pass
#     else:
#         print(son)
