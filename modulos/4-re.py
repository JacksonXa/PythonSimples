import re

text = "Udemy - Uma plataforma com muitos cursos"

# 1 - Indice inicial e final de palavras
# O r significa uma raw string (string bruta)
match = re.search(r'uma plataforma'.lower(), text.lower())
print(f"Indice inicial: {match.start()}")
print(f"Indice final: {match.end()}")


# 2 - Buscando o indice que possui o ponto
site = 'https://udemy.com'
match = re.search(r'\.', site)
print(match)

# 3 - Buscar lista de caracteres dentro de uma frase
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

# 4 - Verificando o inicio de uma string (nesse caso se comeca com A)
rule = r'^A'
phrases = ['A casa esta suja', 'O dia esta lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Nao corresponde: {f}")

# 5 - Verifica o final de uma string (nesse caso se termina com uma exclamacao)
rule_end = r'!$'
phrase2 = "O dia esta lindo!"
match = re.search(rule_end, phrase2)
if match:
    print("Sim, corresponde")
else:
    print("Nao corresponde")