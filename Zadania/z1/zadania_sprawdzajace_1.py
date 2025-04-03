import json
import re
from collections import Counter

# Wczytanie danych z pliku teksty.json
with open("teksty.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Połączenie wszystkich tekstów w jeden ciąg znaków
tekst = " ".join([entry[key] for entry in data["teksty"] for key in entry])

# Zamiana wszystkich dużych liter na małe
tekst = tekst.lower()

# Podział na wyrazy i usunięcie znaków interpunkcyjnych
wyrazy = re.findall(r'\b\w+\b', tekst)

# Modyfikacja każdego wyrazu - ostatnia litera wielka
wyrazy = [w[:-1] + w[-1].upper() if len(w) > 1 else w.upper() for w in wyrazy]

# Usunięcie wyrazów bez 'a' lub 'A'
wyrazy = [w for w in wyrazy if 'a' in w.lower()]

# Stworzenie zbioru unikalnych wyrazów
unikalne_wyrazy = set(wyrazy)

# Zliczenie wystąpień każdego wyrazu
licznik_wyrazow = Counter(wyrazy)

# Zapis do pliku JSON
wynik = {
    "unikalne_wyrazy": list(unikalne_wyrazy),
    "licznik_wyrazow": licznik_wyrazow
}

with open("wynik.json", "w", encoding="utf-8") as file:
    json.dump(wynik, file, ensure_ascii=False, indent=4)