mascotas = ['copito', 'max', 'cochi', 'pelusa']

# Accediendo a un elemento de la lista
print(mascotas[2])

# manipulamos una posicion de la lista
mascotas[3] = 'bicho'

# Accediendo a un rango de la lista, puede ser tambien [:3] o [0:]
print(mascotas[0:3])

# Accedemos al ultimo elemento
print(mascotas[-1])

# Accediendo a los indices pares
print(mascotas[::2])

numeros = list(range(21))
print(numeros[::2])
print(numeros[1::2])
