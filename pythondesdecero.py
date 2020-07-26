#DISTINTAS FORMAS DE ARROJAR COMENTARIO
# print("hello world")
# print('hello world')
print('''hello world''')
# print("""hello world""")


#compilados: requiere de un compilador (otro programa) para que el programa escrito 
#pueda ejecutarse, de tal manera que arroje un archivo con un lenguaje que el 
#computador pueda interpretarlo (codigo binario). Java C C#

#lenguajes interpretados: programa que traduce linea por linea a lenguaje maquina y 
#el tiempo de ejecucion es mas lento pero es multiplataforma. php, ruby, python
CONSTANTE = "Soy una constante"
tutor = "Codi"
print(tutor)

#No se puede utilizar las sgtes palabras por que son reservadas. false, else, if, etc.
#https://www.programiz.com/python-programming/keyword-list

valor1, valor2, valor3 = 10, "Codi", 10 * 20
print(valor1)
print(valor2)
print(valor3)

#OPERADORES
# > , < , >= , <= , == , != 
#-> ejemplo
variable1 = 10
variable2 = 20
menor_igual =  variable1 < variable2 #TRUE
print(menor_igual) #resulta true

#Podemos verificar si dos variables son iguales con IS
igual_is = variable1 is variable2
print(igual_is) #result true or falso

#OPERADORES LOGICOS
result_end = True and menor_igual #TRUE
result_end2 = False or menor_igual #TRUE
print(result_end) #resulta true ya que es necesario que ambos valores sean true.
print(result_end2) #resulta true ya que es necesario que al menos un valor sea true.

#Entrada de datos
nombre=input("Cual es tu nombre?\n")
edad=int(input("Cual es tu edad?\n"))
peso=float(input("Cual es tu peso?\n"))
autorizado=input("Estas autorizado?(si/no)\n") =="si"

print("Hola {}, tienes {} años y tu peso es {}\n¿Estas autorizado? {}".format(nombre,edad,peso,autorizado))
# print("Autorizado", autorizado)

"""
Este es un comentario
en parrafo.
"""

#Lista: permite almacenar cualquier valor (int,float,string)
lista = ["Eduardo",23,True,19.5] #tamaño de 4
cursos=["python","django","flask","c","c++","c#","java","php","sql"]
print(cursos[3:8:2]) #[start:end:step] #[:] [start:] [:end]
lista2 = [8.17, 90, 50, 1, 1.32]
lista2.sort(reverse=True) #ordena descendentemente
print("El menor numero de mi lista es {} y el mayor es {}".format(min(lista2),max(lista2)))
print("La longitud de la lista es: {}".format(len(lista2)))
print(lista2)
#resultado = 8 in lista2 para ver si un valor esta en la lista, return true or false.
valor=1.32
print("El indice de valor {} en la lista es {}".format(valor,lista2.index(valor)))
#lista2.count():para saber la cantidad de veces que se ha repetido un valor 
#lista.append():agrega un elemento al final
#lista.insert(index,elemento): inserta en el indice dado y correo los demas valores.
#lista.remove(elemento): elimana el primer elemento que encuentra
#return_value = languages.pop(3) elimina elemento con index3 y return, si no hay index, default -1.
#lista.clear() deja empty la list
#list.reverse() voltea la lista.
#lista1.extend(list2): agrega todos los elementos de la lista2 al final de la lista1
# language list
# language = ['French', 'English', 'German']
# language tuple
# language_tuple = ('Spanish', 'Portuguese')
# language set
# language_set = {'Chinese', 'Japanese'}
# appending element of language tuple
# language.extend(language_tuple)
# appending element of language set
# language.extend(language_set)

#matrices
fila1 = [10,20]
fila2 = [30,40]
matriz = [fila1,fila2]

#tuplas: no se pueden modificar los elementos que almacena. Estas son mas rapidas para las consultas.
#tuple -> () ; list -> []
mi_tupla = (1,2,3,4,5,6,7,8,9,0)
lista = [10,20,30,40,50,60,70,80,90]
tupla = (100,200,300,400,500,600)
print(mi_tupla[:4:2])
uno, dos, *tres, cero = mi_tupla
# Ejemplo: primero, segundo, ultimo = tupla[0], tupla[1], tupla[-1]
#primero, segundo, *_, ultimo = tupla (obtener 1°,2° y ultimo elemento)
print("{}\n{}\n{}\n{}".format(uno,dos,tres,cero))
print(list(zip(mi_tupla,lista,tupla))) #list
print(tuple(zip(mi_tupla,lista,tupla))) #tuple

