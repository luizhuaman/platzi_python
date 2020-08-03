# import unittest

# class CajaNegraTest(unittest.TestCase):


listt = []

service_name = input('Ingresa el servicio: ')
user_name = input('Ingresa el user_name: ')
user_password = input('Ingresa el password: ')

new_item = {
		"service": service_name, 
		"user": user_name,
		"password": user_password
		}
listt.append(new_item)
new_item2 = {
	"service": 'instagram', 
	"user": 'luis',
	"password": 'dsdadasds'
	}
listt.append(new_item2)

for dictionary in listt:
	print(
		dictionary["service"], "\n",
		dictionary["user"], "\n",
		dictionary["password"], "\n",
		)

print(listt)

i = 0
for dictionary in listt:
	i += 1
	print(f"Cuenta #{i} :")
	print(
		"\tService Name: ", dictionary["service"], "\n",
		"\tUser Name: ", dictionary["user"], "\n",
		"\tPassword: ", dictionary["password"], "\n",
		)

OpcionBorrar = int(input('Ingrese la cuenta a borrar: '))-1

del listt[OpcionBorrar]

j = 0
for dictionary in listt:
	j += 1
	print(f"Cuenta #{j} :")
	print(
		"\tService Name: ", dictionary["service"], "\n",
		"\tUser Name: ", dictionary["user"], "\n",
		"\tPassword: ", dictionary["password"], "\n",
		)

	