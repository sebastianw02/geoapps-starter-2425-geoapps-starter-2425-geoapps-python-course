import math
import random
wartosc = 100

dodawanie = wartosc + 123.15
print(dodawanie)

potega = dodawanie ** 12
print(potega)

tekst = str(potega)
print(tekst)
print(type(tekst))

wartosc_pi = math.pi
print(wartosc_pi)

losowa = random.choice([1,2,3,4,5])
print(losowa)

tekst = f"Wartosc: {tekst}"
print(tekst)

print(len(tekst))
print(tekst[1:4])

print(dir(tekst))

print(tekst.upper())

print(tekst.replace('a', 'p'))

lista = list(tekst)
print(lista)

lista = lista[0:8]
lista = lista + [1,2,3,4,5]
print(lista)
lista.remove(':')
print(lista)

lista2 = [1,2,3,"banan",100]
lista3 = [x ** 2 for x in lista2 if type(x) == int]
print(lista3)

lista4 = list(range(2,16+1,2))
print(lista4)

print(lista2, lista3, lista4)

ja = { }

ja = {
    "imie": "Patryk",
    "nazwisko": "Piątkowski",
    "wiek": "22",
    "moje_hobby": [{"nazwa": "rower", "dlaczego": "bo lubię"}, {"nazwa": "rower", "dlaczego": "bo lubię"}]
}
print(ja)

print(ja["moje_hobby"])

print(ja["moje_hobby"][0]['nazwa'])

print(ja.keys())


if 'adres' in ja.keys(): print(True)
else: print(False)

krotka1 = (1,2,"3",4,2,5)
print(krotka1)
print(len(krotka1))
print(krotka1[0])

print(krotka1.count(2))

#krotka1[1] = 2 błąd

X = set("kalarepa")
Y = set("lepy")

print(X & Y)