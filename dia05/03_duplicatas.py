# %%

import pandas as pd

# %%

df = pd.DataFrame({
    'nome' : ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    'sobrenome' : ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva','silva', 'silva'],
    'salario' : [2132, 1231, 454, 6543, 6532, 4322, 987, 2134],
})

df

# %%

# mantem apenas o primeiro valor das duplicatas
df.drop_duplicates()

# %%

# mantem apenas a ultima
df.drop_duplicates(keep='last')

# %%

# da mesma forma eh possivel passar as colunas para considerar
df.drop_duplicates(subset=['nome', 'sobrenome'])

# %%

# eh importante ordenar para conseguir pegar last ou first

df = (df.sort_values('salario', ascending=True)
        .drop_duplicates(keep='last', subset=['nome', 'sobrenome']))

df
# %%
