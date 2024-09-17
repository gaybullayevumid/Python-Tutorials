# PYTHON DASTURLASH ASOSLARI

## 3-dars Ro'yxatlar va qatorlar.

- Mavzular
    - Ro'yxatlar(lists) bilan ishlash.
    - Qatorlar (tuples) va ular bilan ishlash.
    - Indekslar va bo'laklash (slicing).

## RO'YHATLAR(LISTS) BILAN ISHLASH

Python dasturlash tilida ro'yxatlar (`lists`) bir nechta qiymatlarni bitta o'zgaruvchiga saqlash imkonini beradi. Ro'yxatlar `dinamik` tuzilma bo'lib, ular yaratishdan keyin ham o'zgartirilishi mumkin.

### RO'YHAT YARATISH

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
```

### RO'YHATLARGA MUROJAT QILISH

> [!CAUTION]
> Dasturlash olamida indeks `0` dan boshlanadi! Ya'ni Listning birinchi elementing tartib raqami (indeksi) `0` ga, ikkinchi elementning indeksi `1` ga teng va hokazo.

```python
print(my_list[0])  # Birinchi element
print(my_list[-1])  # Oxirgi element
```

### RO'YHAT UZUNLIGINI TOPISH

Ro'yhat uzunligini topish ya'ni ichida nechta element borligini topish uchun `len()` funksiyasidan foydalanamiz.

```python
print(len(my_list))
``` 

### RO'YHATGA E'LEMENT QO'SHISH

- **Oxiriga element qo'shish:** `.append()`

```python
my_list = [1, 2, 3]
my_list.append(6)
print(my_list)
```
**Natija:** <br>
```shell
[1, 2, 3, 6]
```

- Oddiy `.append()` faqat bitta element qo'shadi, lekin agar siz list yoki boshqa takrorlanadigan obyekt qo'shsangiz, u element emas, balki ro'yxat sifatida qo'shiladi.
```python
my_list = [1, 2, 3]
my_list.append([4, 5])  # List ichiga yana bir list qo'shish
print(my_list)
```
**Natija:** <br>
```shell
[1, 2, 3, [4, 5]]
```

- **Bir nechta element qo'shish** `.extend()`

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print("extend() natijasi:", my_list) # Bu ro'yxatning elementlarini alohida qo'shadi
```

**Natija:** <br>

```shell
extend() natijasi: [1, 2, 3, 4, 5]
```

- **Belgilangan joyga element qo'shish:** `.insert()`

```python
my_list = [1, 2, 3]
my_list.insert(2, 99)  # 2-pozitsiyaga 99 ni qo'shish
print(my_list)
```
**Natija:**
```shell
[1, 2, 99, 3]
```

- `+=` **operatori yordamida ro'yxatga qo'shish**
    - Siz ro'yxatga boshqa ro'yxatni qo'shish uchun `+=` operatoridan ham foydalanishingiz mumkin:
```python
my_list = [1, 2, 3]
my_list += [4, 5]
print(my_list)
```
**Natija:**
```shell
[1, 2, 3, 4, 5]
```

### E'LEMENTLARNI O'CHIRISH

- **Belgilangan elementni o'chirish:** `.remove()`
    - Bu usul ro'yxatdan kiritilgan qiymatga teng bo'lgan birinchi uchragan elementni o'chiradi.

```python
my_list = [1, 2, 3, 4, 3, 5]
my_list.remove(3)  # Ro'yxatdan birinchi 3 ni o'chiradi
print(my_list)
```
**Natija:** <br>
```shell
[1, 2, 4, 3, 5]
```

- **Oxirgi elementni o'chirish:** `.pop()`

```python
my_list.pop()
print(my_list)
```

- **Indeks bo'yicha elementni o'chirish:** `.pop(index)`

```python
my_list.pop(0)  # Birinchi elementni o'chirish
print(my_list)
```

### RO'YHATNI TOZALASH

Ro'yhatni tozalash uchun `.clear()` metodidan foydalanamiz.

```python
my_list.clear()
print(my_list)
```

### RO'YHATNI SARALASH

Ro'yhatni saralash uchun `.sort()` metodidan foydalanamiz. `.sort()` metodi ro'yhatimiz raqamlardan iborat bo'lsa o'sib borish tartibida saralaydi, agar ro'yhatimiz stringdan(harflardan) tashkil topgan bo'lsa alifbo tartibida saralaydi.

