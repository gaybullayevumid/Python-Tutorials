# PYTHON DASTURLASH ASOSLARI

## 7-dars For loop(tsikl)

Python dasturlash tilida `for` tsikli muhim komponent hisoblanadi va ko'p hollarda **iteratsiya** (`takrorlash`) vazifalarini bajarish uchun ishlatiladi.

### FOR LOOP SINTAKSISI
- Pythonda `for` tsiklining umumiy sintaksisi quyidagicha:
```python
for element in iterable:
    # tsikl tanasi
```

- Bu yerda:
    - `element` — bu takrorlanadigan har bir element.
    - `iterable` — bu takrorlash mumkin bo'lgan obyekt (**masalan**, `ro'yxat`, `tuple`, `set`, string`, `dictionary`, va hokazo).
    - `tsikl tanasi` — har bir takrorlashda bajariladigan kod bloki.

### LISTLAR BILAN ISHLASH
- Ro'yxatlar eng keng tarqalgan takrorlanadigan obyektlardan biri hisoblanadi.
```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```
- Bu misolda `for` tsikli `numbers` ro'yxatidagi har bir elementni `takrorlab`, ularni ekranga chiqaradi.

```python
# Mevalar ro'yxati
fruits = ["olma", "banan", "gilos"]

# Ro'yxat bo'yicha tsikl
for fruit in fruits:
    print(fruit)
```
- Tushuntirish:
    - `fruits` uchta matndan(string) dan iborat ro'yxat.
    - `for fruit in fruits`: bu kod qatorida `fruit` o'zgaruvchisi ro'yxatdagi har bir elementni o'z ichiga oladi.
    - `print(fruit)` esa har bir elementni ekranga chiqaradi.

```python
# Misol ro'yxat
numbers = [1, 2, 3, 4, 5]

# Har bir sonning kvadratini hisoblash uchun tsikl
for number in numbers:
    square = number ** 2
    print(f"{number} ning kvadrati {square}")
```
- Tushuntirish:
    - `numbers` raqamlardan iborat ro'yhat.
    - `for number in numbers`: bu kod qatorida `number` o'zgaruvchisi ro'yxatdagi har bir elementni o'z ichiga oladi.
    - `square = number ** 2`: square o'zgaruvchisiga ro'yhatimiz ichidagi har bir raqamning kvadratini saqladik.
    - print() funksiyasi orqali sonlar kvadratini terminalga chiqardik.

- Ro'yxatdagi elementlarni yig'indisini hisoblash:
```python
# Misol ro'yxat
numbers = [10, 20, 30, 40, 50]

# Yig'indini hisoblash uchun o'zgaruvchi
total = 0

# For tsikli bilan ro'yxat bo'ylab yurish
for number in numbers:
    total += number

print(f"Yig'indi: {total}")
```

- Ro'yxatdagi elementlarni filtrlash.
    - Ro'yxatdan faqat juft sonlarni tanlab olish:
```python
# Misol ro'yxat
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Juft sonlarni saqlash uchun yangi ro'yxat
even_numbers = []

# For tsikli bilan ro'yxat bo'ylab yurish
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(f"Juft sonlar: {even_numbers}")
```

- Ro'yxatdagi matnlarni(string) katta harfga o'zgartirish:
```python
# Misol ro'yxat
fruits = ["olma", "banan", "gilos"]

# For tsikli bilan ro'yxat bo'ylab yurish
for i in range(len(fruits)):
    fruits[i] = fruits[i].upper()

print(f"Katta harfdagi mevalar: {fruits}")
```
### `range()` FUNKSIYASI BILAN TAKRORLASH
- `range()` funksiyasi takrorlash uchun sonlar oralig'ini yaratadi. Bu sonlar qatori ustidan `for` tsikli yordamida aylanib chiqish mumkin.

```python
for i in range(5):
    print(i)
```
Bu yerda `range(5)` qatori `0` dan `4` gacha bo'lgan raqamlarni o'z ichiga oladi.

