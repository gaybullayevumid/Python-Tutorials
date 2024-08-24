# PYTHON DASTURLASH ASOSLARI

## 9-dars Funksiyalar

> [!NOTE]
> Python dasturlash tilida `funksiyalar` bu kod bo'laklarini qayta-qayta ishlatish uchun qulay vositadir. `Funksiyalar` yordamida kodni tartibli, tushunarli va takrorlanadigan qila olamiz.

## FUNKSIYALARNI YARATISH VA CHAQIRISH
Pythonda funksiyani `def` kalit so'zi yordamida yaratamiz. Funksiya quyidagi tuzilishga ega:
```python
def funksiya_nomi(parametrlar):
    # Funksiya tanasi (bu yerda kod yoziladi)
    return qaytadigan_qiymat
```
### Oddiy funksiya
- Bu funksiya ikkita sonni qo'shib, natijani qaytaradi:
```python
def yigindini_xisobla(a, b):
    natija = a + b
    return natija

# Funksiyani chaqirish
son = yigindini_xisobla(3, 5)
print(son)  # Natija: 8
```
### PARAMETR VA ARGUMENTLAR
- Parametrlar
    - `Parametrlar` – bu funksiyani yaratishda unga o'tkaziladigan o'zgaruvchilar. `Parametrlar` funksiya tanasida ishlatiladigan qiymatlarni belgilaydi. Ular funksiyani chaqirganda haqiqiy qiymatlar bilan almashtiriladi.
```python
def kvadratni_hisobla(son):
    return son ** 2

# Bu yerda 'son' parametr bo'lib, qiymat bilan to'ldiriladi.
natija = kvadratni_hisobla(5)
print(natija)  # Natija: 25
```
- Argumentlar
    - `Argumentlar` – bu funksiyani chaqirganda `parametrlar` uchun beriladigan haqiqiy qiymatlar. Ular funksiyaga ma'lum bir qiymatlarni berish uchun ishlatiladi.
```python
def yigindini_xisobla(a, b):
    return a + b

# 'a' va 'b' parametrlar uchun beriladigan qiymatlar bu yerda argumentlar bo'ladi.
natija = yigindini_xisobla(3, 7)
print(natija)  # Natija: 10
```
### POSITION VA KALIT SO'ZLI ARGUMENTLAR
- Position argumentlar
    - Pozitsion argumentlar funksiyaga o'z joyi (`pozitsiyasi`) bo'yicha beriladi. Argumentlar `parametrlar` qatoriga mos ravishda ketma-ketlikda beriladi.
```python
def yigindini_xisobla(a, b):
    return a + b

# 'a' = 2 va 'b' = 3 bo'ladi.
natija = yigindini_xisobla(2, 3)
print(natija)  # Natija: 5
```
- Kalit so'zli argumentlar
    - Kalit so'zli argumentlar `parametr` nomi bilan bog'langan qiymat sifatida beriladi. Bu usul `pozitsion` ketma-ketlikka bog'liq emas va kodni tushunishni osonlashtiradi.
```python
def yigindini_xisobla(a, b):
    return a + b

# Bu yerda 'b' birinchi, 'a' esa ikkinchi bo'lib berilmoqda.
natija = yigindini_xisobla(b=3, a=2)
print(natija)  # Natija: 5
```

### QAYTISH QIYMATI(return)
> [!NOTE] 
> Funksiya natijani qaytarish uchun `return` operatoridan foydalanadi. `return` funksiyani to'xtatadi va qaytadigan qiymatni chaqirgan joyga yuboradi.
- Qaytarish qiymatli funksiya
```python
def kvadratni_xisobla(son):
    return son ** 2

natija = kvadratni_xisobla(4)
print(natija)  # Natija: 16
```
Yuqoridagi funksiya sonning kvadratini hisoblaydi

### DEFAULT QIYMATLAR
- Ba'zida `parametrlar` uchun oldindan belgilangan `standart` qiymatlar berish mumkin. Agar funksiyani chaqirganingizda bu `parametr` uchun qiymat bermasangiz, `standart` qiymatdan foydalaniladi.
```python
def salomlash(ism="Do'stim"):
    print(f"Salom, {ism}!")

salomlash()  # Natija: Salom, Do'stim!
salomlash("Ali")  # Natija: Salom, Ali!
```

### *args va **kwargs
- Agar funksiya turli xil sonli argumentlarni qabul qilishi kerak bo'lsa, `*args `va `**kwargs` dan foydalanamiz.

