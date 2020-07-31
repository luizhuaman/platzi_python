def es_palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input('Escribe una palabra: ')
    palindromo = es_palindromo(palabra)
    if palindromo == True:
        print('Es Palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()