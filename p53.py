# 53. Display Calendar of a Given Month and Year
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
print(calendar.month(year, month))