Pythonda ro'yxatlar bilan ishlashda `sort()` va `sorted() `metodlari mavjud bo'lib, ularning farqlari quyidagicha:

#### `.sort()` metodi
- `sort()` metodi ro'yxatni o'zida o'zgartiradi (`in-place`). Bu metod chaqirilganda asl ro'yxat o'zgartiriladi va yangi ro'yxat yaratilmaydi.

- sort() metodi faqat ro'yxatlar (lists) uchun mavjud.

```python
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)
```

#### `.sorted()` funksiyasi

- `sorted()` funksiyasi asl ro'yxatni o'zgartirmaydi, balki saralangan elementlardan yangi ro'yxat yaratadi va qaytaradi.

- `sorted()` funksiyasi ro'yxat (`lists`) dan tashqari boshqa iteralanadigan (`iterable`) obyektlar bilan ham ishlashi mumkin, masalan, qatorlar (`tuples`), lug'atlar (`dictionaries`), va hokazo.

- `sorted()` funksiyasi saralangan yangi ro'yxatni qaytaradi.

```python
my_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(my_list)
print(sorted_list)  # [1, 1, 3, 4, 5, 9]
print(my_list)      # [3, 1, 4, 1, 5, 9]
```

#### Qo'shimcha parametrlar

- `key` parametri: Elementlarni solishtirish uchun qo'shimcha funksiyani belgilash imkonini beradi.

- `reverse` parametri: Saralash tartibini belgilaydi (True bo'lsa, teskari tartibda saralanadi).

`.sort()` metodi bilan

```python
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort(reverse=True)
print(my_list)  # [9, 5, 4, 3, 1, 1]
```

`.sorted()` funksiyasi bilan

```python
my_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(my_list, reverse=True)
print(sorted_list)  # [9, 5, 4, 3, 1, 1]
print(my_list)      # [3, 1, 4, 1, 5, 9]
```


### RO'YHATNI TESKARIGA O'ZGARTIRISH

Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin. Buning uchun 
`.reverse()` metodidan foydalanamiz.

```python
my_list.reverse()
print(my_list)
```

### RO'YHATNI BIRLASHTIRISH

Pythonda ro'yhatlarni birlashtirishni bir nechta usullari bor. Quyida ularga misollar ko'ramiz:

Birinchi usuli `+` operatori bilan birlashtirish:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)
```

**Natija:** `[1, 2, 3, 4, 5, 6]`

`.extend()` metodi bilan birlashtirish:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
```

**Natija:** `[1, 2, 3, 4, 5, 6]`

`itertools.chain()` yordamida:

```python
import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list(itertools.chain(list1, list2))
print(combined_list)
```

**Natija:** `[1, 2, 3, 4, 5, 6]`

### RO'YHAT ICHIDAGI RO'YHAT

Pythonda ro'yxatlar ichidagi ro'yxatlar, ya'ni `ko'p o'lchovli ro'yxatlar` yaratish va ulardan foydalanish juda oddiy. Quyida bunday ro'yxatlar bilan qanday ishlashni ko'rsatib beraman.

```python
multi_dimensional_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

#### Elementlarga murojaat qilish

Ro'yxat ichidagi ro'yxatdagi elementlarga indekslar yordamida murojaat qilish mumkin.

```python
print(multi_dimensional_list[0][2])  # 3
```
Yuqoridagi kodda `0` indexda turgan ro'yhatni tanlab oldim va tanlangan ro'yhatning ichidagi `2` indexda turgan elementga murojat qildim.

Ro'yxatlar ichidagi ro'yxatlarga yangi ro'yxat qo'shish mumkin:

```python
multi_dimensional_list.append([10, 11, 12])
print(multi_dimensional_list)
```

Ro'yhat ichidagi ro'yhatlarni o'zgartirish mumkin:

```python
multi_dimensional_list[0] = [13, 14, 15]
print(multi_dimensional_list)
```

Ma'lum bir ichki ro'yxat elementini o'zgartirish mumkin:

```python
multi_dimensional_list[1][1] = 99
print(multi_dimensional_list)
```

### RO'YHATNI KO'PAYTIRISH

```python
my_list = [1, 2, 3]
multiplied_list = my_list * 3
print(multiplied_list)
```

### RO'YHATDA E'LEMENT BORLIGINI TEKSHIRISH

