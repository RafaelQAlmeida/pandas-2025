# %%

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')

max_ponto = clientes['qtdePontos'].max()

filtro = clientes['qtdePontos'] == max_ponto

clientes[filtro]

# %%

# Para ordenar um df eu preciso usar o by para definir qual a coluna que sera usada
clientes_ordenados = (clientes.sort_values(by='qtdePontos', ascending=False)
                              .head(5)['idCliente'])

# %%

clientes_ordenados

# %%

brinquedo = pd.DataFrame(

    {

        'nome' : ['Teo', 'Ana', 'Nah', 'Jose'],
        'idade' : [32, 43, 35, 42],
        'salario' : [2345, 4533, 3245, 4533],
    }
)

# Considerando desempates eh so passar no by uma lista e no asceding eu posso passar tambem uma lista
brinquedo.sort_values(by=['salario', 'idade'], ascending=[False, True])


# %%

