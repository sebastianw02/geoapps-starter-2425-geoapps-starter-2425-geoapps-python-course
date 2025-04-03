import math
import random

# Dzialania
wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie ** 12
tekst = str(potega)

wartosc_pi = math.pi
losowa = random.choice([1, 2, 3, 4, 5])

# Lancuchy
tekst = f"Wartosc: {tekst}"

print("Dlugosc tekstu:", len(tekst))

print("Czesc tekstu:", tekst[7:10])

print("Funkcja dir dla tekstu:", dir(tekst))

tekst_upper = tekst.upper()
print("Tekst po zmianie na wielkie litery:", tekst_upper)


# Listy
lista = list(tekst)

lista = lista[:8]

lista += [1, 2, 3, 4, 5]

lista.remove(':')

print("Lista po operacjach:", lista)


lista2 = [1, 2, 3, "banan", 100]

lista3 = [x ** 2 for x in lista2 if x != "banan"]

lista4 = [x for x in range(2, 17, 2)]

print("Lista2:", lista2)
print("Lista3:", lista3)
print("Lista4:", lista4)

# Slowniki
ja = {
    "imie": "Sebastian",
    "nazwisko": "Wojtas",
    "wiek": 22,
    "moje_hobby": [
        {"nazwa": "bieganie", "dlaczego": "bo polepsza samopoczucie"},
        {"nazwa": "gry komputerowe", "dlaczego": "bo daja satysfakcje"}
    ]
}

print("Moje hobby:", ja["moje_hobby"])

print("Pierwsze hobby:", ja["moje_hobby"][0]["nazwa"])

print("Klucze slownika:", ja.keys())

print("Czy slownik ma klucz 'adres'?", 'adres' in ja)

# Krotki
krotka1 = (1, 2, "3", 4, 2, 5)

print("Dlugosc krotki:", len(krotka1))
print("Pierwszy element krotki:", krotka1[0])

print("Ile razy wystepuje 2 w krotce:", krotka1.count(2))

try:
    krotka1[0] = 2
except TypeError as e:
    print(f"Blad: {e}")

# Zbiory
X = set("kalarepa")
Y = set("lepy")

print("Czesc wspólna zbiorów X i Y:", X & Y)









