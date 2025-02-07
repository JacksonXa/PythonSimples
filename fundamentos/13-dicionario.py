filmeInception = {
    "title": "Inception",
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi","Action", "Thriller"]
}
linha = "\n***********************************\n"

print(filmeInception)
print(len(filmeInception))
print(type(filmeInception))

# 1 - Recuperar elemento do dicionario
print(linha)
print(filmeInception["genre"])
print(filmeInception.get("imdbRating"))

# 2 - Buscar apenas as chaves do dicionario
print(linha)
print(filmeInception.keys())

# 3 - Busca apenas os valores do dicionario
print(linha)
print(filmeInception.values())

# 4 - Buscar itens do dicionario com chave e valor
print(linha)
print(filmeInception.items())

# 5 - Adicionar itens no dicionario
filmeInception["director"] = "Jackson Xavier"
print(linha)
print(filmeInception)

# 6 - Atualizar itens no dicionario
filmeInception.update({"imdbRating": 8.7})
print(linha)
print(filmeInception)

# 7 - Remoiver item do dicionario
filmeInception.pop("director")
print(linha)
print(filmeInception)