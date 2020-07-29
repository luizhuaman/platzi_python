#Este programa convierte una cantidad de dolares a pesos mexicanos

#Primero definimos nuestras funciones
def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " convertiras? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    pesos = input("Tienes " + dolares + " dolares")

# Pedimos al usuario la cantidad que solares a convertir
menu = """ Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elije una opciones : """

opcion = int(input(menu))
if opcion == 1:
    conversor("colimbianos",3875)
elif opcion == 2:
    conversor("argentinos",65)
elif opcion == 3:
    conversor("mexicanos",24)
else:
    print("Opcion incorrecta, Gracias por participar")

# Nota1 : Para usar un string grandes usamos las tres comillas 
# Tal como se muesta en el ejemplo """   """"
# Nota2 : Para usar emojis oprimir ctrl + cmd + Espacio