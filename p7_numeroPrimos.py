def es_primo(numero):
    if numero == 1:
        return False
    else:
        contador = 0

    for i in range(1 , numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    #Cantidad de divisores
    print("Tiene {} divisores".format(contador+2))
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print(str(numero) + " es primo")
    else:
        print(str(numero) +  " no es primo")


if __name__ == "__main__":
    run()


#metodo wilson
# def primo(n):

#     if n == 0 or n == 1:
#         return print(f'No es primo')
#     else:
#         n = n - 1

# def factorial(n):
# if n == 1:
#     return 1

# return n * factorial(n - 1)

#     return print(f'Es primo') 
#     if (factorial(n) + 1) %(n+1) == 0
#     else print(f'No es primo')

# if __name__ == '__main__':
#     number = int(input('Ingrese un numero: '))
#     my_test = primo(number)