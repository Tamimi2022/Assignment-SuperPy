from datetime import date, datetime, timedelta
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

custom_theme = Theme({'OK': 'green', 'error': 'red'})
console = Console(theme=custom_theme)
Table(show_lines=True, header_style='green')

def is_date_record(date_string):
    try:
        if date_string != datetime.strptime(date_string, '%Y-%m-%d').strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False
    
def reset_date():
    with open('date.txt', 'w') as file:
        today = date.today()
        date_now = today.strftime('%Y-%m-%d')
        file.write(date_now)
        file.close()
        console.print(f"Date set to: {date_now}")

def advance_time(days):
    with open('date.txt', 'r') as f:
        date_string = f.read()
        tdelta = timedelta(days=days)
        date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
        new_time = date_object + tdelta
        new_date_string = new_time.strftime('%Y-%m-%d')
        f.close()
    with open('date.txt', 'w') as file:
        file.write(new_date_string)
        file.close
        console.print(f"Date OK: {new_time}")

def change_date(date):
    with open('date.txt', 'w') as file:
        file.write(date)
        file.close
        date_set = datetime.strptime(date, '%Y-%m-%d').date()
        console.print('Date set to {}'.format(date_set))
        