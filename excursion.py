number_of_people = int(input())
number_night = int(input())
number_cards = int(input())
number_tickets_for_museum = int(input())

price_night = number_night * 20
price_cards = number_cards * 1.60
price_tickets = number_tickets_for_museum * 6

total_sum_per_person = price_night + price_cards + price_tickets
total_sum_for_all_group = total_sum_per_person * number_of_people
final_sum = total_sum_for_all_group + (total_sum_for_all_group / 100 * 25)


print(f"{final_sum:.2f}")
