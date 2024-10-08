# PYTHON DASTURLASH ASOSLARI

## 10-Dars Exception Handling

> [!NOTE]
> Pythonda `Exception Handling`(**Istisno holatlarni boshqarish**) dasturlashda xatoliklarni to'g'ri boshqarish va dasturimizni xatoliklardan himoya qilish uchun muhimdir. Pythonda bu jarayonni `try`, `except`, `else`, va `finally` bloklari yordamida amalga oshirish mumkin.

### EXCEPTION HANDLING HAQIDA UMUMIY TUSHUNCHA
Dastur ishlashi davomida turli xatoliklar yuz berishi mumkin, masalan, noto'g'ri ma'lumot kiritish, bo'linishda nolga bo'lishga urinish yoki fayl mavjud bo'lmaganda uni o'qishga urinish. Bu kabi holatlarda dastur to'xtab qolishi mumkin, lekin Exception Handling yordamida biz bu xatolarni boshqarishimiz va dasturimizning barqaror ishlashini ta'minlashimiz mumkin.

### EXCEPTION HANDLING SINTAKSISI

```python
try:
    # Potensial xato yuzaga kelishi mumkin bo'lgan kod
except XatoNomi:
    # Xato sodir bo'lganda bajariladigan kod
```
1. `try` va `except`
- `try` bloki ichida xatolik yuz berishi mumkin bo'lgan kod yoziladi. Agar xatolik yuz bersa, `except` bloki ishga tushadi va xatolikni boshqaradi.
    ```python
    try:
        son = int(input("Biror son kiriting: "))
        natija = 10 / son
        print(f"Natija: {natija}")
    except ZeroDivisionError:
        print("Xatolik: Nolga bo'lish mumkin emas!")
    except ValueError:
        print("Xatolik: Iltimos, butun son kiriting!")
    ```
        - Bu yerda:
            - Agar foydalanuvchi `0` kiritsa, `ZeroDivisionError` xatosi yuz beradi va u `except ZeroDivisionError` tomonidan boshqariladi.
            - Agar foydalanuvchi son o'rniga harf kiritsa, `ValueError` xatosi yuz beradi va u `except ValueError` tomonidan boshqariladi.
2. `else`
- Agar `try` blokida xatolik yuz bermasa, `else` bloki ishga tushadi. Bu blokda xatoliklar bo'lmasa bajarilishi kerak bo'lgan kodlar yoziladi.
    ```python
    try:
        son = int(input("Biror son kiriting: "))
        natija = 10 / son
    except ZeroDivisionError:
        print("Xatolik: Nolga bo'lish mumkin emas!")
    except ValueError:
        print("Xatolik: Iltimos, butun son kiriting!")
    else:
        print(f"Natija: {natija}")
    ```
    Yuqoridagi misolda, agar foydalanuvchi to'g'ri son kiritsa va `0` bo'lmasa, `else` qismi ichidagi `natija` chop etiladi.
3. `finally`
- `finally` bloki har qanday holatda ham, xatolik yuz bergan yoki bermagan bo'lsa ham, bajariladi. Bu blok, masalan, resurslarni tozalash yoki fayllarni yopish uchun ishlatilishi mumkin.
    ```python
    try:
        son = int(input("Biror son kiriting: "))
        natija = 10 / son
    except ZeroDivisionError:
        print("Xatolik: Nolga bo'lish mumkin emas!")
    except ValueError:
        print("Xatolik: Iltimos, butun son kiriting!")
    else:
        print(f"Natija: {natija}")
    finally:
        print("Dastur yakunlandi.")
    ```
    Yuqoridagi misolda, dastur yakunida har doim `finally` bloki ichidagi `Dastur yakunlandi.` xabari chop etiladi.

4. Xatoni nom bilan chiqarish:
- Ba'zi hollarda, sodir bo'lgan xatoni dasturiy tilda yozib chiqish kerak bo'lishi mumkin. Bunda `as` kalit so'zi orqali xato ob'ektiga nom berish mumkin:

    ```py
    try:
        file = open('myfile.txt')
    except FileNotFoundError as e:
        print(f"Xato: {e}")
    ```
    **Tushuntirish:**
    - Agar `myfile.txt` nomli fayl mavjud bo'lmasa, `FileNotFoundError` xatosi paydo bo'ladi.
    - `as e` orqali bu xatoni `e` nomli o'zgaruvchida saqlab, uni ekranga chiqarish mumkin.

5. 

## AMALIYOT
1. Nolga bo'lishni tekshirish
    - Foydalanuvchi `2` ta son kiritadi. Siz bu sonlarni `bir-biriga` bo'lishingiz kerak, lekin `0` ga bo'lishdan ehtiyot bo'lish kerak.

**Natija:** Agar foydalanuvchi `0` kiritsa, `Xatolik: Nolga bo'lish mumkin emas` degan xabar chiqadi. Agar foydalanuvchi son o'rniga boshqa belgilar kiritsa, `Xatolik: Iltimos, faqat son kiriting` degan xabar chiqadi.

2. Faylni ochish va o'qish
    - Berilgan fayl nomini ochishga harakat qiling. Agar fayl mavjud bo'lmasa, tegishli xatolik xabari chiqsin.

**Natija:** Agar foydalanuvchi mavjud bo'lmagan fayl nomini kiritsa, `Xatolik: Fayl topilmadi` degan xabar chiqadi.

3. Raqamli qiymatni aylantirish
    - Foydalanuvchi kiritgan satrni butun son yoki haqiqiy songa aylantirishga harakat qiling.

**Natija:** Agar foydalanuvchi son emas, balki boshqa harflar yoki belgilar kiritsa, `Xatolik: Satrni son ko'rinishiga o'tkazib bo'lmadi` degan xabar chiqadi.

4. Hisoblash operatsiyasi
    - Foydalanuvchi ikkita son va bir operator (`+, -, *, /`) kiritsin. Hisoblashni amalga oshiring va natijani ko'rsating.

**Natija:** Agar foydalanuvchi noto'g'ri operator kiritsa yoki nolga bo'lishga harakat qilsa, tegishli xatolik xabarlari chiqadi.