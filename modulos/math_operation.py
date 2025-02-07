# Modulo de operacoes Matematicas

def soma(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Nao eh permitido divisao por Zero")