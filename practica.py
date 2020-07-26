#AREA DE UN TRIANGULO
base=int(input("Ingresar base\n"))
altura=int(input("Ingresar altura\n"))
print("El area del triangulo es:",int(base*altura/2))

#dolares a soles
dolares=float(input("Ingresar los dolares a cambiar\n"))
# print("Su cambio en soles es ",(dolares*3.52))

#otra forma
print(f'Cambio: ${float(dolares * 3.52)}')

#comparar edades
var1=int(input("Ingrese edad 1:\n"))
var2=int(input("Ingrese edad 2:\n"))
# igual_is = var1 is var2
# print("Las edades son iguales?\nrpta:",igual_is)

#Otra forma
print(f"Tienen la misma edad?: {var1 is var2}")