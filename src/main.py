import csv
from data_structures.student import Student
from data_structures.chair import Chair

if __name__ == '__main__':
    student_list = []
    with open('../test/randomizedTests/students/test_students_1.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            student_list.append(Student(*row))

    for student in student_list:
        print(student)

    chair_list = []
    with open('../test/randomizedTests/chair/test_chairs_1.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            chair_list.append(Chair(*row))

    for chair in chair_list:
        print(chair)

