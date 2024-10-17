# f = open("file.txt", "r")
# print(f.read())
import os

# f = open("file.txt", "r")

# Barcha ma'lumotni o'qish
# content = f.read()
# print(content)

# Bir qatorni o'qish
# line = f.readline()
# print(line)

# Barcha qatorlarni ro'yxatga o'qish
# lines = f.readlines()
# print(lines)
#
# f.close()

# Faylga ma'lumot yozish
# f = open("file.txt", "w")
# f.write("Hello, Python!\n")
# f.write("This is a second line.\n")
# f.write("Python")
# f.close()

# Ro'yxatni faylga yozish
# lines = ["First line\n", "Second line\n", "Third line\n", "20\n", "70", 'python']
# f = open("file.txt", "w")
# f.writelines(lines)
# f.close()




# f = open("file.txt", "r")
# print(f.read())
# # Fayldan o'qish jarayoni
# f.close()  # Faylni yopish


# with open("file.txt", "r") as f:
#     content = f.read()
#     print(content)
# Bu usulda faylni yopish shart emas, fayl avtomatik ravishda yopiladi.


# Ikkilik faylni o'qish
# with open("img.png", "rb") as img:
#     data = img.read()
#     print(data)

# Ikkilik faylga yozish
# with open("output.bin", "wb") as bin_file:
#     bin_file.write(b"Binary data")

import os

# Faylni o'chirish
# os.remove("output.bin")

# Fayl nomini o'zgartirish
# os.rename("file.txt", "python.txt")
# os.rename("file.txt", "python.jpg")

# Fayl mavjudligini tekshirish
# if os.path.exists("img.png"):
#     print("File exists")
# else:
#     print("File not found")