- *args argumentlar
    - `*args` funksiya ichida tuple(to'plam) shaklida beriladi va turli pozitsion argumentlarni qabul qiladi.
```python
def summa(*args):
    return sum(args)
# *args bilan foydalanish
print(summa(1, 2, 3, 4))  # Natija: 10
```
- **kwargs argumentlar
    - **kwargs funksiya ichida dictionary (lug'at) shaklida beriladi va kalit so'zli argumentlarni qabul qiladi.
```python
def malumot_korsat(**kwargs):
    for kalit, qiymat in kwargs.items():
        print(f"{kalit}: {qiymat}")

# **kwargs bilan foydalanish
malumot_korsat(ism="Ali", yosh=25, shahar="Toshkent")
# Natija:
# ism: Ali
# yosh: 25
# shahar: Toshkent
```
### Lambda FUNCTION
> [!NOTE] 
> Lambda funksiyalari qisqa funksiyalar bo'lib, ularni bir qator kod bilan yozish mumkin.
- Lambda funksiyasini yaratish uchun lambda kalit so'zidan foydalanamiz, va u quyidagi tuzilishga ega:
```python
lambda argumentlar: ifoda
```
- Bu yerda
    - **lambda** - `lambda` funksiyasini yaratish uchun kalit so'z.
    - **argumentlar** - funksiyaga kiruvchi qiymatlar (`parametrlar`).
    - **ifoda** - funksiyaning qaytaradigan natijasi (ko'pincha bitta ifoda bo'ladi).
- Keling, ikkita sonni qo'shadigan oddiy `lambda` funksiyasini yarataylik:
```python
yigindi = lambda x, y: x + y
natija = yigindi(5, 3)
print(natija)  # Natija: 8
```
Bu yerda `lambda x, y: x + y` funksiyasi ikki argumentni qabul qiladi (`x` va `y`) va ularni qo'shib, natijani qaytaradi. Funksiya `yigindi` nomi bilan saqlanadi va keyin chaqiriladi.

`Lambda` funksiyalari va `def` bilan yaratilgan funksiyalar o'rtasidagi farq
- `Lambda` funksiyalari va `def` yordamida yaratilgan funksiyalar o'rtasidagi asosiy farq shundaki, `lambda` funksiyalari juda qisqa va faqat bitta ifodani bajaradi, `def` esa ko'proq qatorli kodlarni o'z ichiga olishi mumkin.

`def` bilan funksiya yaratish
```python
def yigindini_xosobla(x, y):
    return x + y

natija = yigindini_xosobla(5, 3)
print(natija)  # Natija: 8
```
> [!NOTE]
> `Lambda` funksiyalari ko'pincha oddiy hisob-kitoblar yoki anonim funksiyalar kerak bo'lgan joylarda ishlatiladi, masalan, `map`, `filter`, va `sorted` kabi funksiyalarda.

### `lambda` FUNKSIYASIDAN FOYDALANISH
1. `map()` funksiyasi bilan lambda
- `map()` funksiyasi berilgan funksiyani har bir elementga qo'llaydi va yangi ro'yxat qaytaradi.
```python
sonlar = [1, 2, 3, 4]
kvadratlar = list(map(lambda x: x ** 2, sonlar))
print(kvadratlar)  # Natija: [1, 4, 9, 16]
```
Yuqorida `lambda x: x ** 2` har bir elementni kvadratga ko'paytiradi.
2. `filter()` funksiyasi bilan **lambda**
- `filter()` funksiyasi berilgan shart bo'yicha elementlarni saralaydi.
```python
sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
print(juft_sonlar)  # Natija: [2, 4, 6, 8]
```
Yuqorida `lambda x: x % 2 == 0` juft sonlarni tanlaydi.
3. `sorted()` funksiyasi bilan **lambda**
- `sorted()` funksiyasi ro'yxatni tartiblaydi va `lambda` yordamida tartiblash qoidalarini belgilash mumkin.
```python
mevalar = ["olma", "banan", "apelsin", "anor"]
tartiblangan = sorted(mevalar, key=lambda x: len(x))
print(tartiblangan)  # Natija: ['olma', 'anor', 'banan', 'apelsin']
```
Bu yerda `lambda x: len(x)` uzunligi bo'yicha mevalarni tartiblaydi.
### ICHMA-ICH lambda FUNKSIYALAR
- `Lambda` funksiyalarni boshqa funksiyalarga ichida ishlatish mumkin, bu esa kodni qisqartirish va tezkor ishlatish imkonini beradi.
```python
def tashqi_funksiya(karrali):
    return lambda x: x * karrali

ikki_barak = tashqi_funksiya(2)
uch_barak = tashqi_funksiya(3)

print(ikki_barak(5))  # Natija: 10
print(uch_barak(5))  # Natija: 15
```
Yuqorida `tashqi_funksiya` funksiya ichida `lambda` funksiyani qaytaradi va bu `lambda` funksiyasi karrali sonni hisoblaydi.

### FUNKSIYA ICHIDA FUNKSIYA YARATISH
- Pythonda funksiya ichida boshqa bir funksiyani yaratish imkoniyati mavjud. Bu imkoniyatni `ichki funksiyalar` deb ataladi. Ichki funksiyalar biror bir funksiyaning ichida aniqlanadi va odatda shu tashqi funksiyaga xos bo'lgan operatsiyalarni bajarish uchun ishlatiladi.
```python
def tashqi_funksiya(x):
    def ichki_funksiya(y):
        return y ** 2
    return ichki_funksiya(x) + 5

natija = tashqi_funksiya(3)
print(natija)  # Natija: 14
```
Yuqorida `ichki_funksiya(y)` funksiya tashqi funksiyaning ichida aniqlangan va u sonning kvadratini hisoblaydi. `tashqi_funksiya(x)` funksiyasi esa `ichki_funksiya(x)` chaqirib, natijaga 5 qo'shadi va umumiy natijani qaytaradi.

- Ichki funksiyalarning qo'llanilishi:
    - **Kapsulatsiya:** Tashqi funksiyaga xos bo'lgan kodni izolyatsiya qilish uchun. Ichki funksiya faqat tashqi funksiyaning ichida mavjud bo'lib, uni tashqi funksiyadan tashqarida chaqirib bo'lmaydi.
    - **Kod takrorlanishini kamaytirish:** Ko'p martalik ishlatiladigan kod qismlarini ichki funksiya ichida yozish.
    - **Murakkab funksional tuzilmalarni yaratish:** Funksiya ichidagi funksiya orqali murakkab hisob-kitoblarni bajarish.
## AMALIYOT
- Oddiy matematik funksiya:
    - Funksiya yarating, u ikkita sonni qabul qilib, ularni ko'paytirib qaytarsin. Agar foydalanuvchi son bermasa, ikkala son uchun standart qiymat 1 bo'lsin. <br>
    **Natija:**
    ```python
    print(kopaytirish(5, 3))  # Natija: 15
    print(kopaytirish())      # Natija: 1
    ```
- Salomlash funksiyasi:
    - Funksiya yarating, u ismni qabul qilsin va foydalanuvchiga `Salom, [ism]!` deb salomlashsin. Agar ism berilmasa, `Salom, Do'stim!` deb salomlashsin. <br>
    **Natija:**
    ```python
    print(salomlash("Ali"))  # Natija: Salom, Ali!
    print(salomlash())       # Natija: Salom, Do'stim!
    ```
- Sonlarning kvadratlari:
    - Funksiya yarating, u bir ro'yxat qabul qilib, har bir elementning kvadratini qaytarsin. Ro'yxatni `map()` va lambda funksiyasi yordamida qayta ishlang. <br>
    **Natija:**
    ```python
    print(kvadratlar([1, 2, 3, 4]))  # Natija: [1, 4, 9, 16]
    ```
- Juft sonlarni filtrlang:
    - Funksiya yarating, u ro'yxatdan faqat juft sonlarni ajratib qaytarsin. `filter()` va lambda funksiyasidan foydalaning. <br>
    **Natija:**
    ```python
    print(juft_sonlar([1, 2, 3, 4, 5, 6]))  # Natija: [2, 4, 6]
    ```
- Student ma'lumotlarini qaytaruvchi funksiya:
    - Funksiya yarating, u talabaning `ismi`, `yoshi`, va `kursini` qabul qilib, bu ma'lumotlarni tartiblangan ko'rinishda qaytarsin. `**kwargs` dan foydalaning. <br>
    **Natija:**
    ```python
    talaba_ma'lumotlari(ism="Ali", yosh=21, kurs="Python")
    # Natija:
    # ism: Ali
    # yosh: 21
    # kurs: Python
    ```