import pandas as pd

# Ler arquivo
def read_file(file):
    file_data = pd.read_csv(file)
    file_data['date'] = file_data['date'].astype('datetime64')

    return file_data

# Gerar o dataset para montar o gráfico
def filter_dataset(file_data, configuration):
    filtered_data = file_data
    
    #filters
    if(configuration["filters"]["module"]): #by module
        filtered_data = filtered_data[filtered_data['module']==configuration["filters"]["module"]["value"]]
    
    if(configuration["filters"]["latency"]): #by latency
        if(configuration["filters"]["latency"]["comparator"]=="bigger"):
            filtered_data = filtered_data[filtered_data["latency"]<configuration["filters"]["latency"]["value"]]
        if(configuration["filters"]["latency"]["comparator"]=="lower"):
            filtered_data = filtered_data[filtered_data["latency"]<configuration["filters"]["latency"]["value"]]
    
    if(configuration["filters"]["bytes"]): #by bytes
        if(configuration["filters"]["bytes"]["comparator"]=="bigger"):
            filtered_data = filtered_data[filtered_data["bytes"]>configuration["filters"]["bytes"]["value"]]
        if(configuration["filters"]["bytes"]["comparator"]=="lower"):
            filtered_data = filtered_data[filtered_data["bytes"]<configuration["filters"]["bytes"]["value"]]
    
    return filtered_data
