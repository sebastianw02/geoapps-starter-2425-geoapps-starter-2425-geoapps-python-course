import json
plik = open ("/app/Zajęcia1/Ćwiczenia sprawdzające/teksty.json", 'r')
odczyt = plik.read()
odczyt2 = json.loads(odczyt)
odczyt3 = ""
for i in range(5):
    odczyt3 = odczyt2["teksty"][i][f"tekst{i+1}"] + odczyt3
lower = odczyt3.lower()
lower = lower.replace(",", "")
lower = lower.replace(".", "")
lower = lower.split()

for n in range(len(lower)):
    lower[n] =  lower[n][:-1] + lower[n][-1].upper()

lowerBezA = [w for w in lower if w.lower().count("a")==0]

unik = list(set(lowerBezA))

ile = {}
for i in lower:
    ile.setdefault(i, 0)
    ile[i] += 1
print(ile)

slownik = {"Tekst" : lower, "Wyrazy" : unik, "Zliczenia" : ile}
with open("/app/Zajęcia1/Ćwiczenia sprawdzające/nowyTekst.json", "w") as f: 
    json.dump(slownik, f)
plik.close()