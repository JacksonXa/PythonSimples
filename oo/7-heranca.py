# Classe Pai (Super classe) - Generalista
class Game:

    # Variavel de classe, para contar o numero total de jogos
    total_games = 0

    # Metodo construtor - Definindo que os atributos sejam informados no 
    # momento em que instaciar/chamar a classe
    def __init__(self, name="", yearlaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearlaunch = yearlaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
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

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Media do jogo {self.name}: {self.totalEvaluation / self.evaluators}")


# Classe derivada (Subclasse) - Especilizada
class SinglePlayerGame(Game):
    # __init__ eh um metodo construtor
    def __init__(self, name="", yearlaunch=0, note=0, storyline=""):
        super().__init__(name, yearlaunch, multiplayer=False, note=note)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")

mult_game = Game("Fortnite", 2017, True, 8.0)
mult_game.technical_sheet()

sing_game = SinglePlayerGame("The Last of Us 2", 2010, 9.5, "Emocionante hist[oria de sobrevivencia e vinganca")
sing_game.technical_sheet()