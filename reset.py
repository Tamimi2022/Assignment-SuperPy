import os

# Removing all files type
def reset(input):
            # For Bought
    if input == 'bought':
        if os.path.isfile('./df_bought.csv'):
            os.remove('./df_bought.csv')
        if os.path.isfile('./df_bought.pdf'):
            os.remove('./df_bought.pdf')
            
            # For Sold
    elif input == 'sold':
        if os.path.isfile('./df_sold.csv'):
            os.remove('./df_sold.csv')
        if os.path.isfile('./df_sold.pdf'):
            os.remove('./df_sold.pdf')
            
            # For Inventory
    elif input == 'inventory':
        if os.path.isfile('./df_inventory.csv'):
            os.remove('./df_inventory.csv')
        if os.path.isfile('./df_inventory.pdf'):
            os.remove('./df_inventory.pdf')
    else:
        if os.path.isfile('./df_bought.csv'):
            os.remove('./df_bought.csv')
        if os.path.isfile('./df_sold.csv'):
            os.remove('./df_sold.csv')
        if os.path.isfile('./df_inventory.csv'):
            os.remove('./df_inventory.csv')
        if os.path.isfile("./Expired.csv"):
            os.remove("./Expired.csv")