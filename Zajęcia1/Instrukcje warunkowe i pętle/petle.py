#zadanie 1
imiona = {"Michał", "Jakub", "Maria", "Iwona", "Marcin"}
for i, imie in enumerate(imiona):
    print(f"{i}) {imie}")

#zadanie 2
a = float(input("Wprowadź swoją liczbę: "))
if a % 2 == 0 and a > 0:
    print("Liczba jest parzysta i dodatnia")

if a != 0:
    print("Liczba jest różna od zera")

b = input("Wprowadź szukany owoc: ")
owoce = {"jabłko", "banan", "pomarańcza", "grejfrut"}
if b in owoce:
    print("Owoc jest dostępny")

#zadanie 3
suma = 0; i = 0
while suma < 100:
    c = int(input("Wprowadź liczbę do sumy: "))
    suma = suma + c
    i += 1
print(f"Suma wyniosła {suma}, po {i} iteracjach")
