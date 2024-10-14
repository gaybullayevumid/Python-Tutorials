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