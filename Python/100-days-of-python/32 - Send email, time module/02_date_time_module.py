import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday() # dan u nedelji kao broj
print(year, type(now), type(year)) # 2022 <class 'datetime.datetime'> <class 'int'>

if year == 2022:
    print("Year is 2022")

# Create datetime
date_of_birth = dt.datetime(year=2000, month=12, day=22) # hour minute... are optional
print(date_of_birth)