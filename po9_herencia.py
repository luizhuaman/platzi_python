# Un aspecto importantísimo de la Herencia es la posibilidad de reutilizar código. La reutilización es uno de los pilares de la POO, de manera que evitemos reinventar la rueda cada vez. Si tenemos un comportamiento que es común entre una serie de objetos de la misma categoría, este comportamiento debe enviarse a un clase superior que permita compartirlo con sus clases hijas. Esto facilita la mantenibilidad del código haciéndolo más estable.

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado = 5)
    print(cuadrado.area())