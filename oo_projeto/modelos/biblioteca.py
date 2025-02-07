class Biblioteca:
    # Criando uma lista de bibliotecas
    bibliotecas = []

    # Criando o metodo construtor
    """
    Quando instanciar minha classe eu preciso passar o nome d
    a biblioteca
    """
    def __init__(self, nome):
        # Quando uma biblioteca for criado, ja informar o nome dela
        self.nome = nome
        # Quando criar uma biblioteca, por padrao, ele deve estar desativada
        self.ativo = False
        # Quando criar uma biblioteca ja adicionar (append) na lista de bibliotecas 
        # utilizado a palavra self para fazer referencia ao meu objeto
        Biblioteca.bibliotecas.append(self)

    """
    Metodo que vai sobreescrever uma informacao quando o 
    objeto for instanciado
    """
    def __str__(self):
        return self.nome
    
    """
    Vai ate a  minha lsita de bibliotecas, faz um interacao sobre 
    os dados e traz a lista de bibliotecas que eu tenho
    """
    def listar_bibliotecas():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} | {biblioteca.ativo}")


biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")


print(biblioteca_cidade)
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()

# class Biblioteca:
#     nome = ""
#     ativo = False

#     def __str__(self):
#         return self.nome

# # Criando e  Adicionando dados dentro da minha biblioteca cidade
# biblioteca_cidade = Biblioteca()
# biblioteca_cidade.nome = "Biblioteca da Cidade"
# biblioteca_cidade.ativo = True

# # Criando e  Adicionando dados dentro da minha biblioteca shopping
# biblioteca_shopping = Biblioteca()

# bibliotecas = [biblioteca_shopping, biblioteca_cidade]

# print(biblioteca_cidade)
# print(vars(biblioteca_cidade))
# print(vars(biblioteca_shopping))

# # Percorra a lista bibliotecas e armazene as informacoes de cada linha da lista na variavel
# # biblioteca, exiba os dados de cada linha/biblioteca
# contador = 0
# for biblioteca in bibliotecas:
#     contador += 1
#     print(f"Loop {contador} de {len(bibliotecas)}")
#     print(vars(biblioteca))