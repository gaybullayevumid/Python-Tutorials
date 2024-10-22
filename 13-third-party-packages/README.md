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

4. `pandas` **Paketi**

```shell
pip install pandas
```

`pandas` paketi ma'lumotlarni tahlil qilish va ularga ishlov berishda juda foydali. U jadval ko'rinishidagi ma'lumotlar bilan ishlashni osonlashtiradi (masalan, `CSV` yoki `Excel` fayllari).

```python
import pandas as pd

# Jadval yaratish
data = {
    'Ism': ['Umid', 'Ali', 'Sarvar'],
    'Yosh': [23, 35, 29],
    'Kasb': ['Dasturchi', 'Muallim', 'Menejer']
}

df = pd.DataFrame(data)

# Jadvalni ko'rish
print(df)

# Faqat Ism ustunini chiqarish
print(df['Ism'])

# Yosh bo'yicha filtrlash
print(df[df['Yosh'] > 25])
```

5. `beautifulsoup4` **Paketi**

```python
pip install beautifulsoup4
```

`beautifulsoup4` paketi web sahifalardagi `HTML` kodlardan ma'lumotlarni ajratib olish uchun ishlatiladi. `Web scraping` deb ataladigan bu jarayonni osonlashtirish uchun foydalaniladi.

```python
import requests
from bs4 import BeautifulSoup

# Web sahifa so'rovi
url = "https://www.example.com"
response = requests.get(url)

# Sahifani pars qilish
soup = BeautifulSoup(response.text, 'html.parser')

# Sahifadagi barcha <a> teglarini topish
links = soup.find_all('a')

# Har bir linkni chop etish
for link in links:
    print(link.get('href'))
```

6. `flask` **Paketi**

```shell
pip install Flask
```

`flask` bu web ilovalarini yaratish uchun juda yengil va oson ishlatiladigan `web-freymvork`. Ushbu freymvork yordamida `web-serverlar`ni tez va oson yo'lga qo'yish mumkin.

```python
from flask import Flask

# Flask ilovasini yaratish
app = Flask(__name__)

# Bosh sahifa uchun view funksiyasi
@app.route('/')
def home():
    return "Salom, Flask!"

# Ilovani ishga tushirish
if __name__ == '__main__':
    app.run(debug=True)
```

7. `pytest` **Paketi**

```shell
pip install pytest
```

`pytest` bu Python kodlarini testlash uchun ishlatiladigan kuchli va moslashuvchan paketdir. U testlarni yozishni va sinovdan o'tkazishni osonlashtiradi.

```python
# test_mening_funksiyam.py faylida
def ikki_barobar(qiymat):
    return qiymat * 2

def test_ikki_barobar():
    assert ikki_barobar(3) == 6
    assert ikki_barobar(0) == 0
    assert ikki_barobar(-2) == -4

# Testlarni ishga tushirish uchun terminalda:
# pytest
```

# PyPI orqali paket qidirish va o'rnatish

`PyPI` web sayti (**https://pypi.org/**) orqali minglab paketlarni qidirish va topish mumkin. Misol uchun, biror matematik kutubxonani topish uchun `math` so'zini qidirish kifoya.

## Paketlarni boshqarish

> [!NOTE]
> Biror paketni o'rnatganingizdan so'ng, `pip` yordamida uni `yangilash` yoki `o'chirish` mumkin:

1. **Yangilash:**

```shell
pip install --upgrade package_name
```

2. **O'chirish:**

```shell
pip uninstall package_name
```

# Ko'p ishlatiladigan boshqa third-party paketlar:

- **scikit-learn:** Ma'lumotlarni tahlil qilish va mashinani o'qitish (`machine learning`) algoritmlari uchun ishlatiladi.
- **opencv-python:** Rasm va video ma'lumotlarini qayta ishlash uchun ishlatiladigan kutubxona.
- **sqlalchemy:** Ma'lumotlar bazalari bilan ishlashni osonlashtiradigan `ORM` kutubxonasi.
- **celery:** Katta hajmdagi ishlarni `asinxron` ravishda bajarish uchun freymvork.


# Paketlar bilan ishlashdagi ba'zi maslahatlar:

- `requirements.txt` **fayli:** Loyihangizdagi barcha paketlarni boshqarish uchun `pip freeze > requirements.txt` buyrug'i bilan paketlar ro'yxatini faylga yozib qo'yish mumkin.
- **Virtual environment:** Virtual muhit yordamida loyihangizdagi paketlarni izolyatsiya qilish yaxshi amaliyotdir. `venv` orqali virtual muhit yaratish mumkin:

```shell
python -m venv env
source env/bin/activate  # Linux yoki MacOS
env\Scripts\activate     # Windows
```

