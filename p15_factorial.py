def factorial(n):
    """Calcula el Factorial de N
    N Int  > 0
    Return N!
    """
    # print(n)
    if n == 1:
        return1
    return n * factorial (n - 1)

n = int(input('Escribe un entero: '))

print(factorial(n))