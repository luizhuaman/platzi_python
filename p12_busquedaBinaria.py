# Lo aplicado en esta clase se denomina Métodos Numéricos, el metodo usado en la clase es conocido como método de la bisección, es un tipo de búsqueda incremental en el que el intervalo se divide siempre a la mitad.
# Existen diversos métodos que tiene una mejor convergencia para la aproximación a la solución, el mas conocido es el metodo newtoh raphson.

# Pueden revisar este libro si les interesa aprender mas sobre Métodos Numéricos
import time

objetivo = int(input('Escoge un numero: '))

inicio = time.time()
#144
epsilon = 0.001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2
num = 0

print(f'estra .... bajo={bajo}, alto={alto}, respuesta={respuesta}')

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        print(respuesta**2)
        print(objetivo)
        bajo = respuesta
    else:
        print(respuesta**2)
        print(objetivo)
        alto = respuesta

    respuesta = (alto + bajo) / 2
    num += 1

print(f'La raiz cuadrada de {objetivo} es {respuesta}')

fin = time.time()
print(f'Para resolver hizo {num} iteraciones y se demoro {fin - inicio} segundos\nInicio: {time.asctime(time.localtime(inicio))}\nFin: {time.asctime(time.localtime(fin))}')

# 16

# 0.001

# 0.0

# 16

# rpta 8


# raiz 8 - 16 = -8 +8 > 0.0
#     0   16    8
#     if raiz 8 < 16
#         bajo 8 
    
