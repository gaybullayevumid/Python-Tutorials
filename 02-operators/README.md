# PYTHON DASTURLASH ASOSLARI

## 2-dars Oddiy matematik va mantiqiy amallar.

- Python operatorlarini quyidagi guruhlarga bo'lish mumkin:
    - Arifmetik operatorlar
    - Taqqoslash operatorlari
    - Mantiqiy operatorlar
    - Bitwise (Bitli) operatorlar
    - Tayinlash (Assign) operatorlari
    - A'zolik (Membership) operatorlari
    - Identifikatsiya (Identity) operatorlari
    - Aralashtirilgan operatorlar (Mixed Operators)

## ARIFMETIK OPERATORLAR

Python dasturlash tilida arifmetik operatorlar matematik amallarni bajarish uchun ishlatiladi.

1. **Qo'shish** (`+`): Ikkita sonni qo'shish uchun ishlatiladi.

```python
a = 5
b = 3
c = a + b  # c 8 ga teng bo'ladi
print(c)
```

2. **Ayirish** (`-`): Ikkita sonni ayirish uchun ishlatiladi.
```python
a = 5
b = 3
c = a - b  # c 2 ga teng bo'ladi
print(c)
```

3. **Ko'paytirish** (`*`): Ikkita sonni ko'paytirish uchun ishlatiladi.
```python
a = 5
b = 3
c = a * b  # c 15 ga teng bo'ladi
print(c)
```

4. **Bo'lish** (`/`): Ikkita sonni bo'lish uchun ishlatiladi.

```python
a = 6
b = 3
c = a / b  # c 2.0 ga teng bo'ladi
print(c)
```

5. **Butun bo'lish** (`//`): Ikkita sonni butun qismiga bo'lish uchun ishlatiladi.

```python
a = 7
b = 3
c = a // b  # c 2 ga teng bo'ladi
print(c)
```

6. **Qoldiq** (`%`): Ikkita sonni bo'lgandan keyin qoldiqni topish uchun ishlatiladi.

```python
a = 7
b = 3
c = a % b  # c 1 ga teng bo'ladi
print(c)
```

7. **Daraja** (`**`): Bir sonni ikkinchi son darajasiga ko'tarish uchun ishlatiladi.

```python
a = 2
b = 3
c = a ** b  # c 8 ga teng bo'ladi
print(c)
```

## TAQQOSLASH OPERATORLARI

Python dasturlash tilida `solishtirish` operatorlari ikki qiymatni `taqqoslash` uchun ishlatiladi.

1. **Teng** (`==`): Ikkita qiymat tengligini tekshiradi.

```python
a = 5
b = 3
result = (a == b)  # result False ga teng bo'ladi
print(result)
```

2. **Teng emas** (`!=`): Ikkita qiymat teng emasligini tekshiradi.

```python
a = 5
b = 3
result = (a != b)  # result True ga teng bo'ladi
print(result)
```

3. **Katta** (`>`): Chap tomondagi qiymat o'ng tomondagi qiymatdan katta ekanligini tekshiradi.

```python
a = 5
b = 3
result = (a > b)  # result True ga teng bo'ladi
print(result)
```

4. **Kichik** (`<`): Chap tomondagi qiymat o'ng tomondagi qiymatdan kichik ekanligini tekshiradi.

```python
a = 5
b = 3
result = (a < b)  # result False ga teng bo'ladi
print(result)
```

5. **Katta yoki teng** (`>=`): Chap tomondagi qiymat o'ng tomondagi qiymatdan katta yoki teng ekanligini tekshiradi.

```python
a = 5
b = 3
result = (a >= b)  # result True ga teng bo'ladi
print(result)
```

6. **Kichik yoki teng** (`<=`): Chap tomondagi qiymat o'ng tomondagi qiymatdan kichik yoki teng ekanligini tekshiradi.

```python
a = 5
b = 3
result = (a <= b)  # result False ga teng bo'ladi
print(result)
```

## MANTIQIY OPERATORLAR

Python dasturlash tilida mantiqiy operatorlar mantiqiy qiymatlarni (`True` yoki `False`) birlashtirish yoki taqqoslash uchun ishlatiladi.

1. **va** (`and`): Ikkala shart ham `True` bo'lsa, natija `True` bo'ladi, aks holda `False`.

```python
a = True
b = False
result = a and b  # result False ga teng bo'ladi
print(result)
```

2. **yoki** (`or`): Hech bo'lmaganda bitta shart `True` bo'lsa, natija `True` bo'ladi, aks holda `False`.

