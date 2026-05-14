# %%

import pandas as pd

# %%

idades = [32, 44, 12]

idades = pd.Series(idades)

idades

# %%

idades.describe()

# %%

clientes = pd.read_csv('../data/clientes.csv',sep=';')

clientes.head()

# %%

clientes['flTwitch'].sum()

clientes['flTwitch'].mean()

# %%

redes_sociais = ['flEmail','flTwitch','flYouTube','flBlueSky','flInstagram']

# aplicando num DF é calculado os valores de cada uma das colunas (se forem numericas)
clientes[redes_sociais].mean() * 100

# %%

# para calcular automaticamente campos numericos
num_columns = clientes.dtypes[~(clientes.dtypes == 'object')].index.tolist()

clientes[num_columns].describe()

# %%

