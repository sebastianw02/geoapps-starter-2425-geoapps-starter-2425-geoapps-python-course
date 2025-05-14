dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print(f"rok: {rok}, jezyk: {jezyk}, wersja: {wersja}\n")

oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(f"pierwsza: {pierwsza}, srodek: {srodek}, ostatnia: {ostatnia}\n")

info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, _, _, zawod = info
print(f"imie: {imie}, nazwisko: {nazwisko}, zawod: {zawod}\n")

dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok, (jezyk, wersja, (opis, _)) = dane
print(f"rok: {rok}, jezyk: {jezyk}, wersja: {wersja}, opis: {opis}")