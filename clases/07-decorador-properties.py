class Perro:
    # self hace referencia a la instancia de la clase, seria el equivalente al this de otros lenguajes

    def __init__(self, nombre):
        self.nombre = nombre

    # este decorador indica que el metodo mencionado abajo es un getter y oculta la propiedad nombre del autocompletado
    @property
    def nombre(self):
        return self.__nombre

    # decorador que indica que el metodo de abajo es el setter
    @nombre.setter
    def nombre(self, nombre):
        if nombre.stip():
            self.__nombre = nombre