Python'da ro'yxat ichida element borligini tekshirish uchun `in` operatoridan foydalanish mumkin. Bu operator juda sodda va qulay bo'lib, ro'yxat ichida ma'lum bir elementning mavjudligini aniqlash imkonini beradi.

```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False
```
### QO'SHIMCHA FUNKSIYALAR

Python dasturlash tilida ro'yxatlar bilan ishlashda quyidagi funksiyalar yordamida ro'yxatdagi elementlarni `qo'shish`, `maksimal` va `minimal` qiymatlarni topish mumkin:

`sum()` **funksiyasi:** Ro'yxatdagi barcha sonlarning yig'indisini qaytaradi.

```python
my_list = [10, 20, 30, 40, 50]
# Ro'yxatdagi elementlar yig'indisini hisoblash
sum_of_list = sum(my_list)
print(f"Ro'yxatdagi elementlar yig'indisi: {sum_of_list}")
```

`max()` **funksiyasi:** Ro'yxatdagi eng katta qiymatni qaytaradi.

```python
# Ro'yxatdagi eng katta qiymatni topish
max_value = max(my_list)
print(f"Ro'yxatdagi eng katta qiymat: {max_value}")
```

`min()` **funksiyasi:** Ro'yxatdagi eng kichik qiymatni qaytaradi.

```python
# Ro'yxatdagi eng kichik qiymatni topish
min_value = min(my_list)
print(f"Ro'yxatdagi eng kichik qiymat: {min_value}")
```

### `.range()` FUNKSIYASI

Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. 
`list()` funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:

```python
sonlar = list(range(0,10)) # 
print(sonlar)
```
**Natija:** `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

Yuqoridagi misolda `range(0,10)` funktsiyasi 0 dan 9 gacha sonlar ketma-ketligini shakllantirdi, `list(range(0,9))` esa bu ketma-ketlikni ro'yxatga aylantirdi.

> [!CAUTION]
> Diqqat! E'tibor qiling 
`range()` funktsiyasi ikkinchi indeksdan bitta avval to'xtaydi.

`range()` yordamida qadamni ham berishimiz mumkin:

```python
juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)
```
**Natija:**
**Juft sonlar:** `[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]`
**Toq sonlar:** `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19] `

> [!NOTE]
> Agar sonlar ketma-ketligi `0` dan boshlansa, `range()` funktsiyasida yakuniy indeksni ko'rsatish kifoya. Misol uchun `range(0,10)` emas `range(10)` deb yozsak ham bo'laveradi.



## TUPLES

Qatorlar (`tuples`) Pythonda `o'zgarmas` ma'lumot tuzilmasi bo'lib, ularni bir marta yaratgandan keyin o'zgartirib bo'lmaydi. Ular ro'yxatlar (`lists`) ga o'xshash, lekin qatorlar bir marta yaratib olingandan keyin o'zgartirilmaydi, ya'ni ularga yangi element qo'shib bo'lmaydi, mavjud elementlarni o'chirib bo'lmaydi yoki o'zgartirib bo'lmaydi. Qatorlar ko'pincha o'zgarmas ma'lumotlar to'plamini saqlash uchun ishlatiladi.

### TUPLE YARATISH

```python
# Oddiy tuple yaratish
my_tuple = (1, 2, 3)
print(my_tuple)  # (1, 2, 3)

# list dan tuple yaratish
another_tuple = tuple([4, 5, 6])
print(another_tuple)  # (4, 5, 6)

# bo'sh tuple yaratish
empty_tuple = ()
print(empty_tuple)  # ()

# bitta elementli tuple yaratish uchun vergul qo'yish kerak
single_element_tuple = (1,)
print(single_element_tuple)  # (1,)
```

### TUPLE XUSUSIYATLARI
- **O'zgarmasligi (Immutable):** `Tuple` yaratilgandan so'ng, uning elementlarini `o'zgartirib` yoki `o'chirib` bo'lmaydi.
- **Tartiblanganligi:** `Tuple` ichidagi elementlar `tartiblangan` holda saqlanadi.
- **Qayta ishlash:** `Tuple` ichidagi ma'lumotlar o'z tartibini saqlaydi va turli xil ma'lumot turlarini saqlashi mumkin (masalan, `number`, `string` va boshqalar).

