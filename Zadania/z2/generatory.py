def dni_tygodnia():
    dni = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    for dzien in dni:
        yield dzien

print("Wszystkie dni tygodnia:")
for dzien in dni_tygodnia():
    print(dzien)

print("\nPierwsze trzy dni tygodnia:")
count = dni_tygodnia()
print(next(count))
print(next(count))
print(next(count))

