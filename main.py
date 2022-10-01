# Imports
import argparse
import csv
from exporting import *
from datetime import *
from profit_record import *
from plot_rec import plot_rec
from items_to_inventory import buy_items_to_inventory, sell_items_to_inventory
from reset import *
import pandas as pd
from date_record import *
from plot_rec import show_inventory

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    pass

# The Parsers for Command-line
# Creating an Argument Parsers
parser = argparse.ArgumentParser(prog='SuperPy', description='Welcome in my Supermarket')
# Atribute of a positional argument equals
subparsers = parser.add_subparsers(dest='command')


# Usage optional arguments:
parser.add_argument('-a', '--advance-time', type=int, help='advance time with days input: number of days', metavar='')
parser.add_argument('-i', '--input-date', help='give set date input: YYYY-MM-DD', metavar='')

# For Buy
buy_parser = subparsers.add_parser("buy", help="Buy a product")
buy_parser.add_argument('-p', "--product", dest="product", type=str, help="product name", required=True)
buy_parser.add_argument('-b', "--buy-price", type=float, dest="price", help="buy price per product", required=True)
buy_parser.add_argument('-q', "--quantity", type=int, dest="quantity", help="quantity of product", default=1)
buy_parser.add_argument('-d', "--buy-date", type=str, dest="buy_date", help="product buy date (format YYYY-MM-DD)", required=True)
buy_parser.add_argument('-e', "--exp-date", type=str, dest="exp_date", help="product expiration date (format YYYY-MM-DD)", required=True)

# For Sell
sell_parser = subparsers.add_parser("sell", help="Sell a product")
sell_parser.add_argument('-p', "--product", type=str, dest="product", help="product name", required=True)
sell_parser.add_argument('-s', "--sell-price", type=float, dest="price", help="sell price per product", required=True)
sell_parser.add_argument('-q', "--quantity", type=int, dest="quantity", help="quantity of product", default=1)
sell_parser.add_argument('-d', "--sell-date", type=str, dest="sell_date", help="product sell date (format YYYY-MM-DD)", required=True)


# For Export
export_parser = subparsers.add_parser("export", help="Export selection of data on a specific date")
export_parser.add_argument("--file", type=str, dest="file", help="Data to be exported to .csv file", choices=["expired", "bought", "sold"], required=True)
export_parser.add_argument("--date", type=str, dest="date", help="Choose date", required=True)

# For Profit
profit_parser = subparsers.add_parser("profit", help="Calculate profit on a specific date")
profit_parser.add_argument("--date", type=str, dest="date", help="Choose date", required=True)

# For Plot
plot_parser = subparsers.add_parser("plot", help="Plot bar graph of product in inventory, bought / sold list")
plot_parser.add_argument("--file", type=str, dest="file", help="File plotted", choices=["bought", "sold", "inventory"], required=True)

# For Inventory 
inventory_parser = subparsers.add_parser('inventory', help='Product in inventory')
inventory_parser.add_argument("--now", dest='now' , help="Showing inventory at this moment")

# For Reset 
reset_parser = subparsers.add_parser("reset", help="Reset selection of files or all files")
reset_parser.add_argument("--file", type=str, dest="file", help="Files resetted", choices=["bought", "sold", "inventory", "all"], default="all")

args = parser.parse_args()


if args.command is None:
       
        if args.advance_time is not None:
            advance_time(args.advance_time)
        elif args.input_date is not None:
            if len(args.input_date) != 10:
                print('error: use format YYYY-MM-DD')
            elif args.input_date[4] != '-':
                print('error: use format YYYY-MM-DD')
            elif args.input_date[7] != '-':
                print('error: use format YYYY-MM-DD')
            elif args.reset:
                reset_date(args)
            else:
                change_date(args.input_date)
if args.command == "buy":
        buy_items_to_inventory(
            id=id,
            product=args.product,
            quantity=args.quantity,
            price=args.price,
            buy_date=args.buy_date,
            exp_date=args.exp_date
        )
if args.command == "sell":
        sell_items_to_inventory(
            product=args.product,
            price=args.price,
            quantity=args.quantity,
            sell_date=args.sell_date
        )
elif args.command == 'export':
    exporting(selection=args.file, date=args.date)
elif args.command == 'profit':
    profit_record(args.date)
elif args.command == 'plot':
    plot_rec(args.file)
elif args.command == 'inventory':
    show_inventory(args.now)
elif args.command == 'reset':
    reset(args.file)
        
        
if __name__ == "__main__":
    main()