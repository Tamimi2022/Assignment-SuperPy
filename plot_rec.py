import csv
import os
import sys
from matplotlib import pyplot as plt
import pandas as pd
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

#  For other format and show Bar
def plot_rec(input):
    #  Labels
    data = pd.read_csv('df_' + input +'.csv')
    plot = data.plot.bar(xlabel='Product_name', ylabel='Quantity', rot=45, color='g', title='Overview')
    
    # Check if .pdf exist or create one
    if os.path.isfile('./' + input + '.pdf') == False:
        console.print('File ./' + input + '.pdf is created')
        plot.get_figure().savefig('./' + input + '.pdf', format='pdf')  #  With attribute 
        plt.show()  # Overview with Green colors
        
    # Remove the existing .pdf and generating new one
    elif os.path.isfile('./' + input + '.pdf') == True:
        os.remove('./' + input + '.pdf')
        console.print('File ./' + input + '.pdf is updated')
        plot.get_figure().savefig('./' + input + '.pdf', format='pdf')
        #  With attribute 
        plt.show()  # Overview with Green colors
        
 
 # For Showing df_inventory        
def read_inventory(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        instock = list(reader)
        f.close()
        return instock
        # Using Rich 
custom_theme = Theme({'OK': 'green', 'error': 'red'})
console = Console(theme=custom_theme)
table_inventory = Table(show_lines=True, header_style='green')

def show_inventory(now):
    instock = read_inventory('df_inventory.csv')
    table_inventory.add_column('ID')
    table_inventory.add_column('Product Name')
    table_inventory.add_column('Quantity')
    table_inventory.add_column('Expiration Date')
    for row in (instock[1:]):
        
        table_inventory.add_row(*row)
    console.print(table_inventory)
    print('Showing Inventory in this moment: OK')