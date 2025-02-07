"""
Fatorial de um numero:
1 -> 1 * 1
2 -> 2 * 1
3 -> 3 * 2 * 1
"""
# 1 - Fatorial de um numero
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

number = int(input("Digite o numero para o fatorial: \n"))
print(f"O fatorial de {number} eh {factorial(number)}")

# 2 - Soma total de um numero
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))

num = int(input("Digite o numero para a soma: \n"))
print(f"A soma total {num} eh {total_sum(num)}")