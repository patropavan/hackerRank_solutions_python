'''
Problem Statement url
https://www.hackerrank.com/challenges/grading/problem
'''

''' solution  '''


def gradingStudents(grades):
    final_grades_list = []
    for grade in grades:
        round_off_grades_tuple = ((grade // 10) * 10 + 5, (grade // 10) * 10 + 10)
        round_off_grade = 0

        if grade < 38:
            final_grades_list.append(grade)

        elif grade >= 38 and grade < 40:
            round_off_grade = round_off_grade + round_off_grades_tuple[1]
            grade = round_off_grade
            final_grades_list.append(grade)

        else:
            if grade < round_off_grades_tuple[0]:
                round_off_grade = round_off_grade + round_off_grades_tuple[0]
            else:
                round_off_grade = round_off_grade + round_off_grades_tuple[1]

            if round_off_grade - grade < 3:
                grade = round_off_grade
                final_grades_list.append(grade)
            if round_off_grade - grade >= 3:
                final_grades_list.append(grade)

    for f_grade in final_grades_list:
        print(f_grade)


gradingStudents([73, 67, 38, 33])
