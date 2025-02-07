import statistics

# 1 - Aplicando a media
print(statistics.mean([3, 2, 3, 8, 9]))

# 2 - Aplicando a mediana
print(statistics.median([1, 2, 4, 8, 9]))
print(statistics.median([1, 2, 3, 7, 8, 9]))

# 3 - Aplicando a moda (valor que mais se repete)
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]))

# 5 - Desvio padrao
"""
Quanto mais proximo de zero, disgnifica que os dados do conjuntos 
estao menos dispersos
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))

