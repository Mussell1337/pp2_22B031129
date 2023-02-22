import datetime

date1 = datetime.datetime(2023, 2, 20, 0, 0, 0)
date2 = datetime.datetime(2023, 2, 25, 0, 0, 0)

delta = date2 - date1
diff_in_seconds = delta.total_seconds()

print("The difference between the two dates is", diff_in_seconds, "seconds.")