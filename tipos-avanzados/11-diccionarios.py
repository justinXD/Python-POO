punto = {"x": 25, 'y': 50}    # diccionario, parecido a un objeto en JS

print(punto)
print(punto['x'])
print(punto['y'])

punto['z'] = 45  # agregamos nueva propiedad
print(punto)

print(punto.get('x'))
print(punto.get('a'))   # retorna None para a
print(punto.get('a'), 10)   # valor por defecto de a

# tambien podemos usar el metodo del

# iteramos con un for
# devuelve las llaves
for valor in punto:
    print(valor, punto[valor])

# devuelve el valor en forma de tupla
for valor in punto.items():
    print(valor)

# devuelve el valor
for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {'id': 1, 'Nombre': 'copito'},
    {'id': 2, 'Nombre': 'max'},
    {'id': 3, 'Nombre': 'cochi'},
    {'id': 4, 'Nombre': 'prieta'}
]

for usuario in usuarios:
    print(usuario['Nombre'])
