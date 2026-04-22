# %%

import pandas as pd

idades = [ 32, 38, 30, 31 ]

nomes  = ["Teo", "Maria", "Jose", "Luis"]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_nomes

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

# %%

df.iloc[-1]["idades"]