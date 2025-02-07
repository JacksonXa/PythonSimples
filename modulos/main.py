# Programa Principal
import math_operation
# Do modo math_operation importe as funcoes multiplicar e dividir
from math_operation import multiplicar, dividir
import string_utils

print(math_operation.soma(5, 3))
print(math_operation.subtrair(5, 3))
print(multiplicar(5, 3))
print(dividir(5, 3))

print(string_utils.capitalizar("hello"))
print(string_utils.string_reversa("python"))
print(string_utils.contar("apple"))