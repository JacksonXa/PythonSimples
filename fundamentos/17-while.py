# Lista de Filmes
listaFilmes = ["Titanic", "Harry Potter", "Velozes e Furiosos", "Sherek"]

# 1 - Iterando valores de filmes de uma lista
index = 0
while index < len(listaFilmes):
    print(listaFilmes[index])
    index += 1


# 2 - Quando a condicao for atendida, o Loop sera encerrado
index = 0
while index < len(listaFilmes):
    if listaFilmes[index] == "Velozes e Furiosos":
        print("Parando....")
        break
    print(listaFilmes[index])
    index += 1