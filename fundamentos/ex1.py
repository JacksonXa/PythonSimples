# # 1 - Escreva um programa que le dois nomes e retorna uma string
# # formatada no formato "UltimoNome, PrimeiroNome" 
# primeiroNome = input("Informe um nome: ") 
# segundoNome = input("Informe outro nome: ")

# nomeFormatado = f"{segundoNome} {primeiroNome}"
# print(nomeFormatado)

# # 2- Inverta a ordem das palavras em uma string fornecida.
# texto = "Programando em Python em 2025"
# palavras = texto.split()
# textoInvertido = " ".join(palavras[::-1])
# print(textoInvertido)

# # 3 - Verifique se uma string fornecida eh um palindromo 
# # (pode ser lida da mesma forma de tras para frente)
texto1 = "arara"
texto2 = "python"

#Remove espa;o e deixa nome em minusculo
texto1Format = texto1.lower().replace(" ","")
texto2Format = texto2.lower().replace(" ","")

#Verifica se o texto original eh igual ao seu reverso
palindromo1 = texto1Format == texto1[::-1]
palindromo2 = texto2Format == texto2[::-1]

print(palindromo1)
print(palindromo2)