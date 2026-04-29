# %%

# 05.05 - Selecione a primeira transacao diaria de cada cliente

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()

transacoes['data'] = pd.to_datetime(transacoes['DtCriacao']).dt.date

transacoes = transacoes.sort_values('DtCriacao')
transacoes.drop_duplicates(keep='first', subset=['IdCliente', 'data'])

# %%

first = (transacoes.sort_values('DtCriacao')
        .drop_duplicates(keep='first', subset=['IdCliente', 'data']))

last = (transacoes.sort_values('DtCriacao')
        .drop_duplicates(keep='last', subset=['IdCliente', 'data']))
