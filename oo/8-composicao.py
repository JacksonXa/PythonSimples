class Game:

    # Metodo construtor - Definindo que os atributos sejam informados no 
    # momento em que instaciar/chamar a classe
    def __init__(self, name="", yearlaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearlaunch = yearlaunch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0
        self.evaluators = 0

    # Metodo para que ao chamar direto a classe Game o programa retorne o 
    # nome do jogo e nao o espcao em memoria
    def __str__(self):
        return f"Game {self.name}"
    
    def technical_sheet(self):
        print("\n### Dados do Jogo ###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lancamento: {self.yearlaunch}")
        print(f"Modo Multiplayer: {self.multiplayer}")
        print(f"Avaliacao do Jogo: {self.note}")

class GameStudio:
    def __init__(self, name=""):
        self.name  = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)
    
    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estudio {selg.name} ainda nao lancou jogo")
        else:
            average_note = total_notes / num_games
            print(f"Avaliaca media dos jogos do estudio  {self.name}: {average_note:.2f}")


game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("The last of Us 2", 2020, False, 9.0)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()