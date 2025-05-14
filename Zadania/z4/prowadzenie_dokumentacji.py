def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    """
    Funkcja oblicza wartość zamówienia produktu i generuje opis zamówienia.

    Args:
        nazwa_produktu (str): Nazwa zamawianego produktu.
        cena (float): Cena jednostkowa produktu.
        ilosc (int, optional): Ilość zamawianego produktu. Domyślnie 1.

    Returns:
        Krotka zawierająca:
            - str: Tekst opisujący zamówienie w formacie:
                   "Zamowiono: [nazwa_produktu], ilosc: [ilosc], laczna cena: [wartosc] zł"
                   gdzie wartość jest formatowana do 2 miejsc po przecinku.
            - float: Łączna wartość zamówienia (cena * ilosc).

    Example:
        >>> (zamowienie_produktu("Laptop", cena=4000, ilosc=3)
        ('Zamowiono: Laptop, ilosc: 3, laczna cena: 12000 zl)

    Note:
        Parametry 'cena' i 'ilosc' muszą być podane jako argumenty nazwane (keyword arguments).
    """
    wartosc = cena * ilosc
    tekst = f"Zamowiono: {nazwa_produktu}, ilosc: {ilosc}, laczna cena: {wartosc:.2f} zl"
    return tekst, wartosc



zamowienie_produktu()