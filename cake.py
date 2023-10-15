
width = int(input())
length = int(input())
number_of_pieces = True
total_volume_of_cake = width * length
need = input()

while need != "STOP":
    current_number_of_pieces = int(need)
    total_volume_of_cake -= current_number_of_pieces
    if total_volume_of_cake < 0:
        number_of_pieces = False
        break
    need = input()
if number_of_pieces:

    print(f"{total_volume_of_cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_volume_of_cake)} pieces more.")