- Juft sonlarni hisoblash
```python
for index in range(0, 11, 2):
    print(index)
```

### DICTIONARY BILAN ISHLASH
- Lug'atlar `kalit-qiymat` juftlaridan iborat bo'ladi. `for` tsikli yordamida lug'atlarni takrorkashda, kalitlar orqali aylanib chiqish mumkin.
```python
person = {
    "name": "John", 
    "age": 30, "city": 
    "New York"
    }

for key in person:
    print(key, ":", person[key])
```
- Faqat kalitlar ustida ishlash:
```python
person = {
    'name':'Umid',
    'age':20,
    'job':'teacher'
}

for keys in person:
    print(keys)
```
- Qiymatlar ustida ishlash:
```python
person = {
    'name':'Umid',
    'age':20,
    'job':'teacher'
}

for qiymat in person.values():
    print(qiymat)
```

- Kalitlar va qiymatlar ustida ishlash.
    - Agar siz kalitlar bilan birga qiymatlarni ham olishni istasangiz, `.items()` metodidan foydalanishingiz mumkin:
```python
person = {
    'name':'Umid',
    'age':20,
    'job':'teacher'
}
for kalit, qiymat in person.items():
    print(f"{kalit}: {qiymat}")
```

### SETS BILAN ISHLASH
To'plamlar ham takrorlanadigan obyekt bo'lib, ularda tartiblanmagan elementlar mavjud.
```python
numbers = {1, 2, 3, 4, 5}

for num in numbers:
    print(num)
```

```python
mevalar = {"olma", "banan", "uzum"}

for meva in mevalar:
    print(meva)
```
### TUPLE BILAN ISHLASH
- Tuplelar ham ro'yxatlarga o'xshash, lekin o'zgarmas tuzilma bo'lib, ularning elementlari ustidan tsikl ishlatish mumkin.
```python
coordinates = (10, 20, 30)

for coordinate in coordinates:
    print(coordinate)
```

### ICHMA-ICH(NESTED) `for` TSIKLLAR
- Bir `for` tsikli ichida boshqa bir `for` tsiklining ishlatilishi mumkin. Buni **ichma-ich**(`nested`) tsikllar deb atashadi.
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Qator oxirida yangi qatorga o'tish
```
- `end=''` operatori qator tugaganida nimalarni chiqarish kerakligini belgilaydi. Odatda, `print()` funksiyasida qator tugagach yangi qatorga o‘tish (`\n`) avtomatik ravishda amalga oshadi, lekin `end=''` operatori yordamida buning o‘rniga boshqa belgini qo‘yish mumkin.

### `else` BILAN `for` TSIKLI
- Pythonda `for` tsiklining oxirida `else` bloki ishlatilishi mumkin. Agar `for` tsikli to'liq tugasa (hech qanday break holatidan to'xtatilmasa), `else` bloki ishlaydi.

```python
for i in range(5):
    print(i)
else:
    print("Tsikl tugadi")
```

### `break` OPERATORI
- `break` operatori siklni to'xtatadi. Bu operator `for` yoki `while` siklida ishlatilishi mumkin. `break` siklning bajarilishini to'xtatadi va sikldan chiqadi, hatto sikl to'liq tugamagan bo'lsa ham.
```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        break  # Agar son 3 ga teng bo'lsa, loop to'xtaydi
    print(number)
```
- `break` Operatorining Foydalari
    - **Shart Bajarilganda To'xtatish:** Siz siklni ma'lum bir shart bajarilganda to'xtatishingiz mumkin. Bu, masalan, kerakli ma'lumot topilganida yoki xato yuzaga kelganida foydalidir.
    - **Resurslarni Tejash:** Agar sikl uzun bo'lsa va siz biror bir shart bajarilganda ishni to'xtatmoqchi bo'lsangiz, break orqali resurslarni tejashingiz mumkin.
    - **Tashqi Aylanishlarga Osonlik:** `break` siklni to'xtatishi mumkin bo'lgan eng yaqin blok (ya'ni, `for` yoki `while` sikli) ichida ishlaydi.
- Faqat Birinchi To'g'ri Elementni Qidirish:
```python
mevalar = ['olma', 'banan', 'apelsin', 'anjir']

