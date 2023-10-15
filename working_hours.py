hour_of_date_night = int(input())
day_of_week = input()

if not day_of_week == "Sunday" and 10 <= hour_of_date_night <= 18:
    print("open")
else:
    print("closed")
