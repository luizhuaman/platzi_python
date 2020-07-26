curso="Curso de Python 3"
print(len(curso))
print(curso[1:16:2])
#No se puede modificar los String, son inmutables.

#split + join
lenguajes= "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"
resultado=lenguajes.split("; ")
print(resultado) #Es una lista
nuevo_string=" ".join(resultado) #los resultados los separa por " "
print(nuevo_string)

texto="""
Este
es
un texto
con
saltos
"""
resultado_split=texto.splitlines()
print(resultado_split)
nuevo_string_2=" ".join(resultado_split)
print(nuevo_string_2)

#FORMATOS
texto="curso de Python 3, Python basico  "
print(texto.capitalize())   #1ra letra Mayus
print(texto.swapcase())     #Change minus<->mayus
print(texto.upper())        #mayus
# print(texto.isupper())    #bolean
# print(texto.islower())    
print(texto.title())        #1ras letras en Mayus
print(texto.replace("Python","Ruby",1)) #2-> numero de reemplazos
print(texto.strip(),"\n")        #borra espacios en blanco del string

#otros formatos
curso="Python"
version="3"
print("Curso de %s %s" %(curso, version))
print("Curso de {b} {a}".format(a=curso,b=version))
concatenacion=curso+version+" concat "+str(3) #Solo se concatena string, para ello str()
print("La concatenacion es {}".format(concatenacion))
print("La letra {} se encuentra {} veces en el texto de arriba".format("o",concatenacion.count("o")))
# texto in/not in mensaje; retorna false o true
# mensaje.find("texto"); retorna posicion de la primera letra de texto.
# mensaje.startwith("Este"); retorna True or False
# mensaje.endwith("Este"); retorna True or False



