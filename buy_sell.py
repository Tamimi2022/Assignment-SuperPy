import os
import pandas as pd

# For Buy recording
def b_recording(id, product, price, quantity, buy_date, exp_date):
    
    #  Check recording buy , if not eixst Create one
    if os.path.isfile('df_bought.csv') == False:
        df_bought = pd.DataFrame(columns=['ID', 'Product_name', 'Buy_price', 'Quantity', 'Buy_date', 'Expiration_date'])
        
    #  Create new recording + Append
        new_record = {'ID': id, 'Product_name': product, 'Buy_price': price, 'Quantity': quantity, 'Buy_date': buy_date, 'Expiration_date': exp_date}
        
        df_bought = df_bought.append(new_record, ignore_index=True)
        print(product + ' was added to BUY')
        return df_bought.to_csv('df_bought.csv', index=False)
    
    elif os.path.isfile('df_bought.csv'):
        df_bought = pd.read_csv('df_bought.csv')
        
    #   Create + Append to existing file
        new_record = {'ID': id, 'Product_name': product, 'Buy_price': price, 'Quantity': quantity, 'Buy_date': buy_date, 'Expiration_date': exp_date}
        
        df_bought = df_bought.append(new_record, ignore_index=True)
        print(product + ' was added to BUY')
        return df_bought.to_csv('df_bought.csv', index=False)
    
# For Sell recording
def s_recording(id, product, price,sell_date, quantity):
    
    #  Check recording sell , if not eixst Create one
    if os.path.isfile('df_sold.csv') == False:
        df_sold = pd.DataFrame(columns=['ID', 'Product_name', 'Sell_price', 'Quantity', 'Sell_date'])
        
    #  Create new recording + Append
        new_record = {'ID': id, 'Product_name': product, 'Sell_price': price, 'Quantity': quantity, 'Sell_date': sell_date}
        
        df_sold = df_sold.append(new_record, ignore_index=True)
        print(product + ' was added to SELL')
        return df_sold.to_csv('df_sold.csv', index=False)
    
    elif os.path.isfile('df_sold.csv'):
        df_sold = pd.read_csv('df_sold.csv')
        
    #   Create + Append to existing file
        new_record = {'ID': id, 'Product_name': product, 'Sell_price': price, 'Quantity': quantity, 'Sell_date': sell_date}
        
        df_sold = df_sold.append(new_record, ignore_index=True)
        print(product + ' was added to SELL')
        return df_sold.to_csv('df_sold.csv', index=False)
        