```python
a = True
b = False
result = a or b  # result True ga teng bo'ladi
print(result)
```

3. **emas** (`not`): Shartning mantiqiy qiymatini teskariga o'zgartiradi (`True` bo'lsa `False`ga, `False` bo'lsa `True`ga).

```python
a = True
result = not a  # result False ga teng bo'ladi
print(result)
```

Quyidagi misolda mantiqiy operatorlar qanday ishlashini ko'rishimiz mumkin:

```python
x = 5
y = 10
z = 5

# and operatori
result = (x == z) and (y > x)  # result True ga teng bo'ladi, chunki ikkala shart ham True

# or operatori
result = (x == z) or (y < x)  # result True ga teng bo'ladi, chunki birinchi shart True

# not operatori
result = not (x == z)  # result False ga teng bo'ladi, chunki x va z teng
```
## BITWISE(BITLI) OPERATORLAR
Python tilida **bitwise** (`bitli`) operatorlar sonlarning bitlari ustida to'g'ridan-to'g'ri amallarni bajaradi. Bu operatorlar ikkita sonning **binary** (`ikkilik`) shakldagi bitlari bilan ishlaydi.
1. **AND**(`&`)<br>
- Bu operator ikkala sonning mos bitlarini `AND` amali bilan solishtiradi. Ikkala bit ham `1` bo'lsa, natija `1`, aks holda `0`.
```python
a = 5  # 0101
b = 3  # 0011
natija = a & b  # 0001 (1)
print(natija)
```
2. **OR**(`|`)<br>
- Bu operator ikkala sonning mos bitlarini `OR` amali bilan solishtiradi. Kamida bitta bit `1` bo'lsa, natija `1`, aks holda `0`.
```python
a = 5  # 0101
b = 3  # 0011
natija = a | b  # 0111 (7)
print(natija)
```
3. **XOR**(`^`)<br>
- Bu operator ikkala sonning mos bitlarini `XOR` amali bilan solishtiradi. Agar bitta bit `1`, ikkinchisi `0` bo'lsa, natija `1`, aks holda `0`.
```python
a = 5  # 0101
b = 3  # 0011
natija = a ^ b  # 0110 (6)
print(natija)
```
4. **NOT**(`~`)<br>
- Bu operator bitlarning qarama-qarshi qiymatini qaytaradi. `0` ni `1` ga, `1` ni `0` ga o'zgartiradi. Python tilida `~x = -x-1` deb qabul qilinadi.
```python
a = 5  # 0101
natija = ~a  # -(0101 + 1) = -0110 (-6)
print(natija)
```
5. **Chapga siljitish**(`<<`)<br>
- Bu operator bitlarni chapga siljitadi va o'ng tomonga `0` qo'shadi. Har bir siljitish operatsiyasi bitlarning qiymatini `2` ga ko'paytiradi.
```python
a = 5  # 0101
natija = a << 1  # 1010 (10)
print(natija)
```
6. **O'ngga siljitish**(`>>`) <br>
- Bu operator bitlarni o'ngga siljitadi va chap tomonga `0` yoki sonning ishorasi (`positive`/`negative sign`) qo'yiladi. Har bir siljitish operatsiyasi bitlarning qiymatini `2` ga kamaytiradi.
```python
a = 5  # 0101
natija = a >> 1  # 0010 (2)
print(natija)
```
7. Qo'shimcha misollar <br>
- `AND`, `OR`, `XOR` **operatorlari bilan:**
```python
a = 12  # 1100
b = 6   # 0110

natija_and = a & b  # 0100 (4)
natija_or = a | b   # 1110 (14)
natija_xor = a ^ b  # 1010 (10)

print(natija_and)
print(natija_or)
print(natija_xor)
```
8. `NOT`, **chapga va o'ngga siljitish bilan:**
```python
x = 7  # 0111

natija_not = ~x     # -1000 (-8)
chapga = x << 2     # 11100 (28)
ongga = x >> 2     # 0001 (1)

print(natija_not)
print(chapga)
print(ongga)
```

## TAYINLASH(ASSIGN) OPERATORALRI
Pythonda **tayinlash**(`assign`) operatorlari yordamida o'zgaruvchilarga qiymatlar tayinlanadi. Bu operatorlar nafaqat qiymatlarni o'zgaruvchilarga tayinlash, balki matematik amallarni bajarib, natijani ham o'zgaruvchiga saqlash imkonini beradi. Quyida tayinlash operatorlarining to'liq ro'yxati va ulardan foydalanish misollari keltirilgan:

