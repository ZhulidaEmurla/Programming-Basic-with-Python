days = int(input())
type = input()
ocenka = input()
night = days - 1
price = 0
percent = 0
if type == "room for one person":

    price = night * 18
elif type == "apartment":
    price = night * 25
    if days < 10:
        percent = price * 0.3
        price -= percent
    elif days > 15:
        percent = price * 0.5
        price -= percent
    else:
        percent = price * 0.35
        price -= percent

elif type == "president apartment":
    price = night * 35
    if days < 10:
        percent = price * 0.1
    elif days > 15:
        percent = price * 0.2
        price -= percent
    else:
        percent = price * 0.15
        price -= percent

if ocenka == "positive":
    percent = price * 0.25
    price += percent

else:
    percent = price * 0.1
    price -= percent
print(f"{price:.2f}")







