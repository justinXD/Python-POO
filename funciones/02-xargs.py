# Al ponerle el * al nombre del parametro de la funcion le estamos diciendo que sera un iterable
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(5, 6, 8, 3, 7)
