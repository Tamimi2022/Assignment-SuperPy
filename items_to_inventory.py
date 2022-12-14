import os
import pandas as pd
pd.options.mode.chained_assignment = None  # For ignoring the warning
from buy_sell import b_recording, s_recording
from date_record import is_date_record
from rich.console import Console
from rich.theme import Theme
from rich.table import Table


custom_theme = Theme({'OK': 'green', 'error': 'red'})
console = Console(theme=custom_theme)
Table(show_lines=True, header_style='green')

# For Buy
def buy_items_to_inventory(id, product, price, quantity, buy_date, exp_date):
    if (is_date_record(exp_date) == False) | (is_date_record(buy_date) == False):
        print('Incorrect format date str')
        return
    if os.path.isfile('df_inventory.csv') == False: 
        df_inventory = pd.DataFrame(columns=['ID', 'Product_name', 'Quantity', 'Expiration_date'])
        
        countrow = df_inventory.shape[0] # Create inventory 
        id = countrow + 1
        new_record = {'ID': id, 'Product_name': product, 'Quantity': quantity, 'Expiration_date': exp_date}
        
        # Append & Print
        df_inventory = pd.concat([df_inventory.append(new_record, ignore_index=True)])
        console.print(df_inventory.to_string(index=False))
        console.print(product + ' added to Inventory')
        
        b_recording(id, product, price, quantity, buy_date, exp_date) # Add to list
        return df_inventory.to_csv('df_inventory.csv', index=False)
    elif os.path.isfile('df_inventory.csv'):
        df_inventory = pd.read_csv('df_inventory.csv')
        file_exist = ((df_inventory['Product_name'] == product) & (df_inventory['Expiration_date'] == exp_date)).any()
    
    # Create new one if not exist
        if file_exist == False:
            countrow = df_inventory.shape[0]
            id = countrow + 1
            new_record = {'ID': id, 'Product_name': product, 'Quantity': quantity, 'Expiration_date': exp_date}
            
            df_inventory = df_inventory.append(new_record, ignore_index=True)
            console.print(df_inventory.to_string(index=False))
            console.print(product + ' added to Inventory')
            
            # Add to Bought
            b_recording(id, product, price, quantity, buy_date, exp_date)
            return df_inventory.to_csv('df_inventory.csv', index=False)
        # Updating Quantity of the product
        elif file_exist:
            file_index = df_inventory[((df_inventory['Product_name'] == product) & (df_inventory['Expiration_date'] == exp_date))].index.tolist()
            file_index = file_index[0]
            id = int(df_inventory['ID'].iloc[file_index])
            quantity_now = df_inventory['Quantity'].iloc[file_index]
            updating_quantity = int(quantity_now) + int(quantity)
            df_inventory['Quantity'].iloc[file_index] = updating_quantity
            console.print(product + 'Quantity is updating to', updating_quantity)
            console.print(df_inventory.to_string(index=False))
            console.print('Updating inventory')
            
            
            b_recording(id, product, price, quantity, buy_date, exp_date) # Add items
            return df_inventory.to_csv('df_inventory.csv', index=False)
        
# For Sell
def sell_items_to_inventory(product, price, sell_date, quantity):
    if is_date_record(sell_date) == False:
        print('Incorrect format date str')
        return
    
    # Check inventory
    if os.path.isfile('df_inventory.csv') == False:
        console.print('Nothing product for now in inventory')
    
    # Check items with Product_name is present in inventory and if quantity is enough
    elif os.path.isfile('df_inventory.csv'):
        df_inventory = pd.read_csv('df_inventory.csv')
        df_inventory['Quantity'] = pd.to_numeric(df_inventory['Quantity'])
        file_exist = ((df_inventory['Product_name'] == product) & ((df_inventory['Quantity'] >= quantity))).any()
        if file_exist == False:
            console.print(product + ' ' + 'is not show in inventory')
            
          # File index when the product exist  
        elif file_exist:
            file_index = df_inventory[((df_inventory['Product_name'] == product) & (df_inventory['Quantity'] >= quantity))].index.tolist()
            
            # Sell Producs now
            file_index = file_index[0]
            
            
            if pd.to_datetime(df_inventory['Expiration_date'].iloc[file_index], format='%Y-%m-%d') == pd.to_datetime(sell_date, format='%Y-%m-%d'):
                console.print('Product Item has been sold:')
            else:
                id = df_inventory['ID'].iloc[file_index]
                s_recording(id, product, price,sell_date, quantity)
                updating_quantity = int(df_inventory['Quantity'].iloc[file_index]) - int(quantity)
                
                # Deleted row when all product sold
                if updating_quantity == 0:
                    df_inventory = df_inventory.drop(df_inventory.index[file_index])
                    console.print('Updating Inventory for now:')
                    console.print(df_inventory.to_string(index=False))
                    return df_inventory.to_csv('df_inventory.csv', index=False)
                else:
                    df_inventory['Quantity'].iloc[file_index] = updating_quantity
                    console.print('Updating Inventory for now:')
                    console.print(df_inventory.to_string(index=False))
                    return df_inventory.to_csv('df_inventory.csv', index=False)