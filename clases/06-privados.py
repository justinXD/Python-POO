class Perro:
    # self hace referencia a la instancia de la clase, seria el equivalente al this de otros lenguajes

    def __init__(self, nombre, edad):
        self.__nombre = nombre  # self.__propiedad vuelve privada a esa propiedad
        self.edad = edad

    # Todos los metodos y el constructor deben tener como primer parametro self
    def habla(self):
        print(f'{self.__nombre} dice: wow')

    def get_nombre(self):   # getter para obtener el nombre
        return self.__nombre

    # setter para el nombre, este lo hicimos un metodo privado, no se como acceder a este
    def __set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @classmethod
    def factory(cls):   # este metodo nos va aretornar una instancia nueva de la clase Perro, esto se llama factory method
        # le pasamos los argumentos que necesita la clase
        return cls('pepito', 5)


mi_perro = Perro.factory()
mi_perro.habla()
print(mi_perro.get_nombre())

print(mi_perro.get_nombre())
# esta linea da error porque nombre no es accecible desde fuera de la instancia
print(mi_perro.__nombre)
