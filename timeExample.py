from datetime import datetime, timedelta

# get current datetime
dt = datetime.now()
print(dt.minute)
birthday= input ("give me your birthday")
b_date=datetime.strptime(birthday,"%d/%m/%Y" )
# print('Datetime is:', dt.day)
# dt_2 = dt.replace(hour=6)

# print(dt)
# print(dt.replace(hour=6))
# print(dt_2)
x=timedelta(days=1)
for i in range (0,10):
    print (dt+x)
    dt = dt + x
