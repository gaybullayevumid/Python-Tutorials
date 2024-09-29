# PYTHON DASTURLASH ASOSLARI

## 8-dars While Loop

## while loop NIMA?
> [!NOTE]
> `while loop` Pythonda shart bajarilgunga qadar kod blokini qayta-qayta bajarish uchun ishlatiladi. Shart `True` bo'lganida `loop` ishlashda davom etadi, `False` bo'lganda esa to'xtaydi.

### `while loop` SINTAKSISI
```python
while shart:
    # bajariladigan kod
```
**Shart:** Bu `boolean` ifoda bo'lib, u `True` yoki `False` qiymatiga ega bo'lishi kerak. Agar `True` bo'lsa, loop davom etadi, agar `False` bo'lsa, loop tugaydi.

### `while loop`DAN FOYDALANISH
- **Foydalanuvchi kiritmalarini tekshirish:** `while loop` foydalanuvchi kiritgan ma'lumotlarni qayta-qayta tekshirish uchun ishlatilishi mumkin.
- **Ma'lum bir shartga erishilmaguncha bajariladigan operatsiyalar:** Ma'lum bir shart bajarilgunga qadar kodni qayta-qayta bajarish kerak bo'lganda `while loop` ishlatiladi.

- Quyidagi misolda, `while loop` `1` dan `5` gacha bo'lgan sonlarni ekranga chiqaradi.
```python
son = 1

while son <= 5:
    print(son)
    son += 1
```
Yuqoridagi misolda, **loop** `son` o'zgaruvchisi `5` dan kichik yoki teng bo'lgan vaqtda ishlaydi. Har bir takrorlashda son `1` ga oshiriladi. son `6` bo'lganda shart `False` bo'ladi va loop to'xtaydi.

- Quyidagi misolda, `while loop` foydalanuvchidan ma'lumot so'raydi va `stop` so'zi kiritilmaguncha davom etadi.
```python
kiritma = ""

while kiritma != "stop":
    kiritma = input("So'z kiriting (to'xtatish uchun 'stop' yozing): ")
    print(f"Siz '{kiritma}' so'zini kiritdingiz")
```
Yuqoridagi misolda, foydalanuvchi `stop` so'zini kiritmaguncha loop ishlashda davom etadi. `stop` so'zini kiritilgach, shart `False` bo'ladi va **loop** tugaydi.

- Quyidagi misolda, `while loop` sonni qidiradi va topilganda to'xtaydi.
```python
sonlar = [1, 3, 5, 7, 9, 11]
i = 0

while i < len(sonlar):
    if sonlar[i] == 7:
        print("7 soni topildi!")
        break
    i += 1
```
Yuqoridagi misolda, `while loop` ro'yxatdagi sonlarni ketma-ket tekshiradi. `7` soni topilganida, **loop** `break` operatori yordamida to'xtatiladi.

- Quyidagi misolda, `while loop` **musbat** sonlarni ekranga chiqaradi va **manfiy** sonlarni o'tkazib yuboradi.
```python
sonlar = [-2, -1, 0, 1, 2, 3]
i = 0

while i < len(sonlar):
    if sonlar[i] < 1:
        i += 1
        continue
    print(sonlar[i])
    i += 1
```
Yuqorida misolda, **loop** sonlar ro'yxatidagi **manfiy** va **0** qiymatlarini o'tkazib yuboradi. Musbat sonlar chop etiladi.

### `while loop` KAMCHILIKLARI
- **Cheksiz loop:** Agar shart hech qachon `False` bo'lmasa, loop cheksiz davom etishi mumkin, bu esa dasturiy ta'minotning ishdan chiqishiga olib kelishi mumkin.
- **Shartni tekshirish:** Har safar shartni diqqat bilan tekshirish kerak, chunki noto'g'ri shart **loop**ning noto'g'ri ishlashiga olib kelishi mumkin.

## AMALIYOT
1. 1 dan 10 gacha bo'lgan sonlarni terminalga chiqarish:
    - `1` dan `10` gacha bo'lgan sonlarni `while loop` yordamida terminalga chiqaradigan dastur yozing.
2. Foydalanuvchi kiritgan sonning raqamlarini yig'indisini hisoblash:
    - Foydalanuvchidan bir son kiritishini so'rang va ushbu sonning raqamlarini yig'indisini hisoblaydigan dastur yozing. Masalan, foydalanuvchi `123` sonini kiritgan bo'lsa, natija `6` bo'lishi kerak (`1 + 2 + 3`).
3. Foydalanuvchi kiritgan ma'lumot bilan ishlash:
    - Foydalanuvchi `exit` so'zini kiritmaguncha, uning kiritgan ma'lumotlarini qabul qilib terminalga chiqaring.
4. Juft sonlarni hisoblash:
    - Foydalanuvchidan son kiriitishini so'rang va `1` dan ushbu songacha bo'lgan barcha juft sonlarni ekranga chiqaring.
5. Minimal sonni topish:
    - Foydalanuvchidan bir nechta sonlar kiritishni so'rang va foydalanuvchi `0` ni kiritganda kiritilgan sonlar ichidan eng kichik sonni ekranga chiqaring.