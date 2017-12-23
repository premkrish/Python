# number formatting (as is)
print('-----------------------------------------')
print("Numbers")
num1 = 3.14256789023
num2 = 24.4175643
print(f'Number 1 is {num1} and Number 2 is {num2}')

# number formatting 4 numbers only
print('-----------------------------------------')
print("Four Numbers")
num1 = 3.14256789023
num2 = 24.4175643
print(f'Number 1 is {num1:.4} and Number 2 is {num2:.4}')

# number formatting 2 decimal places only
print('-----------------------------------------')
print("Two decimal places")
num1 = 3.14256789023
num2 = 24.4175643
print(f'Number 1 is {num1:.2f} and Number 2 is {num2:.2f}')

#datetime formats
from datetime import date, time, datetime
today = datetime.today()
current_time = datetime.now()
utc_time = datetime.utcnow().strftime('%m%d%Y_%H%M%S')
print('-----------------------------------------')
print("Date formatting")
print(f'Today\'s date is {today}')
print(f'Current time is {current_time}')
print(f'UTC time is {utc_time}')
print(f'Today\'s day is {current_time.day}')
print(f'Today\'s month is {current_time.month}')
print(f'Today\'s year is {current_time.year}')
print("Today's date in MM/dd/YYYY format " + current_time.strftime('%m/%d/%Y'))
