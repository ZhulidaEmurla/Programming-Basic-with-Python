bad_grades = int(input())
average_grades = 0
bad_grades_count = 0
total_problems_solved = 0
last_problem_solved = ''
is_failed = False
current_problems = input()
while current_problems != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == bad_grades:
            is_failed = True
            break
    average_grades += current_grade
    total_problems_solved += 1
    last_problem_solved = current_problems
    current_problems = input()
if is_failed:
    print(f'You need a break, {bad_grades_count} poor grades.')
else:
    average_grades /= total_problems_solved
    print(f'Average score: {average_grades:.2f}')
    print(f'Number of problems: {total_problems_solved}')
    print(f'Last problem: {last_problem_solved}')
