# Databricks notebook source
import numpy as np

def jogar_2_dados():
    """Simula o lançamento de dois dados de seis lados e retorna a soma dos resultados."""
    dado_1 = np.random.randint(1, 7)
    dado_2 = np.random.randint(1, 7)
    return dado_1 + dado_2

# Simulando 1000 jogadas dos dois dados ao mesmo tempo
simulacoes = 1000
resultados = np.array([jogar_2_dados() for _ in range(simulacoes)])

# Análise dos dados
media_resultados = np.mean(resultados)
lancamento_maximo = np.max(resultados)
lancamento_minimo = np.min(resultados)
lancamentos_contabilizados = np.bincount(resultados)[2:]  # Desconsidera 0 e 1, pois não são possíveis

# Exibindo os resultados
print(f"Média dos resultados: {media_resultados}")
print(f"Lançamento máximo: {lancamento_maximo}")
print(f"Lançamento mínimo: {lancamento_minimo}")
for lancamento, contagem in enumerate(lancamentos_contabilizados, start=2):
    print(f"Número de vezes para o lançamento {lancamento}: {contagem}")

'''
Teste de Hipótese:

    A forma como os resultadors foram apresentados mostra uma tendência maior para somas médias (especialmente 6, 7 e 8), já que existem mais combinações para chegarmos nesses números.

    Me parece que a simulação está alinhada com a hipótese de um jogo justo, pois todos os lançamentos são igualmente prováveis.
    
    Para um jogador é mais provável obter somas médias do que somas muito altas ou muito baixas.

'''


  


# COMMAND ----------


