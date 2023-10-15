start = int(input())
final = int(input())
magic = int(input())
is_found = False
counter = 0

for i in range(start, final + 1):
    if is_found:
        break
    for j in range(start, final + 1):
        if is_found:
            break
        counter += 1
        if i + j == magic:
            print(f"Combination N:{counter} ({i} + {j} = {magic})")
            is_found = True
if not is_found:
    print(f"{counter} combinations - neither equals {magic}")