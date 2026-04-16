from abc import ABC, abstractmethod
#CLASE BASE VEHICULO
class Vehiculo():
    def __init__(self,marca,vel_max):
        self.marca = marca
        self.vel_max = vel_max
    def describir(self):
        pass
#CLASE AUTO, HEREDA DE VEHICULO
class Auto(Vehiculo):
    def __init__(self, marca, vel_max):
        super().__init__(marca, vel_max)
    def describir(self):
        print(f'''Marca: {self.marca}
velocidad máxima: {self.vel_max}''')
#CLASE MOTO, HEREDA DE VEHICULO       
class Moto(Vehiculo):
    def __init__(self, marca, vel_max):
        super().__init__(marca, vel_max)
    
    def describir(self):
        print(f'''Marca: {self.marca}
velocidad máxima: {self.vel_max}''')

#--------------------------------FUNCION MAIN------------------------------------
#CREO UNA LISTA DE OBJETOS
lista = [Auto("Alfa romeo",250),Auto("Fiat",300),Moto("Honda",150),Moto("Dominar",400)]
#BUCLE FOR
for i in lista:
    i.describir() #POLIMORFISMO