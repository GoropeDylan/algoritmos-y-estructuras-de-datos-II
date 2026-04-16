from abc import ABC, abstractmethod
#CLASE BASE FIGURA
class Figura():
    def __init__(self,color):
        self.color = color
    def area(self):
        return 0
    def describir(self):
        print(f'color: {self.color}')
#CLASE HIJA RECTANGULO QUE HEREDA DE FIGURA
class Rectangulo(Figura):
    def __init__(self, color,base,altura):
        super().__init__(color)
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
#CLASE HIJA CIRUCLO QUE HEREDA DE FIGURA    
class Circulo(Figura):
    def __init__(self, color,radio):
        super().__init__(color)
        self.radio = radio
    def area(self):
        return 3.1416*self.radio**2
    
#FUNCION PRINCIPAL
lista = [Rectangulo('Rojo',7,4),Rectangulo('Naranja',10,2),Circulo('Azul',3),Circulo('Verde',1)]
#MOSTRANDO AREA 
for i in lista:
    print(i.area())
#COLOR
for i in lista:
    i.describir()