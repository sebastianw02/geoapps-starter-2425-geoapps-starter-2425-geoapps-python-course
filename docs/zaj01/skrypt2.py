import random

#----------------------------Liczby
wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**12

tekst = str(potega)
print(tekst)

wartosc_pi = 3.14
print(wartosc_pi)

losowa = random.choice([1,2,3,4,5])
print(losowa)

#----------------------------Łańcuchy
tekst = f"Wartosc: {tekst}"
print(len(tekst))
print(tekst[1:4])

#print(dir(tekst))
print(tekst.upper())

#tekst[1]= "p"

#----------------------------Listy
lista = list(tekst)
print(lista[:8])

lista.append([1,2,3,4,5])
print(lista)

lista.remove(lista[7])
print(lista)

#----------------------------Listy składane
lista2 = [1,2,3,"banan",100]

lista3 = [x**2 for x in lista2 if x != "banan"]
print(lista3)

lista4 = list(range(2, 17, 2))
print(lista4)

##----------------------------Słowniki

ja = {
    "imie" : "Karolina",
    "nazwisko" : "Kucharz",
    "wiek" : "21",
    "moje_hobby" : [
        {"nazwa" : "hiking", "dlaczego" : "lubie śmierdzieć"},
        {"nazwa" : "geoinformatyka", "dlaczego" : "przestrzenne masohizm dane są fascynujące"}
    ]
}
print(ja["moje_hobby"])
print(ja["moje_hobby"][0]["nazwa"])
print(ja.keys())

masz_gdzie_mieszkac = "adres" in ja
print(masz_gdzie_mieszkac)

##----------------------------Krotki
krotka1 = (1,2,"3",4,2,5)
print(len(krotka1), krotka1[0])
ile2 = krotka1.count(2)
print(ile2)
#krotka1[0] = 2 #sie nie da

##----------------------------Zbiory
X = set("kalarepa")
Y = set("lepy")
print(X & Y)