"""
Criado em Quinta-Feira, 29/12/2022
Autor: Willian Oliveira

Código desenvolvido para criar as bases que serão utilizadas nas análises de distribuição de leitos municipal por ano
e outras análises interativas por meio da ferramenta Tableau Public.

"""

import glob
import pandas as pd

# Carregando o dataset com base nos arquivos csv.
path = 'data'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0, encoding='latin-1')
    li.append(df)

dataset = pd.concat(li, axis=0, ignore_index=True)


# Selecionando variáveis e tratando o tipo das mesmas.
variaveis_obj = dataset.columns.drop(list(dataset.filter(regex='QT')))
dataset[variaveis_obj] = dataset[variaveis_obj].astype(object)
dataset['COMPETEN'] = pd.to_datetime(dataset['COMPETEN'], format='%Y%m')
dataset = dataset.drop(columns={'NATUREZA', 'NIV_HIER', 'RETENCAO', 'ESFERA_A', 'TERCEIRO', 'DISTRSAN', 'DISTRADM', 'MICR_REG', 'REGSAUDE'})


# Reinserindo informações sobre região de saúde de acordo com o CODUFMUN e dados consolidado da Agência Nacional de Saúde Suplementar.
regionais = pd.read_excel('data_pop/regionais-20de-20sade-xls', header=2)
regionais.rename(columns = {'NOME DA REGIÃO DE SAÚDE':'REGSAUDE',
                            'NOME DO MUNICÍPIO':'MUNICIPIO',
                            'CÓD. IBGE DO MUNICÍPIO':'CODUFMUN'}, inplace = True)
regionais = regionais.query("UF == 'GO'").reset_index().drop(columns={'index'})
dataset = pd.merge(dataset, regionais, left_on=['CODUFMUN'], right_on=['CODUFMUN'])


######### Criando o dataset para análises de mapa sobre distribuição regional de Leito Covid-19 #########

dataset_leitos_cov = dataset[dataset['CODLEITO'].isin([51, 52, 96])]
dataset_leitos_cov = dataset_leitos_cov[['COMPETEN',
                                        'QT_SUS',
                                        'QT_EXIST',
                                        'CNES',
                                        'CODLEITO',
                                        'CODUFMUN',
                                        'MUNICIPIO']].groupby(by=['CNES','COMPETEN','CODLEITO','MUNICIPIO','CODUFMUN']).sum().sort_values(by=['CNES','COMPETEN']).reset_index()
dataset_leitos_cov = dataset_leitos_cov.groupby(by=['COMPETEN','MUNICIPIO','CODUFMUN']).sum().sort_values(by=['COMPETEN']).reset_index().drop(columns={'CNES','CODLEITO'})
dataset_leitos_cov['ANO'] = dataset_leitos_cov['COMPETEN'].dt.year.astype(str)
dataset_leitos_cov.to_csv('tableau_datasets/tableau_dataset_leitos_cov.csv',sep=';')

##########################################################################################################

######### Criando o dataset para análises de mapa sobre distribuição regional de Leitos UTI geral #########

dataset_leitos_ger = dataset[dataset['CODLEITO'].isin([74, 75, 76, 77, 78, 80, 81, 82, 83, 85, 86])]
dataset_leitos_ger = dataset_leitos_ger[['COMPETEN',
                                        'QT_SUS',
                                        'QT_EXIST',
                                        'CNES',
                                        'CODLEITO',
                                        'CODUFMUN',
                                        'MUNICIPIO']].groupby(by=['CNES','COMPETEN','CODLEITO','MUNICIPIO','CODUFMUN']).sum().sort_values(by=['CNES','COMPETEN']).reset_index()
dataset_leitos_ger = dataset_leitos_ger.groupby(by=['COMPETEN','MUNICIPIO','CODUFMUN']).sum().sort_values(by=['COMPETEN']).reset_index().drop(columns={'CNES','CODLEITO'})
dataset_leitos_ger['ANO'] = dataset_leitos_ger['COMPETEN'].dt.year.astype(str)
dataset_leitos_ger.to_csv('tableau_datasets/tableau_dataset_leitos_ger.csv',sep=';')

##########################################################################################################

# Criando base de população estimada do Município de acordo com o CODUFMUN, ANO e População estimada que usam como fonte dados 
# tratados da Base dos Dados e a Prévia do Censo de 2022 (Atualizada em 25/12/2022).

pop_mun_2022 = pd.read_excel('data_pop/POP2022_Municipios.xls', header=1, dtype={'COD. UF': str, 'COD. MUNIC': str})
pop_mun_2022 = pop_mun_2022.query("UF == 'GO'").reset_index().drop(columns={'index'})
# Configurando para o mesmo padrão da base do Datasus: Código do município do estabelecimento UF + MUNIC sem dígito.
pop_mun_2022['COD. MUNIC'] = [f"{cod[:-1]}" for cod in pop_mun_2022['COD. MUNIC']]
pop_mun_2022['CODUFMUN'] = [f"{uf}{mun}" for uf,mun in zip(pop_mun_2022['COD. UF'],pop_mun_2022['COD. MUNIC'])]
pop_mun_2022['ANO'] = '2022'
pop_mun_2022 = pop_mun_2022.rename(columns={'POPULAÇÃO':'POPULACAO'})
pop_mun_2022 = pop_mun_2022[['ANO', 'CODUFMUN', 'POPULACAO']]
pop_mun = pd.read_csv('data_pop/base_dos_dados_pop.csv', dtype={'id_municipio':str, 'ano':str}) 
# Configurando para o mesmo padrão da base do Datasus: Código do município do estabelecimento UF + MUNIC sem dígito.
pop_mun['id_municipio'] = [f"{cod[:-1]}" for cod in pop_mun['id_municipio']]
pop_mun = pop_mun.rename(columns={'id_municipio': 'CODUFMUN', 'ano':'ANO', 'populacao':'POPULACAO'})
pop_mun = pop_mun[['ANO', 'CODUFMUN', 'POPULACAO']]
# Consolidando a base para todos os anos.
pop_mun = pd.concat([pop_mun, pop_mun_2022], axis=0).sort_values(['CODUFMUN','ANO']).reset_index().drop(columns={'index'})
pop_mun['POPULACAO'] = pop_mun['POPULACAO'].astype(int)
# Exportando CSV para trabalhar no tableau public.
pop_mun.to_csv('tableau_datasets/tableau_popmun.csv',sep=';')



