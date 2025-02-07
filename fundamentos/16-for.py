# Lista de Filmes
filmesLista = ["Titanic", "Harry Potter", "Velozes e Furiosos", "Sherek"]

# 1 - Iterando valores de uma lista
for filme in filmesLista:
    print(filme)

# 2 - Quando a condicao for atendida, o Loop sera encerrado
for filme in filmesLista:
    if filme == "Velozes e Furiosos":
        print("Parando...")
        break
    print(filme)

# 3 - Quando a condicao for atingida o loop vai para a proxima teracao
for filme in filmesLista:
    if filme == "Velozes e Furiosos":
        print("Pulando...")
        continue
    print(filme)

# 4 - Avaliacao do filme
nomeFilme = input("Digite o nome do filme: \n")
avalizacaoFilme = int(input("Digite quantas avaliacoes deseja fazer: \n"))
total = 0

for i in range(avalizacaoFilme):
    nota = float(input("Digite a nota para o filme:\n"))
    total += nota

if avalizacaoFilme > 0:
    media = total / avalizacaoFilme
else:
    media = 0

# Imprimento a media com 2 casas decimais por isso os dois pontos .2f
print(f"Media de avaliacao do filme {nomeFilme} eh: {media:.2f}")