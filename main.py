def cgpa_calculator():
    numbers = 70, 60, 50, 45, 40, 39
    a_score, b_score, c_score, d_score, e_score, f_score = numbers
    total_credit_points = 0
    total_number_of_units = 0
    inputs_registered = 0
    number_of_registered_courses = int(input('Enter the number of courses you registered this semester:- '))
    print()
    while number_of_registered_courses > inputs_registered:
        inputs_registered += 1
        course_code = input("Enter the course code: ")
        score = int(input(f'Enter what you scored in {course_code}: '))
        course_unit = int(input(f'Enter the course unit: '))
        if a_score <= score < 100:
            print(f"You scored an A in {course_code}")
            unit_scored = 5
            total_credit_points += unit_scored * course_unit
            total_number_of_units += course_unit
        elif b_score <= score < a_score:
            print(f'You scored a B in {course_code}')
            unit_scored = 4
            total_credit_points += unit_scored * course_unit
            total_number_of_units += course_unit
        elif c_score <= score < b_score:
            print(f'You scored a C in {course_code}')
            unit_scored = 3
            total_credit_points += unit_scored * course_unit
            total_number_of_units += course_unit
        elif d_score <= score < c_score:
            print(f'You scored a D in {course_code}')
            unit_scored = 2
            total_credit_points += unit_scored * course_unit
            total_number_of_units += course_unit
        elif e_score <= score < d_score:
            print(f'You scored an E in {course_code}')
            unit_scored = 1
            total_credit_points += unit_scored * course_unit
            total_number_of_units += course_unit
        elif f_score >= score < e_score:
            print(f'You scored an F in {course_code}')
            unit_scored = 0
            total_credit_points += unit_scored * course_unit
            total_number_of_units += course_unit
        else:
            print('Wrong Input!!!!, Enter a number that ranges from 1-100')
    return total_number_of_units, total_credit_points

tnu_1, tcp_1 = cgpa_calculator()
try:
    cgpa_1 = tcp_1 / tnu_1
    print(f'Your CGPA for this semester is {cgpa_1}')
except ZeroDivisionError:
    print('The program cannot run if your value is zero!!!, Please enter a value larger than 0')

all_units = 0
all_points = 0

comment = input('Do you wish to calculate your CGPA for the second semester?, '
                'NOTE: your response can be either "Yes" or "No": ').lower()

if comment == "yes":
    tnu_2, tcp_2 = cgpa_calculator()
    all_units = tnu_1 + tnu_2
    all_points = tcp_1 + tcp_2
    try:
        cgpa_2 = all_points / all_units
        print(f'Your CGPA for this semester is {cgpa_2}')
        print("Thanks for using this program, see you soon !")
    except ZeroDivisionError:
        print('The program cannot run if your value is zero!!!, Please enter a value larger than 0')
elif comment == 'no':
    print("Thanks for using this program, see you soon !")
else:
    print('Command can be either "yes" or "no" only!!!!')