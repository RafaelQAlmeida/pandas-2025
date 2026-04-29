# %%

import pandas as pd

# %%

df = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# astype permite converter tipos de colunas
df['qtdePontos'].astype(int)

# %%

# isso serve para fazer substituicoes de valores passando o valor antigo e o valor novo
df['DtCriacao'].replace(
    {
        '0000-00-00 00:00:00.000' : '2024-02-01 09:00:00.000'
    }
    )

df['DtCriacao'] = pd.to_datetime(df['DtCriacao'])

# atributo dt permite varios valores correspondentes para data
df['DtCriacao'].dt.date
df['DtCriacao'].dt.day
df['DtCriacao'].dt.month_name()