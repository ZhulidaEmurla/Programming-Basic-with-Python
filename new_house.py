type_flower = input()
number_of_flower = int(input())
budget = int(input())
price_per_flower = 0

if type_flower == "Roses":
    price_per_flower = 5
    if number_of_flower > 80:
        price_per_flower *= 0.9
elif type_flower == "Dahlias":
    price_per_flower = 3.8
    if number_of_flower > 90:
        price_per_flower *= 0.85
elif type_flower == "Tulips":
    price_per_flower = 2.8
    if number_of_flower > 80:
        price_per_flower *= 0.85
elif type_flower == "Narcissus":
    price_per_flower = 3
    if number_of_flower < 120:
        price_per_flower *= 1.15
elif type_flower == "Gladiolus":
    price_per_flower = 2.5
    if number_of_flower < 80:
        price_per_flower *= 1.2

total_sum = price_per_flower * number_of_flower
difference = abs(total_sum - budget)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flower} {type_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")





