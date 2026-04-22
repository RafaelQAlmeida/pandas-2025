# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# %%

# retorna os primeiros valores de um dataframe
df_clientes.head(10)

# %%

# retorna os ultimos valores de um dataframe
df_clientes.tail(10)

# %%

# retorna uma amostra aleatoria de um dataframe (serve para entender o dataframe)
df_clientes.sample(10)

# %%

# retorna uma tupla com a quantidade de linha e colunas do df
df_clientes.shape # atributo e nao metodo

# %%

# retorna uma lista com os nomes das colunas do df
df_clientes.columns

# %%

# retorna o indice do dataframe, se nao for importado o pd cria um indice sequencial
df_clientes.index

# %%

# retorna as informacoes do df e os tipos das colunas

df_clientes.info() # retorna tambem a memoria utilizada mas apenas fazendo um inferencia

df_clientes.info(memory_usage='deep') # com isso é o que realmente está usando da memoria

# %%

# dtypes eh uma series que retorna os valores das tipagens das colunas do df 
df_clientes.dtypes["qtdePontos"]