from os import getcwd
import czas
import time
import importlib

current_path = getcwd()

print(current_path)

print(czas.aktualny_czas)

time.sleep(2)

print(czas.aktualny_czas)

importlib.reload(czas)

print(czas.aktualny_czas)