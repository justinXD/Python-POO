mascotas = ['copito', 'max', 'cochi', 'pelusa']

for mascota in enumerate(mascotas):
    # enumerate nos retorna una tupla, para este caso el print daria (0, 'copito)...
    print(mascota)

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
