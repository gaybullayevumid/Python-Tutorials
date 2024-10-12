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




def subtract(a, b):
    """Ikki sondan birini ayirish funktsiyasi."""
    return a - b

def divide(a, b):
    """Ikki sonni bo'lish funktsiyasi."""
    if b == 0:
        raise ValueError("Bo'lish uchun 0 bilan bo'lish mumkin emas!")
    return a / b