class Animal:
    def comer(self):
        print('comiendo')


class Perro(Animal):
    def pasear(self):
        print('pasear')


perro = Perro()
perro.comer()
perro.pasear()


class Chancho(Animal):

    def programar(self):
        print('programando')


cerdito = Chancho()
cerdito.programar()
cerdito.comer()
