# PYTHON DASTURLASH ASOSLARI

## 11-dars Modullar

## MODUL NIMA?
Funksiyaning qulayliklaridan biri, ko'p takrorlanadigan kodlarni funksiya ichida yashirishimiz va kerak bo'lgan murojat qilishimiz mumkinligida. Maqsadimiz dasturimizni ixcham va tushunarli qilib, kelajakda o'zimiz yoki boshqalar uchun ham `toza` kod qoldrisih. Bu yo'nalishda yana bir qadam qo'yib, dasturimizni modullarga ajratimshimiz mumkin. 

Modul bu loyihamiz ichidagi alohida fayl bo'lib, dasturimiz davomida ishlatiladigan funskyalarni (va o'zgaruvchilarni) mana shu faylga joylab, ko'zdan yashirib qo'yishimiz mumkin. Bu bizga asosiy dasturimizdan chalg'imasdan kod yozish imkoniyatini beradi. 

Modul va uning ichidagi funksiyalarni istalgan payt asosiy dasturimizga yuklab olishimiz, modullarni boshqa dasturchilar bilan ulashishimiz yoki kelajakda o'zimizning boshqa loyihalarimizda foydalanishimiz mumkin.

Umuman olganda katta dasturlar bir nech o'nlab modullardan iborat bo'lishi tabiiy hol.

## MODULLARNI `import` QILISH
- Pythonda modullardan foydalanish uchun avvalo ularni `import` qilish kerak. Modullarni **import** qilish uchun `import` kalit so'zidan foydalaniladi.

- `math` modulini `import` qilish
```python
import math

radius = 5
yuza = math.pi * (radius ** 2)
print(f"Aylananing yuzasi: {yuza}")
```
Yuqoridagi misolda `math` moduli import qilinadi va undan `pi` konstantasi yordamida aylananing yuzasi hisoblanadi.

- `import modul_nomi` sintaksisi Pythonda bir modulni `import` qilish uchun ishlatiladi. Bu sintaksis orqali siz Python modullarini skriptlaringizda yoki boshqa modullarda ishlatishingiz mumkin.

- Sintaksisi
```python
import modul_nomi
```
`from modul_nomi import funksiya_yoki_object` sintaksisi yordamida siz ma'lum bir moduldan faqat kerakli `funksiya` yoki `o'zgaruvchini` import qilishingiz mumkin. Bu sizga modulni to'liq import qilmasdan, faqat zaruriy qismlarini olish imkonini beradi.

```python
from modul_nomi import funksiya_yoki_object
```

## MODULLARDAN MUAYYAN QIMSLARNI IMPORT QILISH
- Agar siz faqat ma'lum bir funksiyani yoki o'zgaruvchini `import` qilishni istasangiz, `from ... import ...` sintaksisidan foydalanishingiz mumkin.
`sqrt` funksiyasini `math` modulidan import qilish
```python
from math import sqrt

son = 16
ildiz = sqrt(son)
print(f"{son} ning kvadrat ildizi: {ildiz}")
```
Yuqoridagi misolda biz faqat **sqrt**(kvadrat ildizi) funksiyasini `math` modulidan import qildik.

## MODULGA BOSHQA NOM BERISH
- Modulni import qilishda unga qisqa yoki qulayroq nom berish uchun `as` operatoridan foydalanishingiz mumkin.
```python
import math as m

radius = 7
diametr = 2 * m.pi * radius
print(f"Aylananing diametri: {diametr}")
```
Bu yerda `math` moduli `m` nomi bilan import qilingan va kodda shu nom bilan ishlatilgan.

## MODUL YARATISH
- Modul yaratish uchun asosiy dasturimizdagi funksiyalarni yangi faylga ko'chiramiz xolos. Modulga oson murojat qilishimiz uchun, faylimiz asosiy dasturimiz bilan bitta papkada bo'lgani afzal. Bunda adashib ketmaslik uchun, loyihangizning(dasturning) asosiy faylini `main.py` deb nomlash o'rinli. 

```python
# mymodule.py

