def me():
    """
- INICIO
        Este código teiene como propósito Encontrar el límite de recursión teórico de mi máquina y compararlo con el real.
        1. Defino una funcion recursiva
        2. Le paso dos  argumentos: n y resultado_suma  haciendo referencia a un número n y mi suma.
        3. Imprimo el resultado de suma iterado después de pasarlo por un ciclo for

- FINAL
            El resultado que me va a devolver al final es:
=>
    [Previous line repeated 993 more times]==> Cuando mi límite de recursiónteórico es de 1000
        ...
    RecursionError: maximum recursion depth exceeded while calling a Python object
- RECURSION LIMIT
    Para cambiar el límite de recursiónen python se usa la función: sys.setrecursionlimit(limit)
        Esta función ajusta mi limite máximo de profundidad del stack del interprete de pyhton, este límite previene que la recursión "infinita" crashee el "C stack" de Pyhton
- CONSIDERACIONES
    El límite es directamente proporcional a la máquina. Es plataforma dependiente y es mejor usarlo cuando el contexto lo amerite.
        Si el nuevo límite de profundidad en la recursión es muy bajo el error RecursionError aparece.

https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
- ¿CUAL ES MI LÍMITE DE RECURSIÓN?
=>      Para saber el límite de recursiónse usa: sys.getrecursionlimit()
        Me devuelve el valor actual del limite de recursión para el stackde python.

# Modificamos el limite de recursion a 2000 con la funcion sys.setrecursionlimit() que trae el modulo sys
sys.setrecursionlimit(2000)

    """
    pass

#Con este import traigo palabra reservada sys. del sistema
import sys

print(help(me))
print(f'Mi límite de recursión teórico es: {sys.getrecursionlimit()}')

if __name__ == '__main__':

    def recursive_function  (n , resultado_sum):
        if n < 1:
            print(f'Vuelve siempre cero para quese ejecute un true infinito {n}. Soy el resultado de una suma y tengo el valor de: {resultado_sum} ')
            return sum
        else:
            # Soy la suma inicialmente de la forma =>  n = n+1
            # Y mi resultado lo voy a iterar, repetir como una suma =>  (n + 1) + resultado_suma
            recursive_function(n - 1, resultado_sum + n)

#El valor de c me dará indicacióndeque empieza
    c = 0
# Le digo que me itere hasta 998.
for i in range(998):
    c += 1
    valor_iterado = recursive_function(c, 0)