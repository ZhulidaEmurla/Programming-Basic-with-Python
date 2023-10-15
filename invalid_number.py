user_input = int(input())

is_valid = (100 <= user_input <= 200) or user_input == 0

if not is_valid:
    print("invalid")