def greet(name):
    """Salomlashish funktsiyasi."""
    return f"Salom, {name}!"

def add(a, b):
    """Ikki sonni qo'shish funktsiyasi."""
    return a + b

def multiply(a, b):
    """Ikki sonni ko'paytirish funktsiyasi."""
    return a * b

class Person:
    """Shaxs klassi."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """Shaxsni tanishtiruvchi metod."""
        return f"Men {self.name} va {self.age} yoshdaman."
```

### MODULDAN FOYDALANISH
- `Modul` yaratganingizdan so'ng, uni boshqa Python dasturlarida `import` qilib ishlatishingiz mumkin.
`main.py`
```python
# main.py

import mymodule

# Funksiyalardan foydalanish
print(mymodule.greet("Ali"))
print(mymodule.add(5, 3))
print(mymodule.multiply(4, 7))

# Klasslardan foydalanish
person = mymodule.Person("Omar", 25)
print(person.introduce())
```
### MODULNI KENGAYTIRISH
- Modulga qo'shimcha funksiyalar yoki klasslar qo'shishingiz mumkin. <br>
Masalan: `mymodule.py`
```python
def subtract(a, b):
    """Ikki sondan birini ayirish funktsiyasi."""
    return a - b

def divide(a, b):
    """Ikki sonni bo'lish funktsiyasi."""
    if b == 0:
        raise ValueError("Bo'lish uchun 0 bilan bo'lish mumkin emas!")
    return a / b
```

## FOYDALI MODULLAR
### SANA VA VAQT BILAN ISHLASH UCHUN

- `datetime` moduli sana va vaqt bilan ishlash uchun juda foydali. Ushbu modul quyidagi asosiy komponentlarni o'z ichiga oladi:
- **datetime:** Sana va vaqtni ifodalovchi obyektlar yaratish uchun.
- **date:** Faqat sana ma'lumotini ifodalash uchun.
- **time:** Faqat vaqt ma'lumotini ifodalash uchun.
- **timedelta:** Sana yoki vaqt o'rtasidagi farqni ifodalash uchun.
- **timezone:** Soat zonalarini boshqarish uchun.

1. `datetime` - sana va vaqtni ifodalash uchun ishlatiladi:
```python
from datetime import datetime

# Hozirgi sana va vaqtni olish
now = datetime.now()
print(now)  # 2024-08-19 14:30:00.123456

# Sana va vaqtni formatlash
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2024-08-19 14:30:00
```
2. `date` - faqat sana ma'lumotini saqlaydi:
```python
from datetime import date

# Hozirgi sanani olish
today = date.today()
print(today)  # 2024-08-19

# Sana obyektini yaratish
specific_date = date(2024, 8, 19)
print(specific_date)  # 2024-08-19
```
3. `time` - faqat vaqt ma'lumotlarini saqlaydi:
```python
from datetime import time

# Vaqt obyektini yaratish
specific_time = time(14, 30, 45)
print(specific_time)  # 14:30:45
```
4. `timedelta` - ikki sana yoki vaqtni o'rtasidagi farqni ifodalash uchun ishlatiladi:
```python
from datetime import datetime, timedelta

# Hozirgi sana va vaqt
now = datetime.now()

# 5 kun qo'shish
future_date = now + timedelta(days=5)
print(future_date)

# 5 kun oldingi sana
past_date = now - timedelta(days=5)
print(past_date)
```
5. `timezone` - soat zonalarini boshqarish uchun ishlatiladi:
```python
from datetime import datetime, timedelta

# Hozirgi sana va vaqt
now = datetime.now()

# 5 kun qo'shish
future_date = now + timedelta(days=5)
print(future_date)

# 5 kun oldingi sana
past_date = now - timedelta(days=5)
print(past_date)
```


