import czas
print(czas.aktualny_czas)

import time
time.sleep(2)
print(czas.aktualny_czas)

import importlib
importlib.reload(czas)
print(czas.aktualny_czas)