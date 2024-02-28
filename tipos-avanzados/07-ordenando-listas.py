numeros = [5, 9, 7, 523, 556, 22, 78]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

# sorted devuelve una nueva lista
numeros2 = sorted(numeros, reverse=True)
print(numeros2)


usuarios = [[4, 'chicharito'], [2, 'vega'], [8, 'pepe']]
usuarios.sort()
print(usuarios)

# aqui no se va a ordenar bien porque el incide no esta en la primera posicion de la lista
usuarios = [['chicharito', 4], ['vega', 2], ['pepe', 8]]
usuarios.sort()
print(usuarios)


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)
