# 1 - Listar valores de 0 a 10 que sejam menores do que 4
# for i in range(10):
#     if i < 4:
#         print(i)
listNumeros = [i for i in range(10) if i < 4]
print(listNumeros)

# Lista de Filmes
listaFilmes = ["Titanic", "Harry Potter", "Velozes e Furiosos", "Sherek", "Mais Velozes"]

# 2 Filmes que possuem a letra E no titulo
filmesComE = [filme for filme in listaFilmes if 'h' in filme.lower()]
print(filmesComE)

# 3 - Filmes que eu assisti
filmesAssistidos = [filme for filme in listaFilmes if filme != "Titanic"]
print(filmesAssistidos)

# 4 - Encontrando um filme pelo nome
while True:
    filmeDigitado = input("Digite o nome do filme para buscar na lista ou Sair para encerrar: \n")
    if filmeDigitado.lower() == "sair":
        print("Programa Encerrado")
        break
    encontrarFilmes = [filme for filme in listaFilmes if filmeDigitado.lower() in filme.lower()]
    if encontrarFilmes:
        print(f"Filmes(s) encontrado(s) com o nome {filmeDigitado}:")
        for filme in encontrarFilmes:
            print(filme)
    else:
        print(f"Nenhum filme foir encontrado com o nome {filmeDigitado}. Tente novamente!")