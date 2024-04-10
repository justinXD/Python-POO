class Perro:
    # self hace referencia a la instancia de la clase, seria el equivalente al this de otros lenguajes
    patas = 4  # propiedad que sera la misma para todas las instancias de la clase Perro, a menos que yo la modifique en cada instancia

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Todos los metodos y el constructor deben tener como primer parametro self
    @classmethod  # el decorador Classmethod hace que el metodo sea propio de la clase y no de la instancia
    def habla(cls):  # cls hace referencia a la clase misma
        print('wow')

    @classmethod
    def factory(cls):   # este metodo nos va aretornar una instancia nueva de la clase Perro, esto se llama factory method
        # le pasamos los argumentos que necesita la clase
        return cls('pepito', 5)


Perro.habla()
mi_perro = Perro.factory()
mi_perro.habla()
