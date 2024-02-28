mascotas = ['copito', 'max', 'cochi', 'pelusa']

print(mascotas.index('max'))

# Si lo que buscamos no existe el metodo index nos devolvera un error
# Esto lo podemos evitar validando si existe primero

if 'guapo' in mascotas:
    print(mascotas.index('guapo'))
