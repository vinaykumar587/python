#Using Lambda function, extract and print the year from the datetime object given below.

from datetime import datetime

given_date = datetime(2008, 6, 12, 10, 30, 0)

year = lambda x : x.year
print(year(given_date))

