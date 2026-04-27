# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=";")
df.head()

# %%

# list comprehencions TODO Pesquisar
valores_50_mais = [i for i in pontos if i >= 50]

valores_50_mais

# %%

pontos = [10, 1, 1, 1, 50 ,100 ,130 ,1 ,1 ,30 ,25 ,50]

filtro = []

valores_50_mais = []

# aqui primeiro adiciona apenas o booleano se atende ou nao a condicao
for i in pontos:
    filtro.append(i>=50)

resultado = []

for i in range(len(pontos)):
    # aqui considerando os booleanos faz o match com os pontos e adiciona ao resultado
    if filtro[i]:
        resultado.append(pontos[i])

resultado

# %%

brinquedo = pd.DataFrame(
    {
        'nome' : ['teo', 'nah', 'mah'],
        'idade' : [32, 35, 14],
        'uf' : ['sp', 'pr', 'rj'],
    }
)

# pandas já faz a comparacao para toda a serie elemento por elemento
filtro = brinquedo['idade'] >= 18

# passando o filtro retorna os elementos comparando com o booleano do filtro
brinquedo[filtro]

# da pra fazer assim tambem, sem a necessidade de uma variavel para isso, precisa sempre ter o mesmo tamanho
brinquedo[brinquedo['idade'] >= 18]

brinquedo[brinquedo['nome'] != 'teo']

# %%

df = pd.read_csv('../data/transacoes.csv', sep=";")

df.head()

df[df['QtdePontos'] >= 50]

# %%

# fitro com mais de uma condicao

filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100)

df[filtro]

# multiplicador no caso de booleano é AND mas pode usar tambem & (pq multiplica True e False)
df[(df['QtdePontos'] >= 50) * (df['QtdePontos'] < 100)]

# &&

# soma no caso de booleano é OR mas pode usar tambem | (pq somando True com False é True)
filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)

df[filtro]

# %%

filtro = (df['QtdePontos'] > 0) & (df['QtdePontos'] <= 50) & (df['DtCriacao'] >= '2026-01-01')

df[filtro]

