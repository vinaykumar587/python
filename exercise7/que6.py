#Write a Python program to find the day of the week for the date given below. Also, we don't know what errors we might encounter while executing the program. So, wrap the code inside a try-except block and handle the exceptions by printing the message 'Oops! An error occurred.'

from datetime import datetime
from calendar import day_name
given_date = datetime(2010,6,12)
try:
    weekday = given_date.weekday()
    weekday = day_name[weekday]
    print(weekday)
except:
    print('Oops! An error occured.')
