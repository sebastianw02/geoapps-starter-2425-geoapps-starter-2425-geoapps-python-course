def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    wartosc = cena * ilosc
    tekst = f"Zamowiono: {nazwa_produktu}, ilosc: {ilosc}, laczna cena: {wartosc:.2f} zł"
    return tekst, wartosc

zamowienia = []

zamowienia.append(zamowienie_produktu("Laptop", cena=4000, ilosc=3))
zamowienia.append(zamowienie_produktu("Telefon", cena=2500, ilosc=1))
zamowienia.append(zamowienie_produktu("Sluchawki", cena=400)) 

print("Lista zamowień:")
for zamowienie in zamowienia:
    print(zamowienie[0])

suma = sum(zamowienie[1] for zamowienie in zamowienia)
print(f"\nLaczna wartosc zamowien: {suma:.2f} zl")