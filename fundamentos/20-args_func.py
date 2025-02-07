# 1 - Funcao para imprimir um nome completo
def full_name(first_name, last_name):
    print(f"Nome eh {first_name} {last_name}")

full_name("Jackson", "Xavier")
full_name("Joao", "Costa")

# 2 - Funcao para somar 2 numeros
def sum_numbers(a,b):
    return a + b

print(f"Soma eh: {sum_numbers(10, 40)}")

# 3 - Funcao com parametro deafult
def address(country="Brasil"):
    print(f"Eu moro em {country}")

address()
address("Espanha")

# 4 - Funcao para avaliar um filme
def rate_movie (num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme \n"))
        total += note
    
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    
    print(f"Media de avalicaodo filme {movie_name} eh {average:.2f}")

rate_movie(2, "Sonic")
