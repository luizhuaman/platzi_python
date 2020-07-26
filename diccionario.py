#Diccionarios: son modificables, los valores que se almacenan en este se hacen 
# mediante llaves.
# { llave , valor }

diccionario = {}
diccionario = dict() #creacion del diccionario
diccionario = {"total": 55, "descuento": True}
diccionario = {"total": 55, 10: "Curso Python", (1,2,3):True }

#Podemos utilizar clases como llaves, un diccionario es un json
usuario = {
    'nombre': 'Nombre del Usuario',
    'edad': 23,
    'curso': 'Curso Python',
    'skills': {
        'Programacion': True,
        'Base_de_datos': False
    },
    'medallas': ['basico','intermedio']
}

#agregar nueva llave valor
diccionario['usuario']='eduardo'

#Actualizar valor mediante llave
diccionario['usuario']='eduardo_gpg'

#dic = { "a":1, "b":2, "c":3, "a":4} #el dicc para "a" toma el ultimo valor: 4

#obtener valor mediante llave
print(diccionario['usuario'])
print(diccionario.keys())       #dict_keys(['total', 10, (1, 2, 3), 'usuario'])
print(diccionario.values())     #dict_values([55, 'Curso Python', True, 'eduardo_gpg'])   

for key, value in diccionario.items():
        print("La llave es {} y el valor es {}".format(key, value))

#metodo get: permite obtener el valor de la llave
# usuario = dict()
usuarios = {
    'name' : 'Eduardo Ismael',
    'age' : 26,
    'job' : 'Codigo facilito'
}

print(usuarios.get('calificaciones', ''))
calificaciones=usuarios.get('calificaciones', [])
# calificaciones = usuarios.get('calificaciones', [])
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion,"s")

alumnos = ['Eduardo','Fernando','Uriel','Rafael']
nario = { 
    alumno : position +1
    for position, alumno in enumerate(alumnos)
                    }
print(nario)

dic = { "a":1, "b":2, "c":3, "d":4}
valor = "z" in dic #retorna false
print(dic["a"])

print(dic.get("z","La llave no existe")) #Si no se pone el return del get, retorna "None"
print(dic.setdefault("z",{})) #si no encuentra la llave, inserta y retorna valor.
print(dic)
del dic["a"] #Elimina la llave y el valor
print(dic)
print(len(dic)) #Cuenta los elementos
print(dic)
print("Valor eliminado es {}".format(dic.pop("b"))) #con pop retornamos el valor eliminado
print(dic)

#para eliminar todos los elementos dic={} o dic.clear()




