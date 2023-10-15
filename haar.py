day_normative = int(input())


total = 0

while True:
    t = input()
    if t == "closed":
        break

    if day_normative == total:
        break
    if t == "haircut":
        type_of_haircut = input()
        if type_of_haircut == "mens":
            total += 15
        elif type_of_haircut == "ladies":
            total += 20
        elif type_of_haircut == "kids":
            total += 10
        if day_normative == total:
            break
    elif t == "color":
        type_of_haircut = input()
        if type_of_haircut == "touch up":
            total += 20
        elif type_of_haircut == "full color":
            total += 30
        if day_normative == total:
            break



if day_normative == total:
    print(f"You have reached your target for the day!")
else:
    difference = abs(day_normative - total)
    print(f"Target not reached! You need {difference}lv. more.")

print(f"Earned money: {total}lv.")








