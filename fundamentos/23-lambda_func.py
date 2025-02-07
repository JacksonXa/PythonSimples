# Funcao de potencia de um numero
power = lambda num: num ** 2

# Funcao que verifica se o numero eh par
is_even = lambda x: x % 2 == 0

# Funcao que divide um numero por outro
div_num = lambda x, y: x / y

# Funcao que inverte uma string
reverse_string = lambda s: s[::-1]

print(power(5))
print(power(9))
print(is_even(27))
print(is_even(30))
print(div_num(10, 2))
print(div_num(6, 2))
print(reverse_string("Python"))
print(reverse_string("JavaScript"))


# Funcionalidade relacionada aos filmes
movies_list = ["Titanic", "Harry Potter", "Velozes e Furiosos", "Sherek", "Mais Velozes"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "Harry Potter": [9.5, 9.8, 8.0],
    "Velozes e Furiosos":[8.0, 8.5, 7.0],
    "Sherek": [7.5, 7.0, 8.0],
    "Mais Velozes": [8.8, 9.2, 8.5]
}

# Funcao para calcular a media de avaliacoes de um filma
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print(f"Media de Avaliacao do filme Titanic: {average_rating("Titanic")}")