### TUPLENING AFZALLIKLARI
- **O‘zgarmasligi:** Tupleni `himoyalangan` yoki `o‘zgartirilmas` ma’lumotlar saqlash uchun ishlatish mumkin.
- **Tezligi:** Tuplelar ro‘yxatlarga qaraganda `tezroq` ishlovchi ma'lumot turi hisoblanadi.

### TUPLE E'LEMENTLARIGA MUROJAT QILISH

`Tuple` elementlariga ham `list`larga o'xshab indeks orqali murojaat qilish mumkin. Indekslar `0` dan boshlanadi:

```python
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # 10
print(my_tuple[2])  # 30
print(my_tuple[-1]) # 50 (oxirgi element)
```

### TUPLE USTIDA AMALLAR
> [!NOTE]
> Tuple o'zgarmas bo'lganligi sababli, uni `o'zgartirib bo'lmaydi`. Lekin uni boshqa `tuple`lar bilan `birlashtirish` yoki `takrorlash` mumkin.

1. Tuplelarni birlashtirish:
    - Tuple'lar o'zgarmas (`immutable`) ma'lumot turi bo'lganligi uchun birlashtirish jarayonida asl `tuple`lar o'zgarmaydi. Yangi tuple yaratiladi.

    ```python
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    new_tuple = tuple1 + tuple2
    print(new_tuple)  # (1, 2, 3, 4)
    ```
    - Agar siz bir tupleni o'z-o'ziga birlashtirishni xohlasangiz, yana bir tuple qo'shib berishingiz kerak bo'ladi.
    ```python
    tuple1 = (1, 2, 3)

    # tuple1 ni o'z-o'zidan ikki marta birlashtirish
    result = tuple1 + tuple1
    print(result)
    ```

#### TUPLENI BOSHQA MALUMOT TURLARI BILAN BIRLASHTIRISH

2. Tupleni ko‘paytirish:
```python
tuple1 = ("hello",)
new_tuple = tuple1 * 3
print(new_tuple)  # ('hello', 'hello', 'hello')
```

### TUPLE UZUNLIGINI ANIQLASH

`Tuple`dagi elementlar sonini aniqlash uchun `len()` funksiyasidan foydalaniladi:

```python
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # 5
```

### TUPLEDA `in` OPERATORI
- Biror qiymat tupleda bor yoki yo‘qligini `in` operatori yordamida tekshirish mumkin:
```python
my_tuple = ("apple", "banana", "cherry")
print("banana" in my_tuple)  # True
```

### TUPLENI QIYMATLARGA AJRATISH(`Unpacking`)
- Tuplening barcha qiymatlarini o‘zgaruvchilarga ajratib olish mumkin:
```python
my_tuple = ("apple", "banana", "cherry")
(fruit1, fruit2, fruit3) = my_tuple
print(fruit1)  # 'apple'
print(fruit2)  # 'banana'
print(fruit3)  # 'cherry'
```

### TUPLE ICHIDA TUPLE
- Tuple ichida yana boshqa tuplelar saqlanishi mumkin:
```python
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # (3, 4)
```
### TUPLE BILAN ISHLASHDA FOYDALI FUNKSIYALAR
1. `.count():` Tuple ichida biror qiymat necha marta takrorlanganini aniqlaydi.
```python
my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  # 2
```

2. `.index():` Tuple ichida berilgan qiymatning indeksini topadi.
```python
my_tuple = (1, 2, 3)
print(my_tuple.index(2))  # 1
```

