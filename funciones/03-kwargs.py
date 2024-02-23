# kwargs viene de keyword arguments
def get_product(**datos):
    print(datos)
    print(datos['id'], datos['nombre'])


# Al llamar a la funcion tenemos que indicarle el nombre del argumento que le vamos a dar
# Esto lo que nos muestra es un diccionario
get_product(id='id', nombre='iphone', desc='es un iphone')
