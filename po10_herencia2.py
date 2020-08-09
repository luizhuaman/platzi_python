class PasapalosVenezolanos:

    def __init__(self, precio_unidad, numero_racion, relleno):
        self.precio_unidad = precio_unidad
        self.numero_racion = numero_racion
        self.relleno = relleno
    
    def precio_plato(self):
        return self.precio_unidad * self.numero_racion

class Arepa(PasapalosVenezolanos):

    def __init__(self, precio_unidad, numero_racion, relleno, tipo_de_preparacion, tipo_hmaiz):
        super().__init__(precio_unidad, numero_racion, relleno)
        self.tipo_de_preparacion = tipo_de_preparacion # horno, frita, asada
        self.tipo_hmaiz = tipo_hmaiz # harina de maiz blanco / amarilla
        print(f'El tipo de preparacion es {self.tipo_de_preparacion} , y el ingrediente principal es {self.tipo_hmaiz}')

class Tequeno(PasapalosVenezolanos):

    def __init__(self, precio_unidad, numero_racion, relleno, tipo_masa):
        super().__init__(precio_unidad, numero_racion, relleno)
        self.tipo_masa = tipo_masa # masa tradicional, masa cachapa

class Pastelito(PasapalosVenezolanos):

    def __init__(self, precio_unidad, numero_racion, relleno, tipo_salsa):
        super().__init__(precio_unidad, numero_racion, relleno)
        self.tipo_salsa = tipo_salsa # de ajo, rosada, picante, tartara

if __name__=='__main__':
    Venezolanos=Arepa(25,1.9,'carne','rustico','choclo')
    var = Venezolanos.precio_plato()
    print(f'El precio de la arepa es: {var}')

#super clase programador
class Programador:
    
    def __init__(self, nombre, edad, numero_de_empleado, skill):
        self.nombre = nombre
        self.edad = edad
        self.numero_de_empleado = numero_de_empleado 
        self.skill = skill

    def programar(self):
        print(f'Hola, soy {self.nombre}, tengo {self.edad}, y id_empleado es {self.numero_de_empleado} y me encanta orogramar en {self.skill}')

class ProgramadorJava(Programador):

    def __init__(self, nombre, edad, numero_de_empleado, skill = 'Java'):
        super().__init__(nombre, edad, numero_de_empleado, skill)

class ProgramadorPython(Programador):
    
    def __init__(self, nombre, edad, numero_de_empleado, skill = 'Python'):
        super().__init__(nombre, edad, numero_de_empleado, skill)

class ProgramadorCpp(Programador):

    def __init__(self, nombre, edad, numero_de_empleado, skill = 'C++'):
        super().__init__(nombre, edad, numero_de_empleado, skill)
    

def main():
    programador_java = ProgramadorJava('Ricardo', 25, 1234)
    programador_python = ProgramadorPython('Sofía', 20, 1345)
    programador_cpp = ProgramadorCpp('Gilberto', 35, 5637)

    programador_java.programar()
    programador_python.programar()
    programador_cpp.programar()


if __name__ == "__main__":
    main()