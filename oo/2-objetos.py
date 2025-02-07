class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0

# Primeiro jogo
game1 = Game()
game1.name = "The Legend of Zelda"
game1.yearLaunch = 2017
game1.multiplayer = False
game1.note = 9.5

# Segundo jogo
game2 = Game()
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.note = 8.0


print("### Dados do Jogo ###")
print(f"\nNome do jogo: {game1.name}\nAno de lancamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de lancamento: {game2.yearLaunch}")