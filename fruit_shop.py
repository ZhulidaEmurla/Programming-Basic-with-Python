fruit = input()
day = input()
qty = float(input())
total = 0
is_input_correct = True

# Logic
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        total = qty * 2.5
    elif fruit == 'apple':
        total = qty * 1.2
    elif fruit == 'orange':
        total = qty * 0.85
    elif fruit == 'grapefruit':
        total = qty * 1.45
    elif fruit == 'kiwi':
        total = qty * 2.7
    elif fruit == 'pineapple':
        total = qty * 5.5
    elif fruit == 'grapes':
        total = qty * 3.85
    else:
        is_input_correct = False

elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        total = qty * 2.7
    elif fruit == 'apple':
        total = qty * 1.25
    elif fruit == 'orange':
        total = qty * 0.9
    elif fruit == 'grapefruit':
        total = qty * 1.6
    elif fruit == 'kiwi':
        total = qty * 3
    elif fruit == 'pineapple':
        total = qty * 5.6
    elif fruit == 'grapes':
        total = qty * 4.2
    else:
        is_input_correct = False
else:
    is_input_correct = False

# Print output

if is_input_correct:
    print(f'{total:.2f}')
else:
    print('error')

