import random

def sort_burbuja(lista, contador=0, contador2=0):
    n = len(lista)
    

    for i in range(n):
        for j in range(0, n -i - 1): # O(n) * O(n) = O(n**2) cuadratica
            contador2 += 1
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                contador += 1
    
    return lista, contador, contador2


if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño sera la lista? : '))
    
    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    
    lista_ordenada,contador, contador2 = sort_burbuja(lista)
    print(f'Pasos contador: {contador} y contador2: {contador2}')
    print(lista_ordenada)