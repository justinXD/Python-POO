class Perro:
    # self hace referencia a la instancia de la clase, seria el equivalente al this de otros lenguajes
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Todos los metodos y el constructor deben tener como primer parametro self
    def habla(self):
        print(f'{self.edad} wow')


mi_perro = Perro('pancho', 4)
print(mi_perro.nombre)
mi_perro.habla()
