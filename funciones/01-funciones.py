# Al darle al segundo parametro un valor por defecto le decimos a python que el segundo parametro es opcional
# Si le pasamos el segundo argumento al ejecutar la funcion este no tendra su valor por defecto
def hola(nombre, apellido=''):
    print('Hola mundo')
    print(f'bienvenido {nombre} {apellido}')


hola('Papucho')

# Puedo tambien nombrar los argumentos al ejecutar la funcion
hola(apellido='sabroso', nombre='viejo')
