# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%

df.shape

# %%

df.info(memory_usage='deep')

# %%

df.dtypes

# %%

renamed_columns = {
                    'QtdePontos' : 'qtPontos',
                    'DescSistemaOrigem' : 'SistemaOrigem'
                    }

df.rename(columns=renamed_columns, inplace=True) # inplace serve para atribuir as alteracoes ao proprio df sem precisar reatribuir

df

# %%

columns = ['IdCliente', 'qtPontos']

df[columns]

# %%

# SELECT * FROM df
df

# SELECT ID IdCliente FROM df
df[['IdCliente']]

# SELECT IdCliente, qtPontos FROM df LIMIT 5
df[['IdCliente', 'qtPontos']].sample(5) # sample para aleatorio

# reordenar as colunas do df
# SELECT IdCliente, IdTransacao, qtPontos FROM df LIMIT 5
df[['IdCliente', 'IdTransacao', 'qtPontos']].head(5)

# %%

colunas = df.columns.tolist()
colunas.sort()
colunas

df = df[colunas]

df
