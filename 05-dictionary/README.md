# PYTHON DASTURLASH ASOSLARI

## 5-dars Lug'at(Dictionary)

## LUG'AT(DICTIONARY) NIMA?

Python dasturlash tilida **lug'at**(`dictionary`) — `kalit-qiymat` juftliklarini saqlash uchun mo'ljallangan ma'lumotlar tuzilmasidir. `Lug'atlar` kalitlar yordamida ma'lumotlarga kirishni ta'minlaydi va ular tartibsiz, o'zgaruvchan (`mutable`) va takrorlanmas (`unique`) kalitlardan iborat bo'ladi.

### LUG'ATLARNING ASOSIY XUSUSIYATLARI
1. **Kalitlar va qiymatlar:**
    - Kalitlar (`keys`) va qiymatlar (`values`) juftliklar sifatida saqlanadi. Kalitlar unikal(`takrorlanmas`) bo'lishi kerak.
2. **Tartibsizlik:**
    - Python 3.7 va undan keyingi versiyalarida lug'atlar saqlash tartibini saqlaydi, lekin avvalgi versiyalarda tartibni saqlash kafolatlanmagan.
3. **O'zgaruvchanlik:**
    - Lug'atlar o'zgaruvchan bo'lib, yangi kalit-qiymat juftliklarini qo'shish, mavjudlarini o'zgartirish va o'chirish mumkin.
4. **Unikal Kalitlar:**
    - Har bir kalit faqat bir marta mavjud bo'lishi mumkin. Agar yangi kalit qo'shsangiz yoki mavjud kalitni yangilasangiz, eski qiymat yangisi bilan o'zgartiriladi.

### LUG'AT SINTAKSISI

```python
dict_name = {
    'key':'value'
}
```

### LUG'AT YARATISH
- Bo'sh lug'at yaratish:
```python
my_dict = {}
```

- Elementlar bilan lug'at yaratish:
```python
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
```

### LUG'ATLARNI BOSHQARISH

- Lug'atga element qo'shish uchun o'zgaruvchi nomidan kn `[]` qavs ochib ichiga kalit(key) ni beramiz, undan keyin qo'shmoqchi bo'lgan qiymat(value)imizni beramiz.
```python
my_dict['email'] = 'alice@example.com'
print(my_dict)
# {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
```

- Lug'atni yangilash:
```python
my_dict['age'] = 26
print(my_dict)
# {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
```
- Lug'at ichidagi e'lementlarni o'chirish uchun `del` funksiyasidan foydalanamiz:
```python
del my_dict['email']
print(my_dict)
# {'name': 'Alice', 'age': 26, 'city': 'New York'}
```
- Lug'atdagi e'lementlarni o'chirish uchun `.pop()` metodidan ham foydalansak bo'ladi:
```python
age = my_dict.pop('age')
print(age)  # 26
print(my_dict)  # {'name': 'Alice', 'city': 'New York'}
```

### E'LEMENTLARNI KO'RISH
- Kalitlarni olish:
```python
keys = my_dict.keys()
print(keys)  # dict_keys(['name', 'city'])
```
- Qiymatlarni olish:
```python
values = my_dict.values()
print(values)  # dict_values(['Alice', 'New York'])
```
- Kalit-qiymat juftliklarini olish:
```python
items = my_dict.items()
print(items)  # dict_items([('name', 'Alice'), ('city', 'New York')])
```

### LUG'ATLARNI BOSHQARISH

- Lug'atni tozalash uchun `.clear()` metodidan foydalanamiz:
```python
my_dict.clear()
print(my_dict)  # {}
```
- Lug'atni nusxalash uchun `.copy()` metodidan foydalanamiz:
```python
new_dict = my_dict.copy()
print(new_dict)
```

### LUG'ATLARDA FOYDALI METODLAR
- **`.get()` metodi:** Kalit bo'yicha qiymatni olish (kalit mavjud bo'lmasa, `None` qaytaradi).
```python
name = my_dict.get('name', 'Not Found')
print(name)  # 'Alice'
```
- **`.setdefault()` metodi:** Kalit mavjud bo'lmasa, qiymat qo'shadi va qaytaradi.
```python
country = my_dict.setdefault('country', 'USA')
print(country)  # 'USA'
print(my_dict)  # {'name': 'Alice', 'city': 'New York', 'country': 'USA'}
```

## AMALIYOT

- otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: `Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan`

- Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: `Alining sevimli taomi osh`

- Berilgan `student` lug'atidagi age kalitining qiymatini `1` ga oshiring va yangi `grade` kalit-qiymat juftligini qo'shing.
```python
student = {
    'name': 'Alice',
    'age': 21,
    'major': 'Mathematics'

    # student = {'name': 'Alice', 'age': 22, 'major': 'Mathematics', 'grade': 'A'}
}
```

- Berilgan `employee` lug'atidan `department` kalitini o'chiring va yangi lug'atni chop eting.
```python
employee = {
    'name': 'John',
    'age': 30,
    'position': 'Manager',
    'department': 'Sales'

    # employee = {'name': 'John', 'age': 30, 'position': 'Manager'}
}
```

- `grades` lug'atidagi barcha qiymatlarning yig'indisini hisoblang va natijani chop eting.
```python
grades = {
    'Math': 90,
    'Science': 85,
    'English': 92,
    'History': 88

    # Yig'indi: 355
}
```

- `scores` lug'atidagi `eng kichik` va `eng katta` qiymatlarni toping va ularni chop eting.
```python
scores = {
    'player1': 35,
    'player2': 42,
    'player3': 28,
    'player4': 50

    # Eng kichik qiymat: 28
    # Eng katta qiymat: 50
}
```