#Para cada elemento se define la estructura clave:valor:

#Store the names of the users and the passwords
#sotre user names and passwords and ask the user to sing in
try:
	import sys
except ImportError:
	print()
	print("ERROR: Module 'sys' wasn't found")
else: 
	pass

list1 = []

def add_element_function(listt):
	"""Pregunta el nombre del servicio, username y password
        Luego las guarda en la lista

		(Recuerda presionar 'q' para salir de esta ventana)
	"""

	service_name = str(input("Ingresa nombre de webpage/app: "))
	user_name = str(input("Ingresa username: "))
	user_password = str(input("Ingresa password: "))

	new_item = {
		"service": service_name, 
		"user": user_name,
		"password": user_password
		}

	listt.append(new_item)
	print("Status: Datos Ingresados Correctamente!")
	print(f"Elementos Actuales: {len(listt)}")
	print()
	return listt 

	
def list_viewer(listt):
	"""ver los elemntos dados de una lista

		(Recuerda presionar 'q' para salir de esta ventana)
	"""
	if len(listt) == 0:
		print("No hay elementos")
		print()
	else:
		i = 0
		for dictionary in listt:
			i += 1
			print(f"Account #{i} »»")
			print(
				"\tService Name: ", dictionary["service"], "\n",
				"\tUser Name: ", dictionary["user"], "\n",
				"\tPassword: ", dictionary["password"], "\n",
				)

def process_info(process):
	"""Muestra la informacion de los procesos
		ejecutados en cada opcion.

		(Recuerda presionar 'q' para salir de esta ventana)
	"""
	help(process)

def remove_element(listt):
	"""Imprime todas las cuentas registradas
        Pregunta al usuario cuál quiere eliminar.
        Eliminar la cuenta

		(Recuerda presionar 'q' para salir de esta ventana)
	"""

	for dictionary in listt:
			print(
				dictionary["service"], "\n",
				dictionary["user"], "\n",
				dictionary["password"], "\n",
				)

	user_input = int(input("¿Que cuenta quieres eliminar de aqui? (por favor escriba la posición): "))
	del listt[user_input]
	print()
	return listt

menu = {
	"1": "Agregar nuevo elemento",
	"2": "Ver los elementos actuales",
	"3": "Info",
	"4": "Remover elementos",
	"5": "Exit"
}
while(True):
	for key, value in menu.items():
		print(key +")", value)
	try:
		user_option = input()
		if user_option not in menu:
			raise TypeError
	except TypeError:
		print(f"ERROR: '{user_option}' no es un comando valido, por favor ingresa (1/2/3/4/5)")
	else:
		pass
		
	if user_option == "1":
		add_element_function(listt = list1)
	elif user_option == "2":
		list_viewer(listt = list1)
	elif user_option == "3":
		while(True):
			option1 = str(input("¿Que proceso quieres saber cómo funciona?(1/2/3/4): "))
			if option1 == "1":
				process_info(process = add_element_function)
				break
			elif option1 == "2":
				process_info(process = list_viewer)
				break
			elif option1 == "3":
				process_info(process = process_info)
				break
			elif option1 == "4":
				process_info(process = remove_element)
				break
			else:
				print(f"'{option1}' no es un comando valido, por favor ingresa (1/2/3/4):")
				print()
	elif user_option == "4":
		remove_element(listt = list1)
	else:
		if user_option == "5":
			print("Hasta Luego, Me alegro de haberte ayudado!")
			sys.exit()