> [!NOTE]
> Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni `list()` funksiyasi yordamida `List` (oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib `tuple()` funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin:

```python
toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)
```

## AMALIYOT
1. **Ro'yhat yaratish va elementga murojat qilish.**
    - Quyidagi elementlarga ega bo'lgan ro'yxatni yarating: `'olma'`, `'banan'`, `'gilos'`, `'xurmo'`, `'anjir'`.
    - Ro'yxatning `ikkinchi` va `to'rtinchi` elementlarini oling va ularni terminalga chiqaring.

2. **Ro'yxatni o'zgartirish.**
    - `1` dan `5` gacha bo'lgan sonlar ro'yxatini yarating.
    - Ro'yxatdagi `uchinchi` elementni `10` ga almashtiring va yangilangan ro'yxatni terminalga chiqaring.

3. **Element qo'shish va o'chirish.**
    - Bo'sh ro'yxat yarating.
    - Ro'yxatga `'dog'`, `'cat'` va `'chicken'` elementlarini qo'shing.
    - Ro'yxatdan `'cat'` ni `o'chiring` va natijani terminalga chiqaring.

4. **Ro'yxat uzunligini topish.**
    - Quyidagi elementlarga ega ro'yxat yarating: `'red'`, `'green'`, `'blue'`, `'yellow'`, `'purple'`.
    - Ro'yxatning `uzunligini` toping va terminalga chiqaring.

5. **Ro'yxatlarni birlashtirish.**
    - Quyidagi ikkita ro'yxatni yarating:
        - Ro'yxat1: `['a', 'b', 'c']`
        - Ro'yxat2: `['d', 'e', 'f']`
    - Ikkala ro'yxatni birlashtiring va natijani terminalga chiqaring.

6. **Elementning mavjudligini tekshirish.**
    - Quyidagi ro'yxatni yarating: `['mashina', 'avtobus', 'velosiped', 'poyezd']`
    - Ro'yxatda `'avtobus'` bor-yo'qligini tekshiring va natijani terminalga chiqaring `(True/False)`.

7. **Ro'yxatni saralash.**
    - Quyidagi sonlardan iborat ro'yxat yarating: `[3, 1, 4, 2, 5]`.
    - Ro'yxatni `o'sish` tartibida saralang va natijani terminalga chiqaring.

8. **Ro'yxatdagi elementlarni teskari tartibda Terminalga chiqarish.**
    - Quyidagi ro'yxatni yarating: `[10, 20, 30, 40, 50]`.
    - Ro'yxatni `teskari` tartibda terminalga chiqaring (`reverse`).

9. **Ro'yxatni tozalash.**
    - Quyidagi ro'yxatni yarating: `['kitob', 'qalam', 'daftar', 'sumka']`.
    - Ro'yxatni tozalang (`hamma elementlarni o'chiring`) va bo'sh ro'yxatni terminalga chiqaring.

10. **Ro'yxat elementlarini ko'paytirish.**
    - Ro'yxat yarating: `[1, 2, 3]`.
    - Ro'yxat elementlarini `4` marta ko'paytiring va natijani terminalga chiqaring.

11. **Minimal va Maksimal qiymatni topish.**
    - Quyidagi ro'yxatni yarating: `[25, 17, 9, 50, 33]`.
    - Ro'yxatdagi `eng kichik` va `eng katta` qiymatni toping va terminalga chiqaring.

12. **Ro'yxatni Nusxalash.**
    - Quyidagi ro'yxatni yarating: `[100, 200, 300, 400, 500]`.
    - Ushbu ro'yxatdan `nusxa` ko'chiring va `yangi` ro'yxatni qaytaring.

13. **Tuple yaratish va qiymatlarni chiqarish.**
    ```python
    # 1. Quyidagi tuple'ni yarating va har bir elementini ekranga chiqaring.
    my_tuple = (10, 20, 30, 40, 50)
    ```
    **Natija:**
    ```shell
    (10, 20, 30, 40, 50)
    ```
14. **Tuple elementlariga indeks orqali murojaat qilish.**
    ```python
    # 2. Quyidagi tuple'dan birinchi va oxirgi elementni ekranga chiqaring.
    my_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')
    ```
    **Natija:**
    ```shell
    Birinchi element: apple
    Oxirgi element: elderberry
    ```
15. **Tuple’larni birlashtirish.**
    ```python
    # 3. Ikkita tuple'ni birlashtirib, yangi tuple yarating.
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    ```
    **Natija:**
    ```shell
    (1, 2, 3, 4, 5, 6)
    ```

16. **Tuple uzunligini aniqlash.**
    ```python
    # 4. Quyidagi tuple'ning uzunligini aniqlang.
    my_tuple = ('cat', 'dog', 'rabbit', 'parrot')
    ```
    **Natija:**
    ```shell
    4
    ```

17. **Tuple ichidagi elementlarning qiymatini sanash.**
    ```python
    # 5. Tuple ichida necha marta 'apple' so‘zi mavjudligini aniqlang.
    fruits = ('apple', 'banana', 'cherry', 'apple', 'apple', 'banana')
    ```
    **Natija:**
    ```shell
    3
    ```
18. **Tuple ichida qiymat mavjudligini tekshirish.**
    ```python
    # 6. Tuple ichida 'banana' bor-yo‘qligini tekshiring.
    fruits = ('apple', 'banana', 'cherry')
    ```
    **Natija:**
    ```shell
    True
    ```