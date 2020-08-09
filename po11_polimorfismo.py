class Persona:

    def __init__(self, nombre):
        self.nombre =  nombre

    def avanza(self):
        print('Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando montando Bici')

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniela')
    ciclista.avanza()

if __name__ == '__main__':
    main()

class Persona2:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property
    def getNombre(self):
        return self.nombre
    def avanza(self):
        print(' está caminando')
    
class Ciclista2(Persona2):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print(' está moviéndose en bicicleta')

def main2():
    persona = Persona2('David')
    print(f'{persona.getNombre}:') 
    persona.avanza()

    ciclista = Ciclista2('Eugenia')
    print(f'{ciclista.getNombre}:') 
    ciclista.avanza()

if __name__ == '__main__':
    main2()