# and, or y not

gas = True
encendido = True

# and valida que ambas condiciones sean ciertas
if gas and encendido:
    print('Todo Chido')

encendido = False
# or valida que al menos una de las condiciones sea cierta
if gas or encendido:
    print('Todo bien or')

# not nos cambia el valor bool de una variable a su contrario, es decir, convierte un false a true y viceversa
if gas and not encendido:
    print('Todo bien con el not')
