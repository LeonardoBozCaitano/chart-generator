import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import statistics
import common

###
#   Gera um gráfico de barras.
#   Configurações:
#       - arquivo
#       - Filtros disponíveis:
#            - x
#            - y
#            - z
###
def generate(configuration):
    print(" - Ploting Chart")

    plt.rcdefaults()
    fig, ax = plt.subplots()
    i = 0
    for file in configuration["files"]:
        file_data = common.read_file(file)
        data = generate_data(file_data, configuration["data_generator"])
        rect = ax.bar(i, data*(i+1))
        autolabel(ax,rect)
        i = i + 1

    #custom_lines = [Patch(edgecolor="black"),
    #                Patch(edgecolor="black")]
    #ax.legend(custom_lines, ['CPU(20 Threads)', '1 GPU'])

    plt.xticks(np.arange(i), configuration["labels"])

    plt.title('Média de latência por quantidade de usuarios')
    plt.xlabel('Quantidade de usuarios')
    plt.ylabel('Tempo')

    if(configuration["outputfile"]):
        plt.savefig(configuration["outputfile"])

    plt.show()
    return 1

# Gerar o dataset para montar o gráfico
def generate_data(file_data, configuration):
    filtered_data = common.filter_dataset(file_data, configuration)["latency"]
    
    #grouper
    grouped_data = filtered_data.agg({'latency':'median'})

    dataSetResult = statistics.median(grouped_data)

    return dataSetResult

#Attach a text label above each bar displaying its height
def autolabel(ax,rects):
    hfont2 = {'fontname':'Helvetica','fontsize':12}
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2. - .13, 1.0*height + 3,
                '{:10.2f}'.format(round(height,2)),
                ha='center', va='bottom',**hfont2)
