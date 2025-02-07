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

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Media do jogo {self.name}: {self.totalEvaluation / self.evaluators}")

game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)
game1.average()
game2.average()
