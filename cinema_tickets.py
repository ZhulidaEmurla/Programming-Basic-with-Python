student_ticket = 0
standard_ticket = 0
kid_ticket = 0
name_of_film = input()

while name_of_film != "Finish":
    free_seats = int(input())
    sold_seats = 0
    for free_ticket in range(free_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student_ticket += 1
        elif current_ticket == "standard":
            standard_ticket += 1
        elif current_ticket == "kid":
            kid_ticket += 1
        sold_seats += 1
    percent_full_hall = sold_seats / free_seats * 100
    print(f"{name_of_film} - {percent_full_hall:.2f}% full.")
    name_of_film = input()
total_sold_tickets = student_ticket + standard_ticket + kid_ticket
percent_student_tickets = student_ticket / total_sold_tickets * 100
percent_standard_tickets = standard_ticket / total_sold_tickets * 100
percent_kid_tickets = kid_ticket / total_sold_tickets * 100
print(f"Total tickets: {total_sold_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")

