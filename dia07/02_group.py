# %%

import pandas as pd

# %%

transacoes = pd.read_csv('../data/transacoes.csv',sep=';')

transacoes.head()

# %%

# para contar quantas transacoes cada cliente fez
transacoes.groupby(by=['IdCliente']).count()

# %%

# assim calcula apenas a coluna desejada
transacoes.groupby(by=['IdCliente'], as_index=False)[['IdTransacao']].count()

# %%

# como calcular a quantidade  de transacoes, total de pontos e media de pontos por transacao

transacoes 

summary = (transacoes.groupby(by=['IdCliente'], as_index=False)
                        .agg({'IdTransacao' : ['count'],
                             'QtdePontos' : ['sum', 'mean']})

)

summary[('QtdePontos','mean')]

# %%

# fazendo isso nos tiramos o multindex nomeando as colunas para facilitar os calculos
summary.columns = ['IdCliente', 'QtdeTransacao', 'TotalPontos', 'AvgPontos']

summary

# %%
