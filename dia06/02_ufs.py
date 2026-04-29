# %%

import pandas as pd

uf = pd.read_csv('../data/ufs.csv')

uf

# %%

def str_to_float(x:str):
    x = (x.replace(' ','')
          .replace(',', '.')
        )
    return float(x)

numero = '251 529,2'

str_to_float(numero)

# %%

uf['Área (km²)'] = uf['Área (km²)'].apply(str_to_float)
uf['População (Censo 2022)'] = uf['População (Censo 2022)'].apply(str_to_float)
uf['PIB (2015)'] = uf['PIB (2015)'].apply(str_to_float)
uf['PIB per capita (R$) (2015)'] = uf['PIB per capita (R$) (2015)'].apply(str_to_float)
uf['IDH (2010)'] = uf['IDH (2010)'].apply(str_to_float)


uf
# %%

def str_to_float_expecVida(x:str):
    x = (x.replace(',', '.')
         .replace(' anos', ''))
    return float(x)

uf['Expectativa de vida (2016)'] = uf['Expectativa de vida (2016)'].apply(str_to_float_expecVida)

# %%

def alfabetizacao(x:str):
    x = (x.replace('%', '')
         .replace(',', '.'))
    
    return float(x) / 100 

uf['Alfabetização (2016)'] = uf['Alfabetização (2016)'].apply(alfabetizacao)

# %%

def uf_to_regiao(uf:str):
    if uf in ['Distrito Federal', 'Mato Grosso']:
        return 'Centro-Oeste'
    
    elif uf in ['Aloagas', 'Bahia']:
        return 'Nordeste'

uf['Região'] = uf['Unidade federativa'].apply(uf_to_regiao)

uf

# %%

# Se PIB / Capita > 30k e Mortalidade < 15 / 1k e IDH > 700 -> 'parece bom' else 'nao parece bom'

def mortalidade_to_float(x:str):
    x = (x.replace('‰', '')
         .replace(',', '.')
         )
    
    return float(x)

uf['Mortalidade infantil (/1000)'] = uf['Mortalidade infantil (2016)'].apply(mortalidade_to_float)
# %%

def classifica_bom(linha):
    return (linha['PIB per capita (R$) (2015)'] > 30000 and 
            linha['Mortalidade infantil (/1000)'] < 15 and 
            linha['IDH (2010)'] > 0.700)

# %%

uf.apply(classifica_bom, axis=1)

# %%

# quando usa axis = 0 passa as colunas quando passa axis = 1 passa as linhas
uf.apply(lambda x: print(x), axis=1)

# %%

