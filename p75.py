# 75. Convert Days to Years, Weeks and Days
days = int(input("Enter number of days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7
print(f"{days} days = {years} year(s), {weeks} week(s), {remaining_days} day(s)")
