# PYTHON DASTURLASH ASOSLARI

## 4-dars To'plamlar(sets)

Python dasturlash tilida to'plamlar(`sets`) — bu to‘plamga qo‘shilgan elementlar faqat bir martadan saqlanadigan va tartibi ahamiyatga ega bo‘lmagan ma'lumotlar tuzilmasi. Bu ma'lumotlar tuzilmasi quyidagi asosiy xususiyatlarga ega:
- **Noyob elementlar:** Setdagi barcha elementlar yagona va takrorlanmaydi.
- **Tartibga ega emas:** Setdagi elementlar tartibi muhim emas va ular indekslanmaydi.
- **O'zgaruvchanlik:** Setlar o‘zgaruvchan bo‘lib, ularga yangi elementlarni qo‘shish yoki olib tashlash mumkin.

### TO'PLAM(SET) YARATISH

```python
# Bo'sh set yaratish
my_set = set()

# Elementlar bilan set yaratish
my_set = {1, 2, 3, 4, 5}
```

### TO'PLAM(SET)GA E'LEMENT QO'SHISH
- To'plamga yangi e'lement qo'shish uchun `.add(value)` metodidan foydalaniladi:
```python
my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}
```
**Natija:** `{1, 2, 3, 4, 5}`

- To'plamga ko'proq e'lement qo'shish uchun `.update(values)` metodidan foydalanamiz:
```python
my_set.update([6, 7, 8])
print(my_set)  # {1, 2, 4, 5, 6, 7, 8}
```

### TO'PLAM(SET)DAN E'LEMENT O'CHIRISH
- To'plamdan e'lement o'lib tashlash uchun `.remove(value)` metodidan foydalaniladi:
```python
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}
```

**Natija:** `{1, 2, 4, 5}`

- Agar to'plamda e'lement mavjud bo'lmasa, `.remove(value)` xato beradi, `.discard(value)` xato bermaydi:

```python
my_set.remove(7)
print(my_set)  # {1, 2, 4, 5}
```

**Natija:** `KeyError: 7` 

```python
my_set.discard(7)
print(my_set)  # {1, 2, 4, 5}
```
**Natija:** `{1, 2, 3, 4, 5`

### TO'PLAM OPERATSIYALARI

To'plamlarda `.intersection()` metodi ikki yoki undan ortiq to'plamlar(sets) o'rtasida umumiy bo'lgan elementlarni aniqlash uchun ishlatiladi. Bu metodda natija sifatida barcha berilgan to'plamlarda mavjud bo'lgan e'lementlar qaytariladi.

Python dasturlash tilida **to'plamlar**(`sets`) ni kesishishini amalga oshirish uchun bir nechta usullar mavjud:
1. **`&` operatori:** Kesishish amali uchun maxsus operator.
2. **`.intersection()` metodi:** Bir yoki bir nechta setlar bilan kesishish amalga oshiriladi.

- `&` operatori orqali ikkita to'plamni tanlab olamiz:
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection_set = set1 & set2
print(intersection_set)  # Natija: {3, 4}
```
- `.intersection()` metodi:
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))  # {3, 4}
```
1-qatorda `set1` nomli to'plam yaratdik. <br>
2-qatorda `set2` nomli to'plam yaratdik. <br>
3-qatorda `set1` nomli to'plam uchun `.intersection()` metodiga `set2` nomli to'plamni berdik. Shunda ikkala to'plam ichida bir xil bo'lgan elementlarni chiqaradi.

- Agar kesishish bo'sh to'plam(set) bilan amalga oshirilsa, natija har doim bo'sh to'plam(set) bo'ladi:
```python
set1 = {1, 2, 3, 4}
empty_set = set()

intersection_set = set1 & empty_set
print(intersection_set)  # Natija: set()
```

- To'plamlarda `.difference()` metodi bir setdagi elementlarni boshqa setdagi elementlardan chiqarib tashlash uchun ishlatiladi. Natijada birinchi setda bor, lekin ikkinchi (yoki ko'proq) setda yo'q bo'lgan elementlar qaytariladi.

Python dasturlash tilida setlar farqini topish oshirish uchun bir nechta usullar mavjud:

- **`-` operatori:** .difference() metodi uchun maxsus operator.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

difference_set = set1 - set2
print(difference_set)  # Natija: {1, 2}
```

- **`difference()` metodi:** Bir yoki bir nechta to'plamlar(set) farqlarini tekshiradi.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

difference_set = set1.difference(set2)
print(difference_set)  # Natija: {1, 2}
```

- To'plamlarda `.union()` (**birlashtirish**) metodi ikki yoki undan ortiq to'plamlarning barcha elementlarini yagona to'plamda birlashtirish uchun ishlatiladi. Natijada barcha to'plamlardan elementlar qaytariladi, takroriy elementlar faqat bitta marta saqlanadi.

Python dasturlash tilida to'plamlarni birlashtirilishini amalga oshirish uchun bir nechta usullar mavjud:

- **`|` operatori:** Birlashtirish amali uchun maxsus operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Natija: {1, 2, 3, 4, 5}
```

- **`.union()` metodi:** Bir yoki bir nechta to'plamlarni birlashtiradi.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Natija: {1, 2, 3, 4, 5}
```

> [!NOTE]
> Birlashtirilgan to'plamda har bir element faqat bir marta bo‘ladi, ya'ni takroriy elementlar olib tashlanadi.

## AMALIYOT
- `my_list = [1, 2, 2, 3, 4, 4, 5]` <br>
Berilgan listdagi takroriy elementlarni olib tashlab, yangi to'plam yarating.
- `set1 = {1, 2, 3, 4}` <br>
`set2 = {3, 4, 5, 6}` <br>
Ikki to'plamdan umumiy elementlarni toping.
- `set1 = {1, 2, 3, 4}` <br>
`set2 = {3, 4, 5, 6}` <br>
Birinchi to'plamda mavjud, ikkinchi to'plamda mavjud bo'lmagan elementlarni aniqlang.
- `set1 = {1, 2, 3, 4}` <br>
`set2 = {3, 4, 5, 6}` <br>
`set3 = {5, 6, 7, 8}` <br>
Uchta to'plamdan umumiy bo'lmagan elementlarni aniqlang.
- `my_set = {5, 2, 9, 1, 7}` <br>
Berilgan to'plamning eng kichik va eng katta elementlarini toping.