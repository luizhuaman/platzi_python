
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))

# Excepciones comunes:
# ImportError : una importación falla;
# IndexError : una lista se indexa con un número fuera de rango;
# NameError : se usa una variable desconocida ;
# SyntaxError : el código no se puede analizar correctamente
# TypeError : se llama a una función en un valor de un tipo inapropiado;
# ValueError : se llama a una función en un valor del tipo correcto, pero con un valor inapropiado

#All possible errors
"""
except TypeError:
    print("is thrown when an operation or function is applied to an object of an inappropriate type.")
except IndexError:
   	print("is thrown when trying to access an item at an invalid index.")
except KeyError:
    print("is thrown when a key is not found.")
except ImportError:
  	print("Raised when the imported module is not found.")
except StopIteration:
  	print("is thrown when the next() function goes beyond the iterator items.")
except ValueError:
  	print("is thrown when a function's argument is of an inappropriate type.")
except NameError:
  	print("is thrown when an object could not be found.")	
except ZeroDivisionError:
  	print("is thrown when the second operator in the division is zero.")
except KeyboardInterrupt:
  	print("is thrown when the user hits the interrupt key (normally Control-C) during the execution of the program.")
except MemoryError:
  	print("Raised when an operation runs out of memory.")
except FloatingPointError:
  	print("Raised when a floating point operation fails.")
except OverflowError:
  	print("Raised when the result of an arithmetic operation is too large to be represented.")
except ReferenceError:
  	print("Raised when a weak reference proxy is used to access a garbage collected referent.")
except TabError:
  	print("Raised when the indentation consists of inconsistent tabs and spaces.")
except SystemError:
  	print("Raised when the interpreter detects internal error.")
except RuntimeError:
  	print("Raised when an error does not fall under any other category.")
except:
 	print("Error detected can't be handled nor clasified.")

"""