for meva in mevalar:
    if meva == 'apelsin':
        print('Apelsin topildi!')
        break
```
- Noma'lum Hajmdagi Ma'lumotlarni Qidirish:
```python
sonlar = [7, 10, 2, 6, 11]

for son in sonlar:
    if son % 2 == 0:
        print(f'Juft son topildi: {son}')
        break
```
Yuqoridagi kodda ro'yhat ichidan juft son bor yoqligini tekshirdik va juft son topilgandan keyin kod `break` orqali toxtatdik.
### `continue` OPERATORI
> [!NOTE] 
> `continue` operatori **for loop** ichida ishlatiladi va u **for loop**ning takrorlanishini to'xtatib, keyingi takrorlashga o'tadi. Ya'ni, `continue` operatori **for loop** ichidagi qolgan kodni bajarishdan voz kechib, **for loop**ning keyingi takrorlanishga o'tishni ta'minlaydi.
- `continue` operatoridan foydalanish:
    - Agar **for loop** ichida muayyan shart bajarilganda qolgan kodlarni bajarish kerak bo'lmasa, `continue` operatoridan foydalaniladi.
```python
sonlar = [1, 2, 3, 4, 5]

for son in sonlar:
    if son % 2 == 0:
        continue
    print(son)
```
- `continue` operatorining foydalari
    - **Shart Bajarilganda Kodni O'tkazib Yuborish:** Agar siz **for loop**ning qolgan qismidagi kodni o'tkazib yuborishni xohlasangiz, `continue` operatori juda foydali bo'lishi mumkin.
    - **Tajriba Va Shartlarga Ko'ra Kodni Soddalashtirish:** `continue` operatori yordamida siz ko'proq shartni tekshirishni oldini olishingiz mumkin, bu esa kodingizni soddalashtiradi va o'qilishini yaxshilaydi.
    - **For loopni Boshqarish:** `continue` operatori **for loop**ni boshqarishga yordam beradi, masalan, ba'zi holatlarda faqat muayyan shart bajarilganida kod bajarilishi kerak bo'lganda.

- Faqat musbat sonlarni chiqarish:
```python
sonlar = [-1, 2, -3, 4, -5]

for son in sonlar:
    if son < 0:
        continue
    print(son)
```
Yuqoridagi misolda, manfiy sonlar o'tkazib yuboriladi va faqat musbat sonlar ekranga chiqariladi.

- Faqat juft indexdagi elementlar bilan ishalash:
```python
mevalar = ['olma', 'banan', 'apelsin', 'anjir']

for i in range(len(mevalar)):
    if i % 2 != 0:
        continue
    print(mevalar[i])
```
Yuqoridagi misolda, faqat juft indekslardagi elementlar ekranga chiqariladi.

- `continue` operatorining kamchiliklari
    - **Kodni o'qish murakkablashishi mumkin:** Ba'zi hollarda, `continue` operatoridan haddan tashqari foydalanish kodingizni murakkablashtirishi mumkin, chunki har bir iteratsiyadagi kodning bajarilishini tushunish qiyinlashadi.
    - **Tuzilishi noqulay bo'lishi mumkin:** Agar **for loop**da juda ko'p shartlar bo'lsa va ular har xil `continue` operatorlariga bog'liq bo'lsa, bu kodni murakkab va noqulay tuzishga olib kelishi mumkin.

### pass OPERATORI
> [!NOTE]
> `pass` operatori Pythonda `hech narsa qilmaslik` uchun ishlatiladi. U bo'sh joyni saqlash uchun mo'ljallangan bo'lib, u qachonlardir qo'shilishi mumkin bo'lgan kod uchun o'rinbosar bo'lib xizmat qiladi. `pass` operatori kodning sintaksisi to'g'ri bo'lishi uchun ishlatiladi, lekin u hech qanday amaliyot bajarmaydi.

- `pass` operatoridan foydalanish
    - Agar siz kod yozayotganda hali bajarilishi kerak bo'lgan blokni to'liq qilmagan bo'lsangiz yoki shunchaki vaqtincha bo'sh qoldirmoqchi bo'lsangiz, `pass` operatoridan foydalanishingiz mumkin. Bu kodning ishlashiga to'sqinlik qilmaydi va boshqa qismdagi kodlarni sinab ko'rishga imkon beradi.
```python
for son in range(5):
    if son == 3:
        pass
    else:
        print(son)
