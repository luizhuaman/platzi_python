class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4) #esto es una  variable privada, por eso se empieza con _
        self._seguridad = AirBag ()
    
    def encender(self):
        self._motor.temperatura(30)
        print("\n")
        print(f"El auto encendio y empieza con 30 grados de temperatura")

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
            self._motor.temperatura(12)
        else:
            self._motor.inyecta_gasolina(3)
            self._motor.temperatura(7)

        self._estado = 'En_movimiento'
    
    def desAcelerar(self, tipo='lenta' ):

        if tipo == "brusca":
            print(f'el auto esta tenienedo una desaceleracion {tipo}')
            self._seguridad.activar()
            self._seguridad.infoAirbag()
        else:
            print(f'el auto esta tenienedo una desaceleracion {tipo}')
            self._seguridad.infoAirbag()
            self._estado = 'en_reposo'
    
    def info(self):#Esta funcion es temporal, solo para revisar que todo esta funcionanndo :v xd 
        print("\n")
        print(f"Modelo = {self.modelo}, marca = {self.marca} y color = {self.color}, {self._estado}")
        print("\n")
       
    def girar(self,direccion_de_giro:str):
            print("\nGirando a la {}".format(direccion_de_giro))
    


class Motor:

    def __init__(self, cilindros, tipo='gasolina', nivelGasolina = 46000, temperatura = 0 ):#tipo es un parametro ya definido, se le llama default keyword, se entiende comoo un parametro por defecto.
        self.cilindros = cilindros
        self.tipo = tipo
        self.nivelGasolina = nivelGasolina
        self.estadoTemperatura = temperatura

    def inyecta_gasolina(self, cantidadGasolina):
        self.nivelGasolina = self.nivelGasolina - cantidadGasolina
    
    def temperatura(self, grados ):
        self.estadoTemperatura = self.estadoTemperatura + grados

    def informacion(self):#Esta funcion es temporal, solo para revisar que todo esta funcionanndo :v xd 
        print("\n")
        print(f"nivelGasolina = {self.nivelGasolina} y temperatura = {self.estadoTemperatura}")
        print("\n")

class AirBag:

    def __init__(self, estado = "optimo"):
        self.estado = estado

    def activar(self):
        print("SISTEMA DE SEGURAD DE CHOQUES ACTIVADO")
        self.estado = "inhalitado"
    
    def infoAirbag(self):#Esta funcion es temporal, solo para revisar que todo esta funcionanndo :v xd 
        print("\n")
        print(f"Estado del Airbag: {self.estado}")
        print("\n")

if __name__ == "__main__":

    car1 = Automovil("AAFF","toyota", "rojo")
    car1.encender()
    car1.girar('izquierda')
    car1.info()
    car1._motor.informacion() 
    car1.acelerar("rapida")
    car1.info()
    car1._motor.informacion()
    car1.desAcelerar()
    car1.info()
    
print("\n\n")