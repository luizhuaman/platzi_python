
import time

def validarNumero():
    objetivo = None

    while objetivo == None:
        objetivo_string = input('Ingresa un número que quieras saber su raíz cuadrada: ')
        if(objetivo_string.isdigit()):
            objetivo = int(objetivo_string)
            return objetivo
        else: print('ERROR: Ingresa un numero entero por favor:')
    
def raiz_cuadrada_normal():

    objetivo = validarNumero()
    tiempo_inicial = time.time()
    resultado = 0

    while resultado**2 < objetivo:
        resultado += 1
        if resultado**2 == objetivo:
            break

    if resultado**2 == objetivo:
        print(f'raiz cuadrada de {objetivo} es {resultado}')
    else:
        print(f'No existe una raíz exacta de {objetivo}')
    print(f'El programa demoró {time.time() - tiempo_inicial} segundos ')


def aproximacion():
    
    objetivo = validarNumero()
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    tiempo_inicio = time.time()

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    tiempo_total = time.time() - tiempo_inicio

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada del objetivo')
        print(f'Tardo {tiempo_total} segundos')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        print(f'Tardo {tiempo_total} segundos')


def busqueda_binaria():

    objetivo = validarNumero()
    inicio = time.time()
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    num = 0

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
        num += 1

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    fin = time.time()
    print(f'Para resolver hizo {num} iteraciones y se demoro {fin - inicio} segundos\nInicio:   {time.asctime(time.localtime(inicio))}\nFin: {time.asctime(time.localtime(fin))}')

def run():
    punto_acceso = 0
    while True:
        try:
            while True:
                menu = """ Encuentra la raiz cuadrada 💰

                [1] - Busqueda Normal
                [2] - Busqueda Binaria
                [3] - Busqueda Aproximada
                [0] - Salir

                Elije una opciones : """

                opcion = int(input(menu))

                #Validar Opcion
                if opcion >= 0 and opcion <=3:
                    print('Opcion Correcta')
                    break
                else:
                    print('* * * * * * E R R O R * * * * * *')
                    print('Por favor, Ingresa solo valores del Menu')

            #Acciones del Menu     
            if opcion == 0:
                punto_acceso = 1    
                print('Bye bye, vuelve pronto!')
            elif opcion == 1:
                        raiz_cuadrada_normal()
            elif opcion == 2:
                busqueda_binaria()
            else:
                aproximacion()

        except:
            print('* * * * * * E R R O R * * * * * *')
        if(punto_acceso == 1):
            break

if __name__ == '__main__':
    try:
        run()
    except:
        run()