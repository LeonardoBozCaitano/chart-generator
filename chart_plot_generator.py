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
        add_bar(ax, rect)
        i = i + 1

    #custom_lines = [Patch(edgecolor="black"),
    #                Patch(edgecolor="black")]
    #ax.legend(custom_lines, ['CPU(20 Threads)', '1 GPU'])

    plt.xticks(np.arange(i), configuration["labels"])

    plt.title(configuration["graphic"]["title"])
    plt.xlabel(configuration["graphic"]["xlabel"])
    plt.ylabel(configuration["graphic"]["ylabel"])

    if(configuration["outputfile"]):
        plt.savefig(configuration["outputfile"])

    plt.show()
    return 1

# Gerar o dataset para montar o gráfico
def generate_data(file_data, configuration):
    column = configuration["groupers"]["column"]

    filtered_data = common.filter_dataset(file_data, configuration)
    filtered_data = filtered_data[column]

    if(configuration["agg"]):
         filtered_data.agg(configuration["agg"])

    #grouper
    grouped_data = filtered_data

    # Median (middle value) of data.
    if (configuration["groupers"]["type"]=="median"):
        dataSetResult = statistics.median(grouped_data)
        
    # Arithmetic mean (“average”) of data.
    if (configuration["groupers"]["type"]=="mean"):
        dataSetResult = statistics.mean(grouped_data)
    
    return dataSetResult

#add bar
def add_bar(ax,rects):
    hfont2 = {'fontname':'Helvetica','fontsize':12}
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2. - .13, 1.0*height + 3,
                '{:10.2f}'.format(round(height,2)),
                ha='center', va='bottom',**hfont2)