```
Tushuntirish:
- Ushbu misolda, son `3` ga teng bo'lganda hech narsa qilinmaydi, lekin **for loop**ni davom ettiriladi. `3` raqamiga yetilganda `pass` operatori ishlatiladi va bu hech qanday natija bermaydi. Shuning uchun faqat `3` dan boshqa sonlar chop etiladi.

- `pass` operatorining foydalari:
    - **Kod Tuzilishini Saqlash:** `pass` operatori kod tuzilishini saqlab qoladi va keyinchalik ushbu qismga kod qo'shilishini kutib turadi.
    - **Vaqtinchalik Yechim:** `pass` dasturda vaqtincha yechim sifatida ishlatiladi, ya'ni siz hali bajarilishi kerak bo'lgan qismni aniqlab olmaganingizda.
    - **Sintaksis Xatolarni Oldini Olish:** Agar siz `if`, `for`, `while`, yoki funksiyalar kabi bloklarni yaratgan bo'lsangiz, lekin ularni hali to'ldirmagan bo'lsangiz, `pass` operatori yordamida sintaksis xatolarini oldini olishingiz mumkin.
Misollar:
- Bo'sh funksiyani yaratish:
```python
def empty_func():
    pass
```
Yuqoridagi misolda, `empty_func` nomli funksiyani yaratdik, lekin u hech narsa qilmaydi. Keyinchalik ushbu funktsiya ichiga kod yozishingiz mumkin.

- Bo'sh class yaratish:
```python
class EmptyClass:
    pass
```
Yuqoridagi misolda, `EmptyClass` nomli **class** yaratildi, lekin uning ichida hech qanday metod yoki atribut yo'q. `pass` operatori **class**ni to'ldirish uchun bo'sh joy saqlashga imkon beradi.
- Shartli bo'sh blok:
```python
for son in range(10):
    if son % 2 == 0:
        pass  # Juft sonlar uchun hech narsa qilmaymiz
    else:
        print(son)
