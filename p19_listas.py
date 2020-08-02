"""
😄 Acá investigue los métodos de listas: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Los nuevos que encontré además de los de la clase:

lista.extend(iterable) #extiende la lista con valores dentro de un iterable como un range()
lista.insert(i, ‘valor’) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.
lista.pop(i) #Elimina valor en la posición i de la lista y retorna.
lista.remove(‘valor’) #Elimina el primer elemento con ese valor.
lista.clear() #Borra elementos en la lista.
lista.index(‘valor’) #Retorna posición del primer elemento con el valor.
lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
lista.count(‘valor’) #Cuenta cuántas veces esta ese valor en la lista.
lista.sort() #Ordena los elementos de mayor a menor.
lista.sort(reverse = True) #Ordena los elementos de menor a mayor.
lista.reverse() #Invierte los elementos
lista.copy() #Genera una copia de la lista. También útil para clonar listas.
"""

# Crear una lista:
mylist = ['one', 20, 5.5, [10, 15], 'five']

# listas mutables:
mylist = ['one', 'two', 'three', 'four', 'five']
mylist[2] = "New item"
# Si el índice es negativo, cuenta desde el último elemento.
elem = mylist[-1]

# Recorrer una lista:
for elem in mylist:
    print(elem)

# Actualizar elementos:
mylist = [1, 2, 3, 4, 5]
for i in range(len(mylist)):
    mylist[i]+=5

print(mylist)

mylist = ['one', 20, 5.5, [10, 15], 'five']
print(len(mylist))

# Cortar una lista:
mylist = ['one', 'two', 'three', 'four', 'five']
mylist[1:3] = ['Hello', 'Seven']
print(mylist)

# Insertar en una lista:
mylist = [1, 2, 3, 4, 5]
mylist.insert(1, 'Hello')
print(mylist)

# Agregar a una lista al final:
mylist = ['one', 'two', 'three', 'four', 'five']
mylist.append("new one")

mylist = ['one', 'two', 'three', 'four', 'five']
list2 = ["Hello", "new one"]
mylist.extend(list2)
print(mylist)

# Ordenar una Lista:
mylist = ['cde', 'fgh', 'abc', 'klm', 'opq']
list = [3, 5, 2, 4, 1]
mylist.sort()
list.sort()
print(mylist)
print(list)

# Invertir una lista:
mylist = [1, 2, 3, 4, 5]
mylist.reverse()
print(mylist)

# Indice de un elemento:
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist.index('two'))

# Eliminar un elemento:
mylist = ['one', 'two', 'three', 'four', 'five']
removed = mylist.pop(2)
print(mylist)
print(removed)

mylist.remove('two')
del mylist[2]

mylist = ['one', 'two', 'three', 'four', 'five']
del mylist[1:3]
print(mylist)

# Funciones agregadas:
mylist = [5, 3, 2, 4, 1]
print(len(mylist))
print(min(mylist))
print(max(mylist))
print(sum(mylist))

# Comparar listas:
mylist = ['one', 'two', 'three', 'four', 'five']
list2 = ['four', 'one', 'two', 'five', 'three']
if (mylist == list2):
     print("match")
else:
     print("No match")

# Operaciones matematicas en las listas:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
print(list1 * 2)

# Listas y cadenas:
mystr = "LikeGeeks"
mylist = list(mystr)
print(mylist)

mystr = "LikeGeeks"
mystr = "Welcome to likegeeks website"
mylist = mystr.split()
print(mylist)

# Unir una lista:
mylist = ['Welcome', 'to', 'likegeeks', 'website']
delimiter = ' '
output = delimiter.join(mylist)
print(output)

# Aliasing:
mylist = ['Welcome', 'to', 'likegeeks', 'website']
list2 = mylist
list2[3] = "page"
print(mylist)

#Clonar
a = [1,2,3]
b = a
# b y a comparte el mismo espacio de memoria id(c)
d = a[::]
print(d)
print(id(d))

#List Comprehension: forma concisa de aplicar operaciones a todos los valores.
my_list = list(range(100))
print(my_list)
double = [i * 2 for i in mylist ]

pares = [i for i in my_list if i % 2 == 0]
print(pares)

#Diccionarios

