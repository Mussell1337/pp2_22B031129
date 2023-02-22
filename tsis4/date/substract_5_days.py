import datetime

today = datetime.date.today()
new_date = today - datetime.timedelta(days=5)

print("what day is it today :", today)
print("with substraction to 5 days:", new_date)