import os
import pandas as pd
pd.options.mode.chained_assignment = None  # For ignoring the warning
from buy_sell import b_recording, s_recording
from date_record import date_record

# For Buy
def buy_items(id, product, price, quantity, buy_date, exp_date):
    if (date_record(exp_date) == False) | (date_record(buy_date) == False):
        print('Incorrect format date str')
        return
    if os.path.isfile('df_inventory.csv') == False: 
        df_inventory = pd.DataFrame(columns=['ID', 'Product_name', 'Quantity', 'Expiration_date'])
        
        countrow = df_inventory.shape[0] # Create inventory 
        id = countrow + 1
        new_record = {'ID': id, 'Product_name': product, 'Quantity': quantity, 'Expiration_date': exp_date}
        
        # Append & Print
        df_inventory = pd.concat([df_inventory.append(new_record, ignore_index=True)])
        print(df_inventory.to_string(index=False))
        print(product + 'added to Inventory')
        
        b_recording(id, product, price, quantity, buy_date, exp_date) # Add to list
        return df_inventory.to_csv('df_inventory.csv', index=False)
    elif os.path.isfile('df_inventory.csv'):
        df_inventory = pd.read_csv('df_inventory.csv')
        file_exist = ((df_inventory['Product_name'] == product) & ((df_inventory['Expiration_date'] == exp_date))).any()
    
    # Create new one if not exist
        if file_exist == False:
            countrow = df_inventory.shape[0]
            id = countrow + 1
            new_record = {'ID': id, 'Product_name': product, 'Quantity': quantity, 'Expiration_date': exp_date}
            
            df_inventory = df_inventory.append(new_record, ignore_index=True)
            print(df_inventory.to_string(index=False))
            print(product + 'added to Inventory')
            
            # Add to Bought
            b_recording(id, product, price, quantity, buy_date, exp_date)
            return df_inventory.to_csv('df_inventory.csv', index=False)
        # Updating Quantity of the product
        elif file_exist:
            file_index = df_inventory[((df_inventory['Product_name'] == product) & ((df_inventory['Expiration_date'] == exp_date)))].index.tolist()
            file_index = file_index[0]
            id = int(df_inventory['ID'].iloc[file_index])
            quantity_now = df_inventory['Quantity'].iloc[file_index]
            updating_quantity = int(quantity_now) + int(quantity)
            df_inventory['Quantity'].iloc[file_index] = updating_quantity
            print(product + 'Quantity is updating to', updating_quantity)
            print(df_inventory.to_string(index=False))
            print('Updating inventory')
            
            
            b_recording(id, product, price, quantity, buy_date, exp_date) # Add items
            return df_inventory.to_csv('df_inventory.csv', index=False)
        
# For Sell
def sell_items(product, price, sell_date, quantity):
    if date_record(sell_date) == False:
        print('Incorrect format date str')
        return
    
    # Check inventory
    if os.path.isfile('df_inventory.csv') == False:
        print('Nothing product for now in inventory')
        
    # Check items
    elif os.path.isfile('df_inventory.csv'):
        df_inventory = pd.read_csv('df_inventory.csv')
        df_inventory['Quantity'] = pd.to_numeric(df_inventory['Quantity'])
        file_exist = ((df_inventory['Product_name'] == product) & (df_inventory['Quantity'] >= quantity)).any()
        if file_exist == False:
            print(product + ' ' + 'is not show in inventory')
            
          # File index when the product exist  
        elif file_exist:
            file_index = df_inventory[((df_inventory['Product_name'] == product) & (df_inventory['Quantity'] >= quantity))].index.tolist()
            
            # Sell Producs now
            file_index = file_index[0]
            
            # Check Expiration date
            if pd.to_datetime(df_inventory['Expiration_date'].iloc[file_index], format='%Y-%m-%d') > pd.to_datetime(sell_date, format='%Y-%m-%d'):
                print('All product expired')
            else:
                id = df_inventory['ID'].iloc[file_index]
                s_recording(id, product, price, quantity, sell_date)
                updating_quantity = int(df_inventory['Quantity'].iloc[file_index]) - int(quantity)
                
                # Deleted row when all product sold
                if updating_quantity == 0:
                    df_inventory = df_inventory.drop(df_inventory.index[file_index])
                    print(df_inventory.to_string(index=False))
                    print('Updating Inventory for now:')
                    return df_inventory.to_csv('df_inventory.csv', index=False)
                else:
                    df_inventory['Quantity'].iloc[file_index] = updating_quantity
                    print(df_inventory.to_string(index=False))
                    return df_inventory.to_csv('df_inventory.csv', index=False)