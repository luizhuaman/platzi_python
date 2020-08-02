import time

tiempo_inicial = time.time()
objetivo = None

while objetivo == None:
    objetivo_string = input('Ingresa un número que quieras saber su raíz cuadrada: ')
    if(objetivo_string.isdigit()):
        objetivo = int(objetivo_string)

resultado = 0
while resultado**2 < objetivo:
    resultado += 1
    if resultado**2 == objetivo:
        base = resultado
        break

if resultado**2 == objetivo:
    print(f'raiz cuadrada de {objetivo} es {resultado}')
else:
    print(f'No existe una raíz exacta de {objetivo}')
print(f'El programa demoró {time.time() - tiempo_inicial} segundos ')