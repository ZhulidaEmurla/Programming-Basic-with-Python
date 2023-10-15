number_of_floor = int(input())
number_of_rooms = int(input())

for f in range(number_of_floor, 0, -1):
    for r in range(number_of_rooms):
        if f == number_of_floor:
            print(f"L{f}{r} ", end="")

        elif f % 2 == 0:
            print(f"O{f}{r} ", end="")

        else:
            print(f"A{f}{r} ", end="")

    print()
