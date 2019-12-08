import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import common

###
#   Gera um gráfico de barras horizontal.
#   Configurações:
#       - arquivo
#       - Filtros disponíveis:
#            - x
#            - y
#            - z
###
def generate(configuration):
    print(" - Ploting Horizontal Bar")
    file_data = common.read_file(configuration["file"])
    data = generate_dataset(file_data[configuration["fields"]], configuration["data_generator"])
    generate_plot(data, configuration["outputfile"], configuration["graphic"])

# Gerar o dataset para montar o gráfico
def generate_dataset(file_data, configuration):
    filtered_data = common.filter_dataset(file_data, configuration)
    
    #grouper
    grouped_data = filtered_data.groupby(configuration["groupers"]).agg(configuration["agg"])

    return pd.DataFrame(grouped_data)

# Gerar o grafico para ver a média de cada requisição de primitive.
def generate_plot(data, output_file, graphic):
    width_in_inches = 12
    height_in_inches = 8
    font_size = 12

    data.plot(kind='barh', figsize=(width_in_inches, height_in_inches))
    plt.title(graphic["title"])
    plt.xlabel(graphic["xlabel"])
    plt.ylabel(graphic["ylabel"])

    plt.tick_params(labelsize=8)
    plt.rc('font', size=font_size)          # controls default text sizes
    plt.rc('axes', titlesize=font_size)     # fontsize of the axes title
    plt.rc('axes', labelsize=font_size)     # fontsize of the x and y labels
    plt.rc('xtick', labelsize=font_size)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=font_size)    # fontsize of the tick labels
    plt.rc('legend', fontsize=font_size)    # legend fontsize
    plt.rc('figure', titlesize=font_size)   # fontsize of the figure title
    plt.tight_layout()
    font = {'family' : 'Helvetica', 'size'   : font_size}
    mpl.rcParams.update({'font.size': font_size})
    mpl.rc('font', **font)

    if(output_file):
        plt.savefig(output_file)
        
    plt.show()
