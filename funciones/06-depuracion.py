def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print('antes de la funcion')
l = largo('hola mundo')
print(l)
