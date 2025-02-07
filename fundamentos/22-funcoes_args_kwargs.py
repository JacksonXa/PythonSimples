"""
*args - Utilizamos quando nao temos certeza de quantos argumentos
queremos ter em uma funcao
- Os argumentos sao passados como uma tupla
**kwargs - Alem dos valores podemos passar tambem as respectivas chaves
para cada argumento
- Os argumentos sao passados como um dicionario
"""

# 1 - Soma de numeros
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma eh {sum_total}")

sum(7)
sum(7,9)
sum(7,9,10)
sum(7,9,10,11)

# 2 - Apresentacao de Curso
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de Cursos: ")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visao computacional com Python", category="IA", level="Avancado")
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediario")