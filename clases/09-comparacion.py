class Coordenadas:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

    def __eq__(self, otro):  # metodo magico para comparar dos objetos
        return self.latitud == otro.latitud and self.longitud == otro.longitud

    def __ne__(self, otro):  # otro metodo magico para comparar dos objetos, este es not equal
        return self.latitud != otro.latitud or self.longitud != otro.longitud

    def __lt__(self, otro):  # otro metodo magico para comparar dos objetos, este es lower than
        return self.latitud + self.longitud < otro.latitud + otro.longitud

    def __le__(self, otro):  # otro metodo magico para comparar dos objetos, este es lower or equal than
        return self.latitud + self.longitud <= otro.latitud + otro.longitud


coords = Coordenadas(44, 27)
coords2 = Coordenadas(45, 27)

print(coords == coords2)
print(coords != coords2)
print(coords > coords2)
