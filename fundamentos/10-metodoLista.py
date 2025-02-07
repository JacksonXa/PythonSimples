filmsList = ["Inception", "The Shaw", "Velozes e Furioso", "Harry Potter", 
             "Matrix"]

# 1 - Tamanho da lista
print(len(filmsList))

# 2 - Recuperara um item da lista pelo nome
print(filmsList.index("Velozes e Furioso"))

# 3 - Adicionar item ao final da lista
filmsList.append("Senhor dos Aneis")
print(filmsList)

# 4 - Ordenar lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Harry Potter")
print(filmsCopy)

# 6 - Remover todos os itens da lista
filmsList.clear()
print(filmsList)