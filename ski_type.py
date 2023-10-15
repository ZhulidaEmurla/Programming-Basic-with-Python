day = int(input())
type_of_room = input()
rating = input()
nights = day - 1
prise_per_night = 0
if type_of_room == "room for one person":
    prise_per_night = 18
elif type_of_room == "apartment":
    prise_per_night = 25
    if nights < 10:
        prise_per_night *= 0.7
    elif nights <= 15:
        prise_per_night *= 0.65
    elif nights > 15:
        prise_per_night *= 0.5
elif type_of_room == "president apartment":
    prise_per_night = 35
    if nights < 10:
        prise_per_night *= 0.9
    elif nights <= 15:
        prise_per_night *= 0.85
    elif nights > 15:
        prise_per_night *= 0.8
total_sum = nights * prise_per_night
if rating == "positive":
    total_sum *= 1.25
elif rating == "negative":
    total_sum *= 0.9
print(f"{total_sum:.2f}")


