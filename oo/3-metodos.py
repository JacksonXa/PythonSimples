class Game:
    # Metodo construtor - Definindo que os atributos sejam informados no 
    # momento em que instaciar/chamar a classe
    def __init__(self, name="", yearlaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearlaunch = yearlaunch
        self.multiplayer = multiplayer
        self.note = note

    # Metodo para que ao chamar direto a classe Game o programa retorne o 
    # nome do jogo e nao o espcao em memoria
    def __str__(self):
        return f"Game {self.name}"

game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game1 = Game("Fortnite", 2017, True, 8.0)
# game1.name = "Super Mario"
print(game1)

print("### Dados do Jogo ###")
# print(f"\nNome do jogo: {game1.name}\nAno de lancamento: {game1.yearLaunch}")
# print(f"\nNome do jogo: {game2.name}\nAno de lancamento: {game2.yearLaunch}")