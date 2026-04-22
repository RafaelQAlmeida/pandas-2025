# %%

idades = [ 32, 38, 30, 31 ]

media = sum(idades) / len(idades)
print("Media: " ,media)

diffs = 0

for i in idades:
    # print("-------Idade: ", i)
    # print("Media: ", media)
    diffs += (i - media) ** 2
    # print("Diffs: ", diffs)

variancia = diffs / (len(idades) - 1)

print("Variancia: ",variancia)

# %%

import pandas as pd

series_idades = pd.Series(idades)
series_idades

# %%

# Estatisticas da series
media_idades = series_idades.mean()
media_idades

var_idades = series_idades.var()
var_idades

summary_idades = series_idades.describe()
summary_idades