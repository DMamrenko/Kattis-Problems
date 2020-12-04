#Datum
import datetime
inp = [int(s) for s in input().split()]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[datetime.date(2009, inp[1], inp[0]).weekday()])
