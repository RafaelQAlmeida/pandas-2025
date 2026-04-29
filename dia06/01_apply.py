# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')

# %%

idCliente = '000ff655-fa9f-4baa-a108-47f581ec52a1'

idCliente.split("-")[-1]

def get_last_id(x):
    return x.split('-')[-1]

get_last_id('000ff655-fa9f-4baa-a108-47f581ec52a1')

# %%

id_novo = []

# uma maneira de aplicar alteracoes para toda uma lista pode ser assim se for manual
for i in df['idCliente']:
    id_novo.append( get_last_id(i) )

id_novo

df['novo_id'] = id_novo

df.head()

# %%

# mas a melhor maneira de se trabalhar com alteracoes assim eh usando .apply
# para isso eh importante que o metodo get_last_id receba apenas um parametro
df['idCliente'].apply(get_last_id) # uma maneira de aplicar metodos/alteracoes elemento a elemento


# %%

