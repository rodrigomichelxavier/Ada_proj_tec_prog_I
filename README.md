# 1. Simulação de Jogo de Dados

## Descrição

Este repositório contém um script Python para simular um jogo de dados. O objetivo é reunir estatísticas para analisar a justiça do jogo, avaliar possíveis resultados e fazer previsões sobre jogos futuros.
Características

Simulação de Dados: Uma função para simular o lançamento de dois dados de seis lados, retornando a soma dos resultados.

Múltiplas Simulações: Simulação de 1000 jogos de dados para coleta de dados estatísticos.

Análise de Dados: Cálculos da média dos resultados, do lançamento máximo e mínimo, e a frequência de cada possível lançamento.

Teste de Hipótese: Análise sobre a justiça do jogo baseada nos resultados da simulação.

## Pré-requisitos

Para executar este script, você precisará do Python instalado em seu ambiente. Além disso, bibliotecas NumPy

    
Como Executar

Clone o repositório para sua máquina local e navegue até o diretório do projeto. Em seguida, execute o script dice_simulation.py usando o Python:

Projeto_Tecnicas_de_Prog_I.py

Resultados

Após a execução, o script irá:

Imprimir a média, o máximo e o mínimo dos resultados dos lançamentos.

Mostrar a frequência de cada possível lançamento.
    
# 2. Exercício Hands On

Hands-On

Você foi designado para realizar a limpeza e preparação de dados de dois conjuntos de dados (base1.csv e base2.csv) distintos que representam informações relacionadas a risco de crédito.

Seu objetivo é ler os dois conjuntos de dados usando a biblioteca Pandas, realizar a concatenação dos dados, lidar com valores duplicados e faltantes, além de verificar a presença de outliers nos dados combinados.

Passos a serem seguidos:
Leitura dos Arquivos: Utilize a biblioteca Pandas para ler os dois arquivos de dados: 'base1.csv' e 'base2.csv', que estão no diretório datasets, no repositório do módulo.
Concatenação dos Dados: Concatene os dois conjuntos de dados em um único DataFrame, verificando se os dados possuem a mesma estrutura para uma concatenação adequada.
Tratamento de Dados Duplicados: Verifique se há linhas duplicadas no DataFrame combinado e remova-as, mantendo a primeira ocorrência.
Tratamento de Valores Faltantes: Identifique e lide com os valores faltantes no DataFrame combinado. Preencha os valores ausentes com estratégias apropriadas (média, mediana, valor específico etc.) dependendo do contexto dos dados.
Verificação de Outliers: Utilize métodos estatísticos ou gráficos (como boxplots) para identificar a presença de outliers nos dados. Considere se eles são significativos para a análise ou se precisam ser tratados de alguma forma.
