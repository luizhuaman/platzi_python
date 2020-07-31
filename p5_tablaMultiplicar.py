# def saludo():
#     print("""BIENVENIDO A LAS TABLAS""")

# def tabla_del_numero():
#     numero = int(input("¿Que # de tabla deseas calcular?\n"))
#     limite = int(input("¿Hasta que número?\n"))
#     contador = 0

#     while contador <= limite:
#         resultado = numero * contador
#         print(f"{numero} * {contador} = {resultado}")
#         contador += 1

# if __name__ == "__main__":
#     saludo()
#     tabla_del_numero()

# def tabla_del_numero():
#     n = int(input("¿Que # de tabla quieres calcular?: "))
#     end = int(input("¿Hasta que número?: "))
#     rango = range(1, end + 1)
#     for contador in rango:
#         print(f"{n} * {contador} = {contador * n}")

# if __name__ == '__main__':
#     tabla_del_numero()


def multiplicar(tabla):
    if tabla >= 0:
        print("Tabla del {}".format(tabla))
      
        for i in range(1, 13):
            resultado = i * tabla
            print("{} x {}  = {}".format(tabla, i, resultado))
    else:
        print('LA TABLA NO SE ENCUENTRA EN EL SISTEMA')

def run():
    punto_acceso = 0
    while True:
        try:
            while True:
                #titulo
                formato = '###' * 12
                print('{} \n## Elige una tabla de multiplicar ##\n{}'.format(formato, formato))
                OPCION = "-abcdefghijklm"

                #imprimir valores
                for i in range(1,13):
                    valor = OPCION[i]
                    print("[{}] Tabla del {}".format(valor, i))

                    if i+1 == 13:
                        salir = OPCION[13]
                        print("[{}] Salir".format(salir))

                entrada = input('Ingresa tu opcion : ')
                
                #validando opcion
                if OPCION.rfind(entrada.lower()) > 0 and OPCION.rfind(entrada.lower()) <=13:
                    print('Opcion correcta!!')
                    break;
                else:
                    print('* * * * * * E R R O R * * * * * *')
                    print('Por favor, Ingresa solo valores del Menu')

            #Logica
            if OPCION.rfind(entrada.lower()) == 13:
                # print('entro')
                punto_acceso = 1    
                print('Bye bye, vuelve pronto!')
            else:
                tabla = entrada
                tabla = OPCION.rfind(tabla.lower())
                multiplicar(tabla)

        except:
            print('* * * * * * E R R O R * * * * * *')
        if(punto_acceso == 1):
            break;

    
if __name__ == '__main__':
    try:
        run()
    except:
        run()