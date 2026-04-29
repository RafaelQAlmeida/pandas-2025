# %%

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# isso serve para remover pelo menos uma linha que tenha NA trazendo uma view
clientes.dropna()

# mas o correto seria reatribuir
clientes = clientes.dropna()

clientes

# %%

# podemos tambem escolher a coluna que ira considerar para os NA, agora abaixo se apenas se a linha inteira for NA
clientes.dropna(how = 'all')

# podemos tambem escolher a coluna que ira considerar para os NA, agora abaixo pelo menos uma coluna for NA
clientes.dropna(how = 'any')

# %%

df = pd.DataFrame(
    {
        'nome' : ['Teo', None, 'Nah', 'Marcio'],
        'idade' : [None, None, 43, 52],
        'salario' : [3453, 4324, None, 5423]
    }
)

# dessa forma removemos apenas onde idade está sendo NA
df.dropna(how='any', subset=['idade', 'salario', 'nome']) # da para passar uma lista para as colunas

# %%

# aqui fazemos a alteracao do valor NA para algum valor que desejamos
df['idade'] = df['idade'].fillna(0)

df

# %%

# tambem podemos fazer para varias colunas passando um dicionario
df.fillna({'nome' : 'alguem', 'idade' : 0})

# %%

# alterando os valoes NA pelas respectivas medias de cada linha
df.fillna(df[['idade', 'salario']].mean())

