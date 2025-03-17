#-----------for--------
imiona = ['Anna', 'Barbara', 'Celina', 'Dorota', 'Elzbieta']

for indeks, imie in enumerate(imiona):
    print(f'Indeks {indeks}: {imie}')

#-------------if----------------
a = int(input("Podaj liczbe: "))
if a > 0 and a % 2 == 0:
    print("Liczba jest dodatnia i parzysta")

b = int(input("Podaj liczbe: "))
if b != 0:
    print("Liczba jest różna od 0")

owoce = ['jablko', 'banan', 'pomarancza']
c = str(input("Podaj owoc: "))
if c in owoce:
    print("Owoc jest dostepny")


#--------------while-----------------
suma = 0
while suma <= 100:
    d = int(input('Podaj liczbe: '))
    suma = suma + d

print('Koniec! Suma wprowadzonych liczb:', suma)