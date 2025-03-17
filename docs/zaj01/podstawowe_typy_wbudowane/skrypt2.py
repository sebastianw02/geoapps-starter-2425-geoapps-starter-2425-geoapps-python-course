import math
import random

#-----------------działania ----------------
wartosc = 100
print(f'wartosc: {wartosc}')

dodawanie = wartosc + 123.15
print(f'dodawanie: {dodawanie}')

potega = dodawanie ** 12
print(f'potega: {potega}')

tekst = str(potega)
print(f'tekst: {tekst}')

wartosc_pi = math.pi
print(f'pi: {wartosc_pi}')

losowa = random.choice([1, 2, 3, 4, 5])
print(f'losowa" {losowa}')

#---------------łańcuchy znaków ---------------------
tekst = f"wartosc: {tekst}"
print(f'tekst: {tekst}')
print(len(tekst))
print(tekst[1:4])
print(dir(tekst))
print(tekst.upper())
#tekst[2] = "p" 

#-------------listy---------------
lista = list(tekst)
lista = lista[:8]
lista.append([1,2,3,4,5])
lista.remove(":")
print("Zawartosc listy:", lista)

#------------listy składane-----------
lista2 = [1,2,3,'banan', 100]
lista3 = [x ** 2 for x in lista2 if x != "banan"]
lista4 = [x for x in range(2, 17) if x % 2 == 0]
print('Lista 2:', lista2)
print('Lista 3:', lista3)
print('Lista 4:', lista4)

#----------słowniki------------
ja = {}
ja["imie"] = "Zofia"
ja["nazwisko"] = "Fabrowska"
ja["wiek"] = 21
ja["moje_hobby"] = [
    {"nazwa": "wędrówki", "dlaczego": "kocham naturę"},
    {"nazwa": "czytanie", "dlaczego": "rozwija wyobraźnię"}
]
print("Moje hobby:", ja['moje_hobby'])
print("Pierwsze hobby:", ja["moje_hobby"][0]["nazwa"])
print("Klucze w słowniku:", ja.keys())
print("Czy słownik posiada klucz 'adres':", "adres" in ja)

#------------------krotki------------------------
krotka1 = (1,2,"3",4,2,5)
print('dlugosc krotki: ', len(krotka1))
print('pierwszy wyraz:', krotka1[0])
print('wystapienia wartosci 2:', krotka1.count(2))
#krotka1[0] = 2

#------------zbiory----------------------
X = set("kalarepa")
Y = set("lepy")
print('czesc wspolna zbiorow:', X & Y)