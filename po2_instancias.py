
class Coordenada:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))


class Persona:

    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

    defpregunta_edad(self, otra_persona):
        if self.edad > otra_persona.edad:
            return f'Soy mayor que tú, tengo {self.edad} años.'
        else:
            return f'Soy menor que tú, tengo {self.edad} años.'

    def saludar(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

if __name__ == '__main__':

    mi_nombre = input('Mi nombre es: ')
    mi_edad = int(input('Mi edad es: '))
    nombre_persona = input('¿Cual es tu nombre? ')
    edad_persona = int(input('¿Cual es tu edad? '))

    otra_persona = Persona(edad_persona , nombre_persona)
    yo_persona = Persona(mi_edad , mi_nombre)

    print(yo_persona.saludar(otra_persona))
    print(yo_persona.pregunta_edad(otra_persona))


class Teorema_pitagoras(object):

    """Esta clase hace uso del teorema de pitagoras para calcular
     la hipotenusa alrededor de difererentes catetos"""

    def __init__(self, cateto_1, cateto_2):
        self.cateto_1 = cateto_1
        self.cateto_2 = cateto_2

    def calculo_hipotenusa(self):
        hipotenusa = ((self.cateto_1**2)+(self.cateto_2**2))**0.5
        return hipotenusa

if __name__ == '__main__':

    cateto = int(input('¿Cual es el valor del cateto 1? '))
    cateto_2 = int(input('¿Cual es el valor del cateto 2? '))
    resultado_1 = Teorema_pitagoras(cateto, cateto_2)

    print('El valor de la hipotenusa es ', resultado_1.calculo_hipotenusa())

    bonus = input('¿Quieres saber como te ira en el amor? ')
    genero = input('¿Eres hombre o mujer? ')

    if genero == 'hombre'and bonus=='si':
        print('Ella no te ama')

    elif genero == 'mujer'and bonus == 'si':
        print('Él no te ama')

    else:
        print('Que persona tan amargada eres')
