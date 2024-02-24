from datetime import datetime


a = datetime.now()

# print(str(a.day) + "." + str(a.month) + "." + str(a.year))

print(a.strftime("%Y-%m-%d"))