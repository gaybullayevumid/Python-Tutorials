# PYTHON DASTURLASH ASOSLARI

# 13-dars Uchinchi tomon kutubxonalari

Python kutubxonalari uchta asosiy guruhga bo'linadi: `standart` kutubxonalar, `ikkinchi tomon` kutubxonalari va `uchinchi tomon` kutubxonalari. Ularning har biri turli maqsadlarga xizmat qiladi.


1. **Standart kutubxonalar:**
Python o'zi bilan birga keladigan va alohida o'rnatishni talab qilmaydigan kutubxonalar. Ular Python bilan birga o'rnatilgan va keng foydalanish uchun mo'ljallangan:
- `math`: matematik funksiyalar (sinus, kosinus, logarifm).
- `datetime`: sana va vaqt bilan ishlash.
- `os`: operatsion tizim bilan o'zaro aloqa qilish.
- `random`: tasodifiy sonlar generatsiyasi.
- `json`: JSON formatidagi ma'lumotlarni kodlash va dekodlash.
- `sys`: tizim bilan bog'liq ma'lumotlar va parametrlarni boshqarish.

2. **Ikkinchi tomon kutubxonalari:**
Python jamoasi yoki uning yadro qismi tomonidan ishlab chiqilmagan, lekin keng qo'llaniladigan kutubxonalar. Bular odatda tashqi manbalardan (masalan, `PyPI` orqali) o'rnatiladi, ammo ular keng ommalashgan va ishonchli hisoblanadi. Bu kutubxonalar ko'pincha loyiha davomida qo'shimcha imkoniyatlarni taqdim etadi:
- `requests`: HTTP so'rovlarini jo'natish va qabul qilish.
- `beautifulsoup4`: HTML va XML dan ma'lumotlarni tahlil qilish va olish.
- `lxml`: XML va HTML ma'lumotlarini boshqarish.
- `pandas`: ma'lumotlar tahlili va qayta ishlash uchun.
- `numpy`: katta hajmdagi ma'lumotlar va raqamli hisob-kitoblar uchun.

3. **Uchinchi tomon kutubxonalari:**
Python jamoasidan tashqaridagi ishlab chiquvchilar tomonidan yaratilgan va maxsus vazifalarni hal qilish uchun mo'ljallangan kutubxonalar. Ularni `pip` orqali o'rnatish mumkin va ular har xil sohalarda qo'llaniladi. Uchinchi tomon kutubxonalari ko'pincha maxsus loyihalar uchun yaratiladi:
- `TensorFlow`: machine learning va sun'iy intellekt modellari yaratish uchun.
- `Flask` va `Django`: veb-dasturlash uchun.
- `Pygame`: o'yinlar yaratish uchun.
- `Scikit-learn`: statistik modellash va mashina o'rganish uchun.
- `Matplotlib` va `Seaborn`: ma'lumotlarni vizualizatsiya qilish uchun grafik kutubxonalar.


> [!NOTE]
> Python dasturlash tilida `third-party packages` (**uchinchi tomon paketlari**) — bu boshqa dasturchilar tomonidan yozilgan, ammo Pythonning standart kutubxonalariga kiritilmagan paketlar yoki kutubxonalardir. Bu paketlar turli vazifalarni osonlashtirish yoki kengaytirish uchun yaratiladi va ular odatda `pip` (**Python Package Installer**) orqali tarqatiladi.

# Third-Party Packages o'rnatilishi

- Paketlarni o'rnatish uchun odatda `pip` (**Python Package Installer**) ishlatiladi. Misol uchun, `requests` paketini o'rnatish uchun quyidagi buyruqni ishlatasiz:

```shell
pip install requests
```

# Third-Party Packages bilan ishlash

Third-party paketlarni o'rnatib bo'lgandan keyin, ularni Python kodida foydalanish uchun `import` qilamiz.

1. `requests` **Paketi**

`requests` paketi `HTTP` so'rovlar bilan ishlash uchun mo'ljallangan. Bu paket yordamida web sahifalardan ma'lumot olishni osonlashtirish mumkin.

```Python
import requests

# Biror web sahifaga so'rov jo'natish
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Javob ma'lumotlarini olish
if response.status_code == 200:
    data = response.json()  # Ma'lumotni JSON formatida olish
    print(data[0])  # Birinchi postni chop etish
else:
    print('So\'rov muvaffaqiyatsiz bo\'ldi.')
```

2. `numpy` **Paketi**

```shell
pip install numpy
```

`numpy` paketi katta o'lchamdagi massivlar bilan ishlash uchun mo'ljallangan bo'lib, matematik operatsiyalarni oson va samarali bajaradi.

```Python
import numpy as np

# 1 dan 10 gacha bo'lgan sonlar bilan massiv yaratish
arr = np.arange(1, 11)

# Massivdagi barcha elementlarning kvadratini hisoblash
squares = arr ** 2

print("Asl massiv:", arr)
print("Kvadratlar:", squares)
```

3. `matplotlib` **Paketi**

```shell
pip install matplotlib
```

`matplotlib` grafik chizish va ma'lumotlarni vizual ko'rinishda ko'rsatish uchun ishlatiladi.

```python
import matplotlib.pyplot as plt

# Ma'lumotlar
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Grafikni chizish
plt.plot(x, y, marker='o')

# Grafik nomlari
plt.title('Oddiy Grafik')
plt.xlabel('X o\'qi')
plt.ylabel('Y o\'qi')

# Grafikni ko'rsatish
plt.show()
```

# PyPI orqali paket qidirish va o'rnatish

`PyPI` web sayti (**https://pypi.org/**) orqali minglab paketlarni qidirish va topish mumkin. Misol uchun, biror matematik kutubxonani topish uchun `math` so'zini qidirish kifoya.