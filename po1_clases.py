#defino mi lista
alumnado = []

#defino una clase Alumno
class Alumno: 
# se inicia el constructor de instancias y propiedades de instancia
    
    def __init__(self, id_alumno, nombre, grado, alumnos):
        self.id_alumno = id_alumno      #incializo variables de instancia
        self.nombre = nombre            
        self.grado = grado            
        self.alumnos = alumnos
    
    def agregar(self, id_alumno, nombre, grado, alumnos):

        new_item = {
		    "id_alumno": id_alumno, 
		    "nombre": nombre,
		    "grado": grado
		    }

        self.alumnos.append(new_item)
        print('El Alumno ingresado es: ')
        print(
		    "\tid_alumno: ", id_alumno, "\n",
		    "\tnombre: ", nombre, "\n",
            "\tgrado: ", grado, "\n",
		    		)


    def mostrar(self, alumnos):    

        if len(alumnos) == 0:
            print('No existen alumnos en la lista')
        else:
            i = 0
            for dictionary in alumnos:
                i += 1
                print(f"Alumno #{i} :")
                print(
		    		"\tid_alumno: ", dictionary["id_alumno"], "\n",
		    		"\tnombre: ", dictionary["nombre"], "\n",
                    "\tgrado: ", dictionary["grado"], "\n",
		    		)
    
    def borrar(self, alumnos):
        OpcionBorrar = int(input('Ingrese el alumno a borrar: '))-1
        del alumnos[OpcionBorrar]

         
def Menu():

    while True:

        command = str(input('''
            ¿Que deseas hacer?

            [a]Añadir Alumno
            [b]Mostrar Alumnos
            [c]Eliminar Alumnos
            [s]Salir
        '''))

        alumnos = alumnado
        id_alumno = ''
        nombre = ''
        grado = ''
        matricular = Alumno(id_alumno,nombre,grado,alumnos)

        if  command.lower() == 'a':
            id_alumno = str(input('Escribe la identificacion del Alumno : '))
            nombre = str(input('Escribe el nombre del Alumno : '))
            grado = str(input('Escribe el grado academico: '))
            print('')
            matricular.agregar(id_alumno,nombre,grado,alumnos)

        elif command.lower() == 'b':
            matricular.mostrar(alumnos)

        elif command.lower() == 'c':
            matricular.borrar(alumnos)

        elif command.lower() == 's':
            break
        else:
            print('Comando no encontrado.')

if __name__ == '__main__':
    print()
    print('B I E N V E N I D O  A L  S I S T E M A  D E   M A T R I C U L A S')
    Menu()