'''
ESTO ES SOBRE ESCRIBIR UN METODO COMO LO HARIAMOS EN JAVA O C#
'''


class Ave:
    def __init__(self):
        self.volador = 'volador'

    def vuela(self):
        print('vuela ave')


class Pato(Ave):
    def __init__(self):
        super().__init__()  # mando llamar al constructor de la clase padre
        self.nada = 'nadador'

    def vuela(self):
        super().vuela()  # llamo a todos los metodos y propiedades de la clase padre con super()
        print('vuela pato')  # estoy sobre escribiendo el metodo vuela


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