1. `=` - **Oddiy tayinlash operatori**
    - Bu operator oddiy qiymat tayinlash uchun ishlatiladi.
```python
x = 10
y = 5
```
Yuqoridagi misolda `x` o'zgaruvchisiga `10`, `y` o'zgaruvchisiga esa `5` qiymati tayinlanadi.

2. `+=` - **Qo'shish va tayinlash**
    - Bu operator yordamida o'zgaruvchi qiymatini berilgan qiymatga qo'shib, natijani o'zgaruvchiga qayta tayinlash mumkin.
```python
x = 10
x += 5  # x endi 15 ga teng bo'ladi
```

3. `-=` - **Ayirish va tayinlash**
- Bu operator yordamida o'zgaruvchi qiymatini berilgan qiymatdan ayirib, natijani o'zgaruvchiga qayta tayinlash mumkin.
```python
x = 10
x -= 3  # x endi 7 ga teng bo'ladi
```

4. `*=` - **Ko'paytirish va tayinlash**
- Bu operator yordamida o'zgaruvchi qiymatini berilgan qiymatga ko'paytirib, natijani o'zgaruvchiga qayta tayinlash mumkin.
```python
x = 4
x *= 2  # x endi 8 ga teng bo'ladi
```
5. `/=` - **Bo'lish va tayinlash**
- Bu operator yordamida o'zgaruvchi qiymatini berilgan qiymatga bo'lib, natijani o'zgaruvchiga qayta tayinlash mumkin.
```python
x = 20
x /= 4  # x endi 5.0 ga teng bo'ladi (natija float turida bo'ladi)
```
6. `%=` - **Qoldiqni tayinlash**
- Bu operator yordamida o'zgaruvchi qiymatini berilgan qiymatga bo'lgandan keyin qoldiqni o'zgaruvchiga qayta tayinlash mumkin.
```python
x = 10
x %= 3  # x endi 1 ga teng bo'ladi (qoldiq)
```
7. `**=` - **Daraja va tayinlash**
- Bu operator yordamida o'zgaruvchi qiymatini berilgan darajaga oshirib, natijani o'zgaruvchiga qayta tayinlash mumkin.
```python
x = 3
x **= 2  # x endi 9 ga teng bo'ladi (3^2 = 9)
```
8. `//=` - **Butun bo'lish va tayinlash**
- Bu operator yordamida o'zgaruvchi qiymatini berilgan qiymatga butun bo'lib, natijani o'zgaruvchiga qayta tayinlash mumkin.
```python
x = 10
x //= 3  # x endi 3 ga teng bo'ladi (butun qismini oladi)
```
## A'ZOLIK(MEMBERSHIP) OPERATORLARI
- Pythonda a'zolik (membership) operatorlari ma'lum bir elementning **ketma-ketlik**(`sequence`), masalan, **ro'yxat**(`list`), **qator**(`string`) yoki **to'plam**(`set`) ichida mavjudligini tekshirish uchun ishlatiladi. 
1. `in` **operatori**
- Bu operator yordamida elementning ma'lum bir ketma-ketlikda mavjudligini tekshirish mumkin.
```python
mevalar = ['olma', 'banan', 'nok']
if 'olma' in mevalar:
    print("Olma ro'yxatda mavjud.")
```
**Natija:** `Olma ro'yxatda mavjud.` <br>
Bu yerda `olma in mevalar ifodasi` True qiymatini qaytaradi, chunki `olma` mevalar ro'yxatida mavjud.

2. `not in` **operatori**
- Bu operator yordamida elementning ma'lum bir ketma-ketlikda mavjud emasligini tekshirish mumkin.
```python
mevalar = ['olma', 'banan', 'nok']
if 'uzum' not in mevalar:
    print("Uzum ro'yxatda mavjud emas.")
```
`Natija:` **Uzum ro'yxatda mavjud emas.**
Yuqorida `uzum not in mevalar` ifodasi True qiymatini qaytaradi, chunki 'uzum' mevalar ro'yxatida mavjud emas.

3. Stringlarda misollar
- A'zolik operatorlari **qatorlar**(`string`) bilan ham ishlaydi. Kichik qatorning kattaroq qator ichida mavjud yoki mavjud emasligini tekshirish mumkin.
```python
matn = "Salom dunyo"
if 'dunyo' in matn:
    print("'dunyo' matn ichida mavjud.")
```

