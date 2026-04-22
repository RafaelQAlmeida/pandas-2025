# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", delimiter=";")
df

# %%

df.to_parquet("clientes.parquet", index=False)

# %%

df_2 = pd.read_parquet("clientes.parquet")
df_2

# %%

df.to_excel("clientes.xlsx", index=False)

# %% 

import openpyxl

df_3 = pd.read_excel("cleintes.xlsx")