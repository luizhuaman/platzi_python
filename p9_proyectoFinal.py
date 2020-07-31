import random
import string

# La función choice(secuencia) elige un valor al azar en un conjunto de elementos. Cualquier tipo de datos enumerable (tupla, lista, cadena, range) puede utilizarse como conjunto de elementos.
# La función join convierte una lista en una cadena formada por los elementos de la lista separados por comas.

def generar_contrasena():
    #mayusculas = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    #minusculas = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es : '+ contrasena)

if __name__ == '__main__':
    run()