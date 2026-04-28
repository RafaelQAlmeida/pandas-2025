# %%

import pandas as pd
import numpy as np

df = pd.read_csv('../data/clientes.csv', sep=';')

df.head()

# %%

# Funcao escalar, que vai somando encima de cada elemento da serie
df['pontos_100'] = df['qtdePontos'] + 100 #atribuindo uma nova coluna

# %%

nova_coluna = []

# usando assim tambem funciona, porem eh menos performatico pq precisa acessar elemento por elemento
for i in df['qtdePontos']:
    nova_coluna.append(i+100)

nova_coluna

# %%

# para saber se a pessoa tem email ou twitch
df['emailTwitch'] = df['flEmail'] + df['flTwitch']

df.head()

# %%

# se multiplicar, como eh 1 ou 0 só vai dar 1 onde tiver pelo menos 1
df['flEmail'] * df['flTwitch']

# da mesma forma, se for somar tudo eu consigo saber quantas redes sociais cada usuario tem cadastrado

# %%

df['qtdePontos'].describe()

# %%

# numpy eh muito util e rapido para calculos
df['logPontos'] = np.log(df['qtdePontos'] +1)

# %%

df['logPontos'].describe()

# %%

import matplotlib.pyplot as plt

plt.hist(df['logPontos'])
plt.grid(True)
plt.show()