mascotas = ['copito', 'max', 'cochi', 'pelusa', 'pulga', 'guapo', ' romeo']

# Insertamos un nuevo elemento a la lista en el indice indicado
mascotas.insert(1, 'savina')
print(mascotas)

# Insertamos un nuevo elemento al final de la lista
mascotas.append('prieta')
print(mascotas)

# Eliminamos un elemento de la lista, solo elimina la primera coincidencia, no funciona si queremos eliminar el ultimo elemento
mascotas.remove('pelusa')
print(mascotas)

# Elimina el utimo elemento de la lista
mascotas.pop()  # Podemos pasarle un indice para que borre el elemento almacenado en ese indice
print(mascotas)

# tambien podemos usar del para eliminar elementos de una lista dandole el indice
del mascotas[2]
print(mascotas)

# Limpiamos la lista
mascotas.clear()
print(mascotas)
