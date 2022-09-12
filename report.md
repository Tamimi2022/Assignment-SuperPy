First of all:  I want to inform that I keep using 'main.py' and not changing to 'super.py' . So all Commands use/with 'main.py' .

For me 'Python' is something new and fun with all libraries, make me curious. So I dissected and explored 3 modules in this project csv - argparse - datetime. My first step is planning, get started with argparse and build the foundation for make the command. As well as build and opening multiple .csv files. And how to set times and the inventory. I learned how to make (plotx,y) in matplothib, and solve the problem of warnings message that often appear in python for example with: pd.options.mode.chained_assignment, other example: 'DataFrame' and so on. Also like 'Pandas' and its customization with df = pd.concat... or using .loc . 
I really learned a lot from this project, even I found a new method to maximize the way of learning. 

Note:
Here For all the results of my Command i did before creating a specific date. and now After all the Command instances I ran I created a specific date in the 'date.txt . file

Some examples and more spesific in 'command.txt 

# Profit
Products bought before or on: 2030-10-03
   ID Product_name  Buy_price  ...  Expiration_date Bought Costs
0   1        Apple        5.0  ...       2022-03-04   True   5.0
1   1        Apple        5.0  ...       2022-03-04   True  50.0

[2 rows x 8 columns]
Products sold before or on: 2030-10-03
   ID Product_name  Sell_price  Quantity  Sell_date  Sold  Benefit
0   1        Apple        21.0         1 2025-10-01  True     21.0
1   1        Apple        21.0         3 2025-10-01  True     63.0
costs:55.0
benefit:84.0
profit:29.0

To display the inventory or others not only .csv but also i used a .pdf

When we buy or sell items, the item is placed in a CSV file. To provide these items with a Unique ID, I wrote functionality that the item will always have a unique ID.

For Reset or remove :
 I made several choices, can delete per file and can delete all files
 csv format or pdf format .