import os
import pandas as pd
from date_record import date_record


# Exporting selections of data to CSV files
def exporting(selection, date):
    if date_record(date) == False:
        print('Incorrect date str format')
        return
    elif date_record(date) == True:
        date = pd.to_datetime(date)
        
    if selection == 'expired':
        if os.path.isfile('df_inventory.csv') == False:
            print('No date in current inventory')
        elif os.path.isfile('df_inventory.csv'):  # Create new one
            df_inventory = pd.read_csv('df_inventory.csv')
            df_inventory['Expiration_date'] = pd.to_datetime(df_inventory['Expiration_date'], format='%Y-%m-%d')
            df_inventory['Expired'] = df_inventory['Expiration_date'] < date
            
            # Selection
            df_inventory_selection = df_inventory[df_inventory['Expired'] == True]
            if df_inventory_selection.empty:
                print('No expired product for now')
            else:
                print('Data exported to expired.csv')
                print(df_inventory_selection.to_string(index=False))
                print('Data exported')
                return df_inventory_selection.to_csv('expired.csv', index=False)
       # For Bought       
    if selection == 'bought':
        if os.path.isfile('df_bought.csv') == False:
            print('No data')
        elif os.path.isfile('df_inventory.csv'):
            df_bought = pd.read_csv('df_bought.csv')
            df_bought['Buy_date'] = pd.to_datetime(df_bought['Buy_date'])
            df_bought['Bought'] = df_bought['Buy_date'] <= date  # Create new one
            df_bought_selection = df_bought[df_bought['Bought'] == True]
            if df_bought_selection.empty:
                print('No bought product for this date')
            else:
                print('Data exported to bought.csv')
                print(df_bought_selection.to_string(index=False))
                print('Bought product on:')
                return df_bought_selection.to_csv('bought.csv', index=False)

        # For Sold
    if selection == 'sold':
        if os.path.isfile('df_sold.csv') == False:
            print('No data')
        elif os.path.isfile('df_sold.csv'):  # Check
            df_sold = pd.read_csv('df_sold.csv')
            df_sold['Sell_date'] = pd.to_datetime(df_sold['Sell_date'])
            df_sold['Sold'] = df_sold['Sell_date'] <= date
            df_sold_selection = df_sold[df_sold['Sold'] == True]
            if df_sold_selection.empty:
                print('No sold product for now')
            else:
                print('Data exported to sold.csv')
                print(df_sold_selection.to_string(index=False))
                print('Sold product on:')
                return df_sold_selection.to_csv('sold.csv', index=False)