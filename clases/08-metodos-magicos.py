class Perro:
    # self hace referencia a la instancia de la clase, seria el equivalente al this de otros lenguajes

    def __init__(self, nombre, edad):
        self.nombre = nombre  # self.__propiedad vuelve privada a esa propiedad
        self.edad = edad

    def __str__(self):
        return f'clase Perro: {self.nombre}'

    def __del__(self):
        print(f'adios vaquero  {self.nombre}')

    # Todos los metodos y el constructor deben tener como primer parametro self
    def habla(self):
        print(f'{self.nombre} dice: wow')


perro = Perro('pedrito', 4)
print(perro)
del perro