## IDENTIFIKATSIYA(IDENTYFY) OPERATORLARI
- Pythonda identifikatsiya (identity) operatorlari ikki ob'ektning bir xil xotira joylashuvida saqlanayotganini aniqlash uchun ishlatiladi. Bu operatorlar ob'ektlarning identifikatorlarini solishtiradi, ya'ni ikki o'zgaruvchining aslida bitta ob'ektga ishora qilayotganini tekshiradi.

1. `is` **operatori**
- `is` operatori yordamida ikkita o'zgaruvchining bir xil ob'ektga ishora qilayotganligini tekshirish mumkin.
```python
a = [1, 2, 3]
b = a
if a is b:
    print("a va b bir xil ob'ekt.")
```
**Natija:** `a va b bir xil ob'ekt.` <br>
Yuqorida `a` va `b` bir xil ro'yxatga ishora qilmoqda, shuning uchun `a is b` ifodasi `True` qiymatini qaytaradi.

2. `is not` **operatori**
`is not` operatori yordamida ikkita o'zgaruvchining bir xil obyektga ishora qilmayotganini tekshirish mumkin.
```python
a = [1, 2, 3]
b = [1, 2, 3]
if a is not b:
    print("a va b bir xil ob'ekt emas.")
```
**Natija:** `a va b bir xil ob'ekt emas.`
Yuqorida `a` va `b` bir xil qiymatlarni o'z ichiga olgan bo'lsa ham, ular alohida ob'ektlar. Shuning uchun `a is not b` ifodasi True qiymatini qaytaradi.

- Identifikatsiya operatorlarining ishlash prinsipi
    - Identifikatsiya operatorlari ob'ektlarning xotira joylashuvini tekshiradi, ya'ni ob'ektlarning `ID` raqamlarini solishtiradi.
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))  # a ob'ektining ID raqami
print(id(b))  # b ob'ektining ID raqami
```
Agar `a` va `b` ID raqamlari turli bo'lsa, demak ular alohida obyektlar.

## ARALASHTIRILGAN OPERATORLAR(MIXED OPERATORS)
- Python dasturlash tilida aralashtirilgan **operatorlar**(`mixed operators`) deganda bir nechta turli operatorlarni bitta ifodada ishlatish tushuniladi. Bu ifodalar matematik va mantiqiy amallarni birlashtirib, ancha murakkab hisob-kitoblar yoki shartlarni aniqlashga yordam beradi. Quyida aralashtirilgan operatorlardan foydalanish misollari keltirilgan:

1. `Arifmetik` va `mantiqiy` operatorlar aralashmasi
```python
x = 10
y = 5
z = 20

natija = (x + y) * z > 100 and z % y == 0
print(natija)
```
**Natija:** `True`
Yuqoridagi `(x + y) * z > 100` and `z % y == 0` ifodasi arifmetik (`+, *, %`) va mantiqiy (`and`) operatorlar aralashmasidan iborat. Ifoda birinchi bo'lib `(x + y) * z > 100` qismini hisoblaydi, so'ngra `z % y == 0` qismini tekshiradi va oxirida and operatori yordamida natijalarni birlashtiradi.

2. `Arifmetik` va `solishtirish` operatorlari aralashmasi
```python
a = 7
b = 3

natija = a * 2 > b + 5
print(natija)
```
**Natija:** `True`
Yuqorida `a * 2 > b + 5` ifodasi avval `a * 2 va b + 5` qismlarini hisoblaydi, keyin esa ularni `>` solishtirish operatori bilan solishtiradi.

3. **Shartli**(`ternary`) ifoda va arifmetik operatorlar
```python
a = 10
b = 5

max_qiymat = a if a > b else b
print(max_qiymat)
```
**Natija:** `10`
Yuqoridagi misolda `a if a > b else b` shartli ifoda yordamida aralashtirilgan operatorlar orqali `a` va `b` ning maksimal qiymatini aniqlaymiz.

## AMALIYOT
1. Ikkita o'zgaruvchi yarating va ularning qiymatlarini qo'shib natijani ekranga chiqaruvchi dastur yozing.
2. Foydalanuvchi tomonidan kiritilgan ikkita sonning ayirmasini hisoblab ekranga chiqaruvchi dastur yozing.
3. Ikkita o'zgaruvchi yarating va ularni bo'lgandan keyin butun qismini ekranga chiqaruvchi dastur yozing.
4. Foydalanuvchi tomonidan kiritilgan ikkita sonni bo'lgandan keyin qoldig'ini ekranga chiqaruvchi dastur yozing.