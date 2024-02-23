for numero in range(5):
    print(numero)

# for con else, a esto se le conoce como for else
buscar = 8
for numero in range(5):
    print(numero)
    if numero == buscar:
        print('Encontrado: ', numero)
        break
else:
    print('No lo encontramos :(')