```
Yuqoridagi misolda, juft sonlar uchun hech narsa qilinmaydi, faqat toq sonlar chop etiladi.

- `pass` operatorining kamchiliklari
    - **Boshqaruv tuzilmasi mumkin:** Agar siz `pass` operatoridan foydalanishni unutib qo'ysangiz, kodda muhim qismi bo'sh qolishi mumkin, bu esa keyinchalik dasturda muammolar keltirib chiqarishi mumkin.
    - **Kamdan-kam foydalaniladi:** `pass` operatori kodni tayyorlash va sinovdan o'tkazish jarayonida foydali, lekin final versiyasida odatda kamdan-kam ishlatiladi.

## AMALIYOT
- Elementlarni chiqarish:
    - `for` loop yordamida ro‘yxatdagi barcha elementlarni ekranga chiqaruvchi kod yozing.
    ```python
    mevalar = ["olma", "banan", "shaftoli"]
    ```
- Sonlar yig‘indisi:
    - `for` loop yordamida `1` dan `10` gacha bo‘lgan sonlarning yig‘indisini toping.
- Harflarni hisoblash:
    - Bir matn berilgan. for loop yordamida matndagi nechta unli harf borligini hisoblang. Unli harflar: `a, e, i, o, u`.
- Sonlarni ko‘paytirish:
    - Ro‘yxatdagi sonlarni `2` ga ko‘paytiring va yangi ro‘yxat hosil qiling.
    ```python
    sonlar = [2, 4, 6, 8]


    # [4, 8, 12, 16]
    ```
- Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing.
- Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing).
- 10 dan 100 gacha bo'lgan juft sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kvadratini yangi qatordan konsolga chiqaring.
- Ma'lum bir elementni qidirish:
    - Quyidagi misolda, ro'yxatdagi kerakli elementni topib, uni topgan zahoti **for loop**ni to'xtatamiz.
```python
mevalar = ['olma', 'banan', 'apelsin', 'anjir']
```
Bu misolda, **for loop**i `mevalar` ro'yxatidagi elementlarni ketma-ket tekshiradi. `apelsin` topilganidan so'ng, `break` operatori siklni to'xtatadi.
- Juft sonni qidirish
    - Quyidagi misolda, ro'yxatdagi birinchi juft sonni topganimizda **for loop**ni to'xtatamiz.
```python
sonlar = [1, 3, 5, 6, 7, 9]
```
Bu misolda, **for loop**i `sonlar` ro'yxatidagi elementlarni tekshiradi. `6` raqami birinchi juft son bo'lganligi uchun, `break` operatori siklni to'xtatadi.
- O'quvchilar ro'yxatidan ma'lum bir ismni qidirish
    - Quyidagi misolda, o'quvchilar ro'yxatidan ma'lum bir ismni topganimizda **for loop**ni to'xtatamiz.
```python
oquvchilar = ['Ali', 'Vali', 'Olim', 'Jasur']
```
Bu misolda, **for loop**i `oquvchilar` ro'yxatidagi ismlar ustida aylanadi. `Olim` ismi topilganida, `break` operatori **for loop**ini to'xtatadi.
- 10 dan katta bo'lgan birinchi sonni topish
    - Quyidagi misolda, ro'yxatdagi `10` dan katta bo'lgan birinchi sonni topganimizda **for loop**ni to'xtatamiz.
```python
sonlar = [2, 4, 10, 15, 8]
```
Bu misolda, **for loop**i `sonlar` ro'yxatidagi sonlarni ketma-ket tekshiradi. `15` raqami `10` dan katta bo'lgan birinchi son bo'lib, `break` operatori **for loop**ni to'xtatadi.
- Toq sonlarni chiqarish:
    - Quyidagi misolda, ro'yxatdagi faqat **toq** sonlarni ekranga chiqaramiz. **Juft** sonlarga kelganda, `continue` operatori ishlaydi va ularni o'tkazib yuboradi.
```python
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
Bu misolda, **for loop**i sonlar ro'yxatidagi barcha sonlarni tekshiradi. Agar son juft bo'lsa, `continue` operatori ishlaydi va **for loop**ning qolgan qismi o'tkazilib, keyingi takrorlashga o'tiladi. Natijada faqat toq sonlar chop etiladi.
- Ma'lum bir harfni o'tkazib yuborish:
    - Quyidagi misolda, string ichidagi ma'lum bir harfni (masalan, `a` harfini) ekranga chiqarmasdan o'tkazib yuboramiz.
```python
matn = "salom dunyo"
```
Yuqoridagi misolda, **for loop**i matndagi barcha harflarni tekshiradi. Agar harf `a` ga teng bo'lsa, `continue` operatori ishlaydi va u harfni chiqarishdan o'tkazib yuboradi. Natijada `a` harfi chiqmaydi.

- Manfiy sonlarni o'tkazib yuborish
    - Quyidagi misolda, ro'yxatdagi manfiy sonlarni ekranga chiqarishni o'tkazib yuboramiz va faqat musbat sonlarni chop etamiz.
```python
sonlar = [-5, 3, -1, 7, -8, 10]
```
Yuqoridagi misolda, **for loop**i sonlar ro'yxatidagi barcha sonlarni tekshiradi. Agar son **manfiy** bo'lsa, `continue` operatori ishlaydi va u sonni ekranga chiqarmasdan o'tkazib yuboradi. Natijada faqat **musbat** sonlar chiqariladi.
