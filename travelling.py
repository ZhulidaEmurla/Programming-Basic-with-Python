save_money = 0

while True:
    town = input()
    if town == "End":
        break
    price = float(input())
    save_money = 0
    while True:
        income = float(input())
        save_money += income
        if save_money >= price:
            print(f"Going to {town}!")
            break
