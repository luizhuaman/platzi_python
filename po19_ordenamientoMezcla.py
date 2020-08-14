import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        print(izquierda)
        print(derecha)

        #llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        #Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0
        print(f'i:{i} j:{j} k:{k}')
        print(f'len izq es {len(izquierda)} y len der {len(derecha)}')

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                print(f'izq[{i}]..{izquierda[i]} y der[{j}] ... {derecha[j]}')
                lista[k] = izquierda[i]
                print(f'{k}: {lista[k]}')
                i += 1
            else:
                print(f'izq[{i}]..{izquierda[i]} y der[{j}] ... {derecha[j]}')
                lista[k] = derecha[j]
                print(f'{k}: {lista[k]}')
                j += 1

            k += 1

        while i < len(izquierda):
            print(f'i:{i} y len izq {len(izquierda)}')
            lista[k] = izquierda[i]
            print(f'{k}: {lista[k]}')
            i += 1
            k +=1

        while j < len(derecha):
            print(f'j:{j} y len der {len(derecha)}')
            lista[k] = derecha[j]
            print(f'{k}: {lista[k]}')
            j += 1
            k += 1
        
        print(f'lista izquierda {izquierda},lista derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista



if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño sera la lista? : '))
    
    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    print('-' * 20)
    
    lista_ordenada = ordenamiento_por_mezcla(lista)
    
    print(lista_ordenada)