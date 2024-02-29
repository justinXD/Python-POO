usuarios = [['chicharito', 4], ['vega', 2], ['pepe', 8]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

# Comprension de listas
# map
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# filter
nombre = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombre)

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
