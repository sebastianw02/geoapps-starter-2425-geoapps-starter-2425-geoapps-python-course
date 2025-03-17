#-----------------------1
imiona = ["Zuzia", "Józia", "Kasia", "Eufremia"]

for imie in enumerate(imiona):
    print(imie)

#-----------------------2
liczba = -2

if liczba % 2 == 0 and liczba > 0:
    print(f"Liczba {liczba} jest dodatnia parzysta :)")
else:
    print("WARUNEK NIESPEŁNIONY JEZUS")

if liczba != 0:
    print(f"Liczba jest różna od 0")


owoc = 'banan '
lista_owocow = ['jabłko', 'banan', 'pomarańcza']

if owoc in lista_owocow:
    print("Owoc jest dostępny")
else:
    print("Owocu nie ma na liście")

#-----------------------3

wynik = 0

while wynik <= 100:
    try: 
        plus = float(input("Wprowadź liczbe: "))
        wynik += plus
    except:
        print("Nie wprowadzono liczby!")

print(f"Suma wprowadzonych liczb: {wynik}")
