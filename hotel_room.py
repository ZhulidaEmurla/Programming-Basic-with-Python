month = input()
nights = int(input())

price_for_studio = 0
price_for_apartment = 0

if month == "May" or month == "October":
    price_for_studio = nights * 50
    price_for_apartment = nights * 65

elif month == "June" or month == "September":
    price_for_studio = nights * 75.20
    price_for_apartment = nights * 68.70

elif month == "July" or month == "August":
    price_for_studio = nights * 76
    price_for_apartment = nights * 77

if nights > 14 and (month == "May" or month == "October"):

    price_for_studio *= 0.70

elif nights > 7 and (month == "May" or month == "October"):

    price_for_studio *= 0.95

elif nights > 14 and (month == "June" or month == "September"):

    price_for_studio *= 0.80

if nights > 14:
    price_for_apartment *= 0.90

print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")







