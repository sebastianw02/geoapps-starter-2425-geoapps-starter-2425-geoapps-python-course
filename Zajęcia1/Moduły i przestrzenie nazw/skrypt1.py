import czas
print(czas.aktualny_czas)

import time
time.sleep(20)
print(czas.aktualny_czas)

import importlib
importlib.reload(czas)
print(czas.aktualny_czas)

# Wartość zmiennej aktualny_czas zmieniła się dopiero po przeładowaniu modułu.
# Zmienna aktualny_czas jest inicjowana w pliku czas.py