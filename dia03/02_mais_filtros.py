# %%

import pandas as pd

df = pd.read_csv('../data/transacao_produto.csv', sep=';')

df

# %%

filtro = (df['IdProduto'] == '5') | (df['IdProduto'] == '11')

df[filtro]

# %%

df.dtypes

# %%

# assim faz um filtro estando entre esses valores
df['IdProduto'].isin([5,11])

# %%

# isna vazio e notna preenchido
df['IdProduto'].isna()

# usar o ~ é o NOT ou seja inverte a funcao
~df['IdProduto'].isna()