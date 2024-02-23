print('bienvenido a la alculadora')
print('Para salir escribe salir')
print('Las operasiones disponibles son suma, resta, multi y div')

resultado = ''
while True:
    if not resultado:
        resultado = input('Ingresa un Número: ')
        if resultado.lower() == 'salir':
            break
        resultado = int(resultado)
    op = input('Ingresa la operación: ')
    if op.lower() == 'salir':
        break
    n2 = input('Ingresa otro número: ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)

    if op.lower() == 'suma':
        resultado += n2
    elif op.lower() == 'resta':
        resultado -= n2
    elif op.lower() == 'multi':
        resultado *= n2
    elif op.lower() == 'div':
        resultado /= n2
    else:
        print('Operación invalida')
        break

    print(f'El resultado es {resultado}')
