# PYTHON DASTURLASH ASOSLARI

**Pythonda fayllar bilan ishlash dasturlashning muhim qismidir. Bu orqali siz ma'lumotlarni saqlash, o'qish, tahrirlash va boshqarish imkoniyatiga ega bo'lasiz.**

# Faylni ochish

Faylni ochish uchun `open()` funksiyasidan foydalaniladi. Bu funksiya fayl nomini va rejimini qabul qiladi. `open()` funksiyasida ikkinchi parametr sifatida fayl rejimini ko'rsatishingiz mumkin:

### Fayl rejimlari

- `r` – Faylni o'qish uchun ochish. Fayl mavjud bo'lishi kerak.
- `w` – Faylga yozish uchun ochish. Agar fayl mavjud bo'lmasa, yangi fayl yaratadi. Mavjud fayl bo'lsa, ma'lumotlarni o'chirib yuboradi.
- `a` – Faylga qo'shish uchun ochish. Mavjud faylga yangi ma'lumot qo'shadi, agar fayl mavjud bo'lmasa, yangi fayl yaratadi.
- `x` – Faylni faqat yangi fayl yaratish uchun ochadi. Agar fayl allaqachon mavjud bo'lsa, xato chiqaradi.

```python
# Faylni o'qish uchun ochish
f = open("file.txt", "r")

# Faylga yozish uchun ochish
f = open("file.txt", "w")

# Faylga qo'shish uchun ochish
f = open("file.txt", "a")

# Fayl mavjud emasligini tekshirib, yaratish
f = open("file.txt", "x")
```

# Faylni o'qish

Fayl ichidagi ma'lumotlarni o'qish uchun bir necha usullar mavjud:
- `read()` – Faylni to'liq o'qiydi.
- `readline()` – Fayldan bir qatorni o'qiydi.
- `readlines()` – Fayldagi barcha qatorlarni ro'yxat sifatida o'qiydi.

```python
f = open("file.txt", "r")

# Barcha ma'lumotni o'qish
content = f.read()
print(content)

# Bir qatorni o'qish
line = f.readline()
print(line)

# Barcha qatorlarni ro'yxatga o'qish
lines = f.readlines()
print(lines)

f.close()
```

# Faylga yozish

Faylga yozish uchun `write()` yoki `writelines()` metodlaridan foydalaniladi:
- `write()` – Faylga matn yozadi.
- `writelines()` – Ro'yxatdagi barcha qatorlarni faylga yozadi.

```python
# Faylga ma'lumot yozish
f = open("file.txt", "w")
f.write("Hello, Python!\n")
f.write("This is a second line.\n")
f.close()

# Ro'yxatni faylga yozish
lines = ["First line\n", "Second line\n", "Third line\n"]
f = open("file.txt", "w")
f.writelines(lines)
f.close()
```

# Faylni yopish

Fayl bilan ish tugagandan so'ng, uni yopish kerak. Faylni yopish uchun `close()` metodidan foydalaniladi.
```python
f = open("file.txt", "r")
# Fayldan o'qish jarayoni
f.close()  # Faylni yopish
```

> [!NOTE]
> Yana bir usul – faylni `with` bloki yordamida ochish, bunda fayl avtomatik ravishda yopiladi:
```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
# Bu usulda faylni yopish shart emas, fayl avtomatik ravishda yopiladi.
```

# Fayl rejimlari

- `t` – Matn rejimi. Fayllarni matn sifatida ochadi. Bu rejim `r` va `w` bilan birga ishlatiladi. Masalan, `rt` yoki `wt`.
- `b` – Ikkilik (`binary`) rejimi. Fayllarni ikkilik rejimda ochadi. Masalan, `rb` yoki `wb`.

```python
# Ikkilik faylni o'qish
with open("image.png", "rb") as img:
    data = img.read()
    print(data)

# Ikkilik faylga yozish
with open("output.bin", "wb") as bin_file:
    bin_file.write(b"Binary data")
```

# Fayllar bilan bog'liq ba'zi funksiyalar

- `os.remove()` – **Faylni o'chirish.**
- `os.rename()` – **Fayl nomini o'zgartirish.**
- `os.path.exists()` – **Fayl mavjudligini tekshirish.**

```python
import os

# Faylni o'chirish
os.remove("file.txt")

# Fayl nomini o'zgartirish
os.rename("old_name.txt", "new_name.txt")

# Fayl mavjudligini tekshirish
if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File not found")
```

# AMALIYOT

1. Yangi fayl yaratish va unga ma'lumot yozish:
- `example.txt` deb nomlangan yangi fayl yarating va unga `"Python is fun!"` yozuvini kiriting.
2. Fayldan ma'lumot o'qish
- Yaratilgan fayldan yozilgan ma'lumotni o'qing va ekranga chiqarib bering.