import datetime

current_date = datetime.date.today()
print(current_date)

current_year = current_date.year
print(current_year)

current_month = current_date.month
print(current_month)

current_day = current_date.day
print(current_day)

#formatted output
print(current_date.strftime('%Y-%m-%d'))


#now gives the date and time both
print(datetime.datetime.now())

#get current day as string
date_time = datetime.datetime.now()
print('current day is', date_time.strftime('%A'))

#current month as string
print('current month is', date_time.strftime('%B'))