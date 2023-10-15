money_of_tereza = float(input())
wins_for_den_of_sale = float(input())
expenses = float(input())
price_of_gift = float(input())

saved_money = 5 * money_of_tereza
won_money = 5 * wins_for_den_of_sale
total_money_saved = saved_money + won_money
total_expenses = total_money_saved - expenses
if total_expenses > price_of_gift:
    print(f"Profit: {total_expenses:.2f} BGN, the gift has been purchased.")

else:
    difference = abs(price_of_gift - total_expenses)
    print(f"Insufficient money: {difference:.2f} BGN.")
    