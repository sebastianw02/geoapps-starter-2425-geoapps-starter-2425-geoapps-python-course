import time
from functools import wraps

def mierzenie_czasu(unit='seconds'):
    def dekorator(funkcja):
        @wraps(funkcja)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            wynik = funkcja(*args, **kwargs)
            koniec = time.perf_counter()
            czas = koniec - start

            if unit == 'microseconds':
                czas *= 1000000
                jednostka = 'μs'
            else:
                jednostka = 's'

            print(f"Czas wykonania: {czas:.2f} {jednostka}")
            return wynik
        return wrapper
    return dekorator


@mierzenie_czasu(unit='microseconds')
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    wartosc = cena * ilosc
    tekst = f"Zamowiono: {nazwa_produktu}, ilosc: {ilosc}, laczna cena: {wartosc:.2f} zl"
    return tekst, wartosc



print(zamowienie_produktu("Laptop", cena=4000, ilosc=3))