from functools import reduce

def app(lista):
    numerosImpares = list(filter((lambda x: x % 2 == 1), lista))
    print(numerosImpares)
    suma = reduce((lambda x, y: x + y), numerosImpares)
    print(suma)

lista = list(range(100))

app(lista)