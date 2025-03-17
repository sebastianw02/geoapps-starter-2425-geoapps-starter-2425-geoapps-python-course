import json

#odczyt pliku
with open('docs/zaj01/zadanie_sprawdzające/teksty.json', 'r', encoding='utf-8') as file:
    dane = json.load(file)  #jako słownik

#połączone teksty
    teksty = []  #pusta lista na teksty
for obj in dane["teksty"]:  #iteracja po obiektach w "teksty"
    for tekst in obj.values():  #pobranie wartosci z każego tekstu
        teksty.append(tekst)  #dodanie do listy

 #polaczenie w nowe dane
dane2 = ' '.join(teksty)

 #małe litery
dane2 = dane2.lower()

 #usunięcie . i ,
dane2 = dane2.replace('.', '').replace(',','')

 #podział na wyrazy
wyrazy = dane2.split()

#kozA, brzozA
wyrazy = [a[:-1] + a[-1].upper() for a in wyrazy]

#tylko wyrazy z A lub a
wyrazy_z_a = [] #pusta lista
for wyraz in wyrazy:
    if 'a' in wyraz or 'A' in wyraz:
        wyrazy_z_a.append(wyraz)
#wyrazy = [w for w in wyrazy if 'a' in w or 'A' in w]

#unikalne wyrazy
wyrazy_unique = set(wyrazy) #zbiór = set

#ilosc wystapien w tekscie
count = {} #pusty słownik
for wyraz in wyrazy:
    if wyraz in count:
        count[wyraz] += 1
    else:
        count[wyraz] = 1
#count = {w: wyrazy.count(w) for w in unique}

#zapis do pliku JSON
with open('docs/zaj01/zadanie_sprawdzające/wynik.json', 'w', encoding='utf-8') as file:
    json.dump(count, file, indent=4) 




