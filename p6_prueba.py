OPCION = "-abcdefghijklm"
entrada = input('Ingresa tu opcion : ')
print(OPCION.rfind(entrada.lower()))
if OPCION.rfind(entrada.lower()) == 13:
    print('Lo logre, entro a la condicion')

#validando opcion
for i in range(1,14):
    print(OPCION[i])
    if entrada == OPCION[i]:
        break