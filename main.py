#custom
import bar_plot_generator
import chart_plot_generator
import json 
from pprint import pprint

def main():
    # configuração para plot
    with open('configuration.json') as f:
        configuration = json.load(f)

    print("# Process running... ")

    if(configuration["bar"]["plot"]=='true'):
        bar_plot_generator.generate(configuration["bar"])

    if(configuration["chart"]["plot"]=='true'):
        chart_plot_generator.generate(configuration["chart"])
    
    print("# Stoping... ")

#init
main()