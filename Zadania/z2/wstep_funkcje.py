def zmien_wartosc(arg):
    print("\nW funkcji - przed modyfikacją:", arg)
    
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652 
    
    print("W funkcji - po modyfikacji:", arg)

lista = [1, 2, 3]
print("Przed wywołaniem funkcji:", lista)
zmien_wartosc(lista)
print("Po wywołaniu funkcji:", lista)

liczba = 10
print("Przed wywołaniem funkcji:", liczba)
zmien_wartosc(liczba)
print("Po wywołaniu funkcji:", liczba)