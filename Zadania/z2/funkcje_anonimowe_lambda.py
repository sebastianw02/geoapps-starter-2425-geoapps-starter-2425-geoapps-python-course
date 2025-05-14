ksiazki = [
    {"tytul": "Władca Pierścieni", "autor": "J.R.R. Tolkien", "rok_wydania": 1954},
    {"tytul": "Harry Potter i Kamień Filozoficzny", "autor": "J.K. Rowling", "rok_wydania": 1997},
    {"tytul": "Duma i uprzedzenie", "autor": "Jane Austen", "rok_wydania": 1813},
    {"tytul": "Rok 1984", "autor": "George Orwell", "rok_wydania": 1949},
    {"tytul": "Zbrodnia i kara", "autor": "Fiodor Dostojewski", "rok_wydania": 1866},
    {"tytul": "Mistrz i Małgorzata", "autor": "Michaił Bułhakow", "rok_wydania": 1967},
    {"tytul": "Hobbit", "autor": "J.R.R. Tolkien", "rok_wydania": 1937},
    {"tytul": "Sto lat samotności", "autor": "Gabriel García Márquez", "rok_wydania": 1967},
    {"tytul": "Imię róży", "autor": "Umberto Eco", "rok_wydania": 1980},
    {"tytul": "Solaris", "autor": "Stanisław Lem", "rok_wydania": 1961},
]

ksiazki_posortowane = sorted(ksiazki, key=lambda x: x['rok_wydania'])

print("Ksiazki posortowane wedlug roku wydania:")
for ksiazka in ksiazki_posortowane:
    print(f"{ksiazka['rok_wydania']}: {ksiazka['tytul']}")

ksiazki_po_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, ksiazki))

print("\nKsiazki wydane po 2000 roku:")
if ksiazki_po_2000:
    for ksiazka in ksiazki_po_2000:
        print(f"{ksiazka['tytul']} ({ksiazka['rok_wydania']})")
else:
    print("Brak ksiazek wydanych po 2000 roku")

tytuly_ksiazek = list(map(lambda x: x['tytul'], ksiazki))

print("\nLista tytulow ksiazek:")
for tytul in tytuly_ksiazek:
    print(tytul)