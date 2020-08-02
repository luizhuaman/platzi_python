from functools import lru_cache
import time

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

#Using decorates
@lru_cache(maxsize = 1000)
def fibonacci_lru(n):
    #Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n debe ser un tipo entero")
    if n < 1:
        raise ValueError("n debe ser un entero positivo")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
#Using memoization
fibonacci_cache = {}

def fibonacci_memo(n):
    #If we have cached the value, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    #Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    #Cache the value and return iter
    fibonacci_cache[n] = value
    return value


def run():
    n = int(input("Cantidad de elemento de la sucesión: "))
    opcion = int(input("""
                       1. Fibonacci (Normalito)
                       2. Fibonacci (Decorates)
                       3. Fibonacci (Memoization)
        Ingresa la opción:
                       """))
    inicial = time.time()
    if opcion == 1:
        for i in range(1, n+1):
            print(f'Elemento {i}: {fibonacci(i)}')
        print(f"Tiempo: {time.time()-inicial}")
    elif opcion == 2:
        for i in range(1, n+1):
            print(f'Elemento {i}: {fibonacci_lru(i)}')
        print(f"Tiempo: {time.time()-inicial}")
    elif opcion == 3:
        for i in range(1, n+1):
            print(f'Elemento {i}: {fibonacci_memo(i)}')
        print(f"Tiempo: {time.time()-inicial}")
    else:
        print("Es de 1 a 3. (╯°□°）╯︵ ┻━┻")
        

if __name__ == '__main__':
    run()