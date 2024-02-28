numeros = [1, 2, 3]

# Funciona pero no es lo mejor
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# Obteniendo solo el primer elemento, y los demas quedaran en una lista
primero, *otros = numeros
print(primero, otros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, ultimo = numeros
print(primero, segundo, otros, ultimo)
