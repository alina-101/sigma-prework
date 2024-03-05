from datetime import datetime, date, time, timezone
today = date.today()
date_str = input("Please input a date in the form dd-mm-yyyy: ")
user_date = datetime.strptime(date_str, '%m-%d-%Y').date()
age = today.year - user_date.year
if user_date.month > today.month:
  age -=1
elif user_date.month == today.month:
  if user_date.day > today.day:
    age -=1
return age