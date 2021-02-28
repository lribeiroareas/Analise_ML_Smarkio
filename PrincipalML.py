#Análise explaratória dos dados utilizando estatística descritiva
#Foi utilizado também o pacote xlrd para a leitura do arquivo excel com extensão .xls

import pandas as pd
import numpy as np
import xlrd

from matplotlib import pyplot as plt
from pandas_profiling import ProfileReport
from sklearn.metrics import mean_squared_error
from sklearn.metrics import average_precision_score

#Leitura dos dados a partir do arquivo Excel.
data_set = pd.read_excel("teste_smarkio_lbs.xls")
print(data_set)

#Utilização de comandos da biblioteca do xlrd para manipulação dos dados dentro da planilha.
book = xlrd.open_workbook_xls("teste_smarkio_lbs.xls")
page1 = book.sheet_by_index(0)

#Relatório com a análise descritiva unidimensional exportado para arquivo .html.
profile = ProfileReport(data_set, title = "Análise Exploratória dos Dados")
profile.to_notebook_iframe((output_file="analise_exploratoria_dos_dados.html"))

#Tratamento dos dados para colocá-los em listas.
limit = len(page1.col_values(colx=0)) - 1
print(limit)
i = 1

list_true_class = page1.col_values(start_rowx=1, colx=3)
list_pred_class = page1.col_values(start_rowx=1, colx=0)
print(list_true_class)

while i < limit:
    if list_true_class[i] == "":
        list_true_class[(i)] = list_pred_class[i]
    i = i + 1

new_list_true_class = []
for item in list_true_class:
    new_list_true_class.append(float(item))

list_results = []

while i < limit:
    if list_true_class[i] == list_pred_class[i]:
        list_results[i] = 1
    else:
        list_results[i] = 0
    i = i + 1

#Métrica Mean Squared Error - MER.
result = (mean_squared_error(new_list_true_class, list_pred_class))




