# # Informacoes sobre o filme
# name = input("Digite o nome do filme:\n")
# yearRelease = int(input("Digite o ano de lancamento:\n"))
# rating = float(input("Digite a nota do filme:\n"))

# # Verifica se o filme eh recomendado
# if rating > 8.0 and yearRelease > 2015:
#     print(f"O filme {name} eh muito bom. Recomendo assisti-lo.")
# else:
#     print(f"O filme {name} ainda nao atingiu uma boa nota")

num1 = float(input("Digite o primeiro numero:\n"))
num2 = float(input("Digite o segundo numero:\n"))  
operation = input("Digite a operacao a ser realizada: (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisao por Zero")
        result = 0
else:
    print("Operacao invalida")
    result = 0 

print(f"Resultado da operadao: {result:.2f}")