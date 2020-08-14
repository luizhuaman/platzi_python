#En la busqueda binaria la lista debe estar ordenada.

import random

def busqueda_lineal(lista, objetivo,iter_lin=0):
    match = False

    for elemento in lista:
        iter_lin+=1
        if elemento == objetivo:
            match = True
            break

    return (match,iter_lin)

def busqueda_binaria(lista, comienzo, final, objetivo,iter_bin=0):
    print(f'Buscando {objetivo} entre lista({comienzo}):{lista[comienzo]} y lista({final-1}):{lista[final-1]}')
    iter_bin+=1
    if comienzo > final:
        #tener en cuenta que esto solo sucede cuando el elemento ya no esta en el bloque de busqueda
        print(f'Iteracion Final: {iter_bin}, su elemento no fue encontrado')
        return (False,iter_bin)

    medio = (comienzo + final) // 2 #division de enteros.
    print(f'[Iteracion: {iter_bin}, Medio: {medio}]\n')

    if lista[medio] == objetivo:
        return (True,iter_bin)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo,iter_bin=iter_bin)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo,iter_bin=iter_bin)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño es la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    # Ordenamos la lista de elementos random
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    print(lista)
    print(f'\nTotal de elementos:{len(lista)}\n')
    (encontrado,iter_bin) = busqueda_binaria(lista, 0, len(lista), objetivo)
    (encontrado,iter_lin) = busqueda_lineal(lista, objetivo)

    #print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda lineal: {iter_lin}')
    print(f'Iteraciones busqueda binaria: {iter_bin}')