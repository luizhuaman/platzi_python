OPCION = "-abcdefghijklm"

#RECORRER STRING
for letra in OPCION:
    print ("Opcion {} ".format(letra.upper()))

entrada = input('Ingresa tu opcion : ')

print("El indice de la opcion que elegiste, es el siguiente: {}".format(OPCION.rfind(entrada.lower())))

#RFIND() PARA TRAER EL INDICE DE INPUT
if OPCION.rfind(entrada.lower()) == 13:
    print('Lo logre, entro a la condicion, marcaste M')

#CONTINUE AND BREAK
for i in range(1,14):
    if entrada == OPCION[i]:
        break
    if OPCION[i] == OPCION[2]:
        continue
    print(OPCION[i].upper())

cadenda_texto = "Luis"

cadenda_texto = cadenda_texto*2

print(cadenda_texto)

