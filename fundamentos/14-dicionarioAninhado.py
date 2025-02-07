import pprint

linha = "\n***********************************\n"

filmsDict = {
    "Inception":{
        "title": "Inception",
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi","Action", "Thriller"]
    },
    "Harry Potter":{
        "title": "Inception",
        "yearRelease": 2009,
        "imdbRating": 9.9,
        "genre": ["Sci-fi","Fantasy", "Thriller"]
    },
    "Velozes e Furiosos":{
        "title": "Inception",
        "yearRelease": 2008,
        "imdbRating": 9.5,
        "genre": ["Action","Drama", "Adventure"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)


# 1 - Buscar uma informacao dentro de um dicionario aninhado
print(linha)
print(filmsDict["Harry Potter"]["genre"])
print(linha)
