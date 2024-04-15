class Animal:
    def comer(self):
        print('comiendo')


class Perro:
    def pasear(self):
        print('pasear')


perro = Perro()
perro.pasear()


class Chancho(Perro, Animal):

    def programar(self):
        print('programando')


cerdito = Chancho()
cerdito.programar()
cerdito.comer()
