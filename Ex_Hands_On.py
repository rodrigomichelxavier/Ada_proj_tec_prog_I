# Databricks notebook source
import pandas as pd

# Aqui vou baixar os dois arquivos do dataset (mas tive q colocar full path pq só o sulfixo não estava rolando)
base1 = pd.read_csv('/Workspace/Repos/rxavier@unimedcampinas.com.br/ADA_classes/DS-PY-Data-Science/DS-PY-004 TÉCNICAS DE PROGRAMAÇÃO I (PY)/Material do Aluno/datasets/base1.csv')
base2 = pd.read_csv('/Workspace/Repos/rxavier@unimedcampinas.com.br/ADA_classes/DS-PY-Data-Science/DS-PY-004 TÉCNICAS DE PROGRAMAÇÃO I (PY)/Material do Aluno/datasets/base2.csv')

base1

# COMMAND ----------


# Aqui juntei as duas bases
dados_combinados = pd.concat([base1, base2], ignore_index=True)

# Aqui removi duplicados
dados_combinados = dados_combinados.drop_duplicates()

# Aqui usei a etsratégia de substituir os valores "na" pela média (não sei se é a melhor estratégia)
dados_combinados.fillna(dados_combinados.mean(), inplace=True)

dados_combinados

# COMMAND ----------

import matplotlib.pyplot as plt

# Aqui eu importei a biblioteca matplotlib pra plotar o gráfico.

dados_combinados.boxplot(figsize = (12 , 6)) #pesquisei no google como muda o tamanho do gráfico pq o rótulo inferior estava encavalado
plt.title("Verificação de Outliers")
plt.show()

# COMMAND ----------


