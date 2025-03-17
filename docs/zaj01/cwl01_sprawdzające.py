import json
import re
from collections import Counter

# Wczytanie pliku JSON jako słownik
with open("/app/geoapps-starter-2425-Kakucharz/docs/zaj01/teksty.json", "r", encoding="utf-8") as file:
    teksty = json.load(file)

# Funkcja do przekształcania wartości na tekst bo słowiniki to jakaś najczarniejsza z czarnych magii
def flatten_values(d):
    wynik = []
    for wartosc in d.values():
        if isinstance(wartosc, dict):
            wynik.extend(flatten_values(wartosc))  # Rekurencyjnie przetwarzamy zagnieżdżone słowniki (bo jest ich 4)
        elif isinstance(wartosc, list):
            wynik.extend(str(el) for el in wartosc if isinstance(el, (str, int, float)))
        elif isinstance(wartosc, (str, int, float)):
            wynik.append(str(wartosc))
    return wynik

# Połączenie wszystkich wartości w jeden tekst
polaczony_tekst = " ".join(flatten_values(teksty))

# Zamiana dużych liter na małe
polaczony_tekst = polaczony_tekst.lower()

# Usunięcie znaków interpunkcyjnych (kropek i przecinków)
polaczony_tekst = re.sub(r"[.,]", "", polaczony_tekst)

# Podział na wyrazy
wyrazy = polaczony_tekst.split()

# Ostatnia litera jako wielka litera
wyrazy = [w[:-1] + w[-1].upper() if len(w) > 0 else w for w in wyrazy]

# Usunięcie wyrazów bez "a"
wyrazy = [w for w in wyrazy if 'a' in w]

# Unikalne wyrazy
unikat = set(wyrazy)

# Wystąpienia słów
wystapienia = dict(Counter(wyrazy))

# Zapis do nowego pliku JSON
final = {
    "Unikaty": list(unikat),
    "Wystapienia": wystapienia
}

with open("final.json", "w", encoding="utf-8") as outfile:
    json.dump(final, outfile, ensure_ascii=False, indent=4)

print("Wynik zapisano do pliku final.json")
