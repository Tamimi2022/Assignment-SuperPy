import os
import pandas as pd
from date_record import is_date_record
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

custom_theme = Theme({'OK': 'green', 'error': 'red'})
console = Console(theme=custom_theme)
Table(show_lines=True, header_style='green')

# Calculate 
def profit_record(input_date):
    if is_date_record(input_date) == False: # Check if in correct format YYYY-MM-DD
        console.print('Incorrect format date str')
        return
    elif is_date_record(input_date) == True:
        input_date = pd.to_datetime(input_date)
    # Check Transactions 
    if os.path.isfile('df_sold.csv') == False:  # to Sold
        console.print('Nothing in Sold')
    if os.path.isfile('df_bought.csv') == False:  # to Bought
        console.print('Nothing in Bought')
    elif os.path.isfile('df_sold.csv') & os.path.isfile('df_bought.csv'):
        df_sold = pd.read_csv('df_sold.csv')
        df_bought = pd.read_csv('df_bought.csv')
        
        # Buy
        df_bought['Buy_date'] = pd.to_datetime(df_bought['Buy_date'])
        df_bought['Bought'] = input_date >= df_bought['Buy_date']
        b_calculate = df_bought[df_bought['Bought'] == True]
        
        # Sell
        df_sold['Sell_date'] = pd.to_datetime(df_sold['Sell_date'])
        df_sold['Sold'] = input_date >= df_sold['Sell_date']
        s_calculate = df_sold[df_sold['Sold'] == True]
        
        # Calculate Costs -- Bought
        b_calculate['Buy_price'] = pd.to_numeric(b_calculate['Buy_price'])
        b_calculate['Quantity'] = pd.to_numeric(b_calculate['Quantity'])
        b_calculate['Costs'] = (b_calculate['Quantity'] * b_calculate['Buy_price'])
        
        # Calculate Benefit -- Sold
        s_calculate['Sell_price'] = pd.to_numeric(s_calculate['Sell_price'])
        s_calculate['Quantity'] = pd.to_numeric(s_calculate['Quantity'])
        s_calculate['Benefit'] = s_calculate['Quantity'] * s_calculate['Sell_price']
        
        # Total all Profit
        costs = b_calculate['Costs'].sum()
        benefit = s_calculate['Benefit'].sum()
        profit = benefit - costs
        date = input_date.strftime('%Y-%m-%d')
        
        if int(benefit) == 0:
            console.print("No products sold before or on:" + " " + date)
        if int(costs) == 0:
            console.print("No products bought before or on:" + " " + date)
        else:
            console.print("Products bought before or on:" + " " + date)
            console.print(b_calculate)
            console.print("Products sold before or on:" + " " + date)
            console.print(s_calculate)
            console.print("costs:" + str(costs))
            console.print("benefit:" + str(benefit))
            console.print("profit:" + str(profit))