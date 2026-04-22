# %%

idades = [ 32, 38, 30, 31 ]

import pandas as pd

series_idades = pd.Series(idades)
series_idades

# %%

idades[-1]
series_idades[0]

# %%

series_idades[len(series_idades)-1]

# %%

series_idades = series_idades.sort_values()
series_idades

# %%

series_idades.iloc[-1]

# %%
series_idades.iloc[::-1]

# %%

idades = [ 32, 38, 30, 31 ]

indexs = ["Teo", "Maria", "Jose", "Luis"]

series_idades = pd.Series(idades, index=indexs)

series_idades["Maria"]

series_idades.iloc[[0]]

# %%

series_idades.loc[["Teo"]]
