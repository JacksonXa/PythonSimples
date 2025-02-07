name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lancamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

# # Alternativa 1
print("Dados do Filme")
print("Nome do Filme:",name)
print("Ano Lancamento:",yearLaunch)
print("Nota do Filme:",noteMovie)

# # Alternativa 2
print("Nome do Filme:", name, "\nAno Lancamento:", yearLaunch, "\nNota do Filme:", noteMovie)

# # Alternativa 3
print(f"Nome do Filme: {name}\n"
      f"Ano de lancamento: {yearLaunch}\n"
      f"Nota do filme: {noteMovie}\n")
