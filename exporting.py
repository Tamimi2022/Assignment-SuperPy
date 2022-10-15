import os
import pandas as pd
from date_record import is_date_record
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

custom_theme = Theme({'OK': 'green', 'error': 'red'})
console = Console(theme=custom_theme)
Table(show_lines=True, header_style='green')

# Exporting selections of data to CSV files
def exporting(selection, date):
    if is_date_record(date) == False:
        console.print('Incorrect date str format')
        return
    elif is_date_record(date) == True:
        date = pd.to_datetime(date)
        
    if selection == 'expired':
        if os.path.isfile('df_inventory.csv') == False:
            console.print('No data in current inventory')
        elif os.path.isfile('df_inventory.csv'):  # Create new one
            df_inventory = pd.read_csv('df_inventory.csv')
            df_inventory['Expiration_date'] = pd.to_datetime(df_inventory['Expiration_date'], format='%Y-%m-%d')
            df_inventory['Expired'] = df_inventory['Expiration_date'] < date
            
            # Selection
            df_inventory_selection = df_inventory[df_inventory['Expired'] == True]
            if df_inventory_selection.empty:
                console.print('No expired product at this date')
            else:
                console.print('Data exported to expired.csv')
                console.print(df_inventory_selection.to_string(index=False))
                console.print('Expired products on selected date:') #check
                return df_inventory_selection.to_csv('expired.csv', index=False)
       # For Bought       
    if selection == 'bought':
        if os.path.isfile('df_bought.csv') == False:
            console.print('No data')
        elif os.path.isfile('df_inventory.csv'):
            df_bought = pd.read_csv('df_bought.csv')
            df_bought['Buy_date'] = pd.to_datetime(df_bought['Buy_date'])
            df_bought['Bought'] = df_bought['Buy_date'] <= date  # Create new one
            df_bought_selection = df_bought[df_bought['Bought'] == True]
            if df_bought_selection.empty:
                console.print('No bought product for this date')
            else:
                console.print('Data exported to df_bought.csv')
                console.print(df_bought_selection.to_string(index=False))
                console.print('Bought product on:')
                return df_bought_selection.to_csv('df_bought.csv', index=False)

        # For Sold
    if selection == 'sold':
        if os.path.isfile('df_sold.csv') == False:
            console.print('No data')
        elif os.path.isfile('df_sold.csv'):
            df_sold = pd.read_csv('df_sold.csv')
            df_sold['Sell_date'] = pd.to_datetime(df_sold['Sell_date'])
            df_sold['Sold'] = df_sold['Sell_date'] <= date
            df_sold_selection = df_sold[df_sold['Sold'] == True]
            if df_sold_selection.empty:
                console.print('No sold product for this date')
            else:
                console.print('Data exported to df_sold.csv')
                console.print(df_sold_selection.to_string(index=False))
                console.print('Sold product on:')
                return df_sold_selection.to_csv('df_sold.csv', index=False)