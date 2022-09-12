import os
from matplotlib import pyplot as plt
import pandas as pd

#  For other format and show Bar
def plot_rec(input):
    #  Labels
    data = pd.read_csv('df_' + input +'.csv')
    plot = data.plot.bar(xlabel='Product_name', ylabel='Quantity', rot=45, color='g', title='Overview')
    
    # Check if .pdf exist or create one
    if os.path.isfile('./' + input + '.pdf') == False:
        print('File ./' + input + '.pdf is created')
        plot.get_figure().savefig('./' + input + '.pdf', format='pdf')  #  With attribute 
        plt.show()  # Overview with Green colors
        
    # Remove the existing .pdf and generating new one
    elif os.path.isfile('./' + input + '.pdf') == True:
        os.remove('./' + input + '.pdf')
        print('File ./' + input + '.pdf is updated')
        plot.get_figure().savefig('./' + input + '.pdf', format='pdf')
        #  With attribute 
        plt.show()  # Overview with Green colors