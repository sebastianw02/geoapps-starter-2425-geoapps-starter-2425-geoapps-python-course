from docs.zaj01.moduly_przestrzenie.matematyka import odejmij

wynik = odejmij(10,4)
print(f'Wynik odejmowania: {wynik}')

x = 10  # Zmienna globalna

def funkcja():
    x = 5  # Zmienna lokalna
    print(f'Wartość x wewnątrz funkcji: {x}')

funkcja()
print(f'Wartość x na poziomie globalnym: {x}')

