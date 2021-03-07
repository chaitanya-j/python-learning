from datetime import date
d0 = date(2018, 7, 15)
d1 = date(2017, 6, 14)
delta = d0 - d1
print(f"{delta.days} days of difference")
