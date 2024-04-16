from abc import ABC, abstractmethod


class Model(ABC):

    def __init__(self):
        if not self.tabla:
            print('Error, tienes que definif una tabla')

    @property
    @classmethod
    def tabla(self):
        pass

    def guardar(self):
        print(f'Guardando {self.tabla} en BBDD')

    @abstractmethod
    def metodo_abs(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f'Buscando por id {_id} en la tabla {self.tabla}')


class Usuario(Model):
    tabla = 'Usuario'

    def metodo_abs(self):
        print('Metodo abstracto')


usuario = Usuario()
usuario.guardar()
usuario.metodo_abs()
Usuario.buscar_por_id(123)
