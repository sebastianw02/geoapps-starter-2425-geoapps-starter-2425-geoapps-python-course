imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]

print("Przypadek gdy listy są równej długości:")
for imie, ocena in zip(imiona, oceny):
    print(f"{imie}: {ocena}")

imiona_dluzsze = ['Anna', 'Jan', 'Ewa', 'Krzysztof']
oceny_krotsze = [5, 4]

print("\nPrzypadek gdy listy są różnej długości:")
for imie, ocena in zip(imiona_dluzsze, oceny_krotsze):
    print(f"{imie}: {ocena}")  #Wyswietla tylko dwie pierwsze pary, ignoruje reszte


liczby = [1, 2, 3, 4, 5]

def kwadrat(x):
    return x ** 2

kwadraty = list(map(kwadrat, liczby))

print(f"Oryginalna lista: {liczby}")
print(f"Kwadraty liczb: {kwadraty}")