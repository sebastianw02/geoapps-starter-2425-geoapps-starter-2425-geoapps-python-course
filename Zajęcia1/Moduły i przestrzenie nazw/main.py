# # Zajęcia 0
# import this

# # Przykład 1
# import matematyka

# wynik = matematyka.dodaj(5, 3)
# print(f'Wynik dodawania: {wynik}')

# from matematyka import odejmij
# wynik = odejmij(10, 4)
# print(f'Wynik odejmowania: {wynik}')

# x = 10  # Zmienna globalna

# def funkcja():
#     x = 5  # Zmienna lokalna
#     print(f'Wartość x wewnątrz funkcji: {x}')

# funkcja()
# print(f'Wartość x na poziomie globalnym: {x}')

# Zadanie 1
from os import getcwd
current_path = getcwd()
print("Wartość zmiennej current_path: " + current_path)