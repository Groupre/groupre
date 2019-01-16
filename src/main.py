import csv
from data_structures.student import Student
from data_structures.chair import Chair
 
def placeStudents(student_list, chair_list):
    pairs = []
    for chair in chair_list:  
        for student in student_list:
            if not chair.is_broken and not chair.taken:
                if not student.taken and student.num_points > 99:
                    student.num_points -= 100
                    if chair.num_points == student.num_points:
                        pairs.append([chair.chair_id,student.student_id])
                        chair.taken = True
                        student.taken = True
     
    for chair in chair_list:
        for student in student_list:
            if not chair.is_broken and not chair.taken:
                if not student.taken:
                    if chair.num_points == student.num_points:
                        pairs.append([chair.chair_id,student.student_id])
                        chair.taken = True
                        student.taken = True
    for chair in chair_list:
        for student in student_list:
            if not chair.is_broken and not chair.taken:
                if not student.taken:
                    pairs.append([chair.chair_id,student.student_id])
                    chair.taken = True
                    student.taken = True
    return pairs
 
 
if __name__ == '__main__':
    student_file = '../test/randomizedTests/students/test_students_1.csv'
    chair_file = '../test/newTests/room.csv'
    student_count = sum(1 for line in open(student_file))-1
    chair_count = sum(1 for line in open(chair_file))-1
    student_list = []
    chair_list = []
 
    with open(student_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = True
        for row in csv_reader:
            print(row)
            if first_line: first_line = False
            else:
                if len(row) <= 4:
                    student_list.append(Student(row[0],row[2],[]))
                else:
                    student_list.append(Student(row[0], row[2], row[4:]))
 
    with open(chair_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = True
        for row in csv_reader:
            print(row)
            if first_line:
                first_line = False
            else:
                if len(row) <= 2:
                    chair_list.append(Chair(row[0],[]))
                else:
                    chair_list.append(Chair(row[0], row[2:]))

    for i in student_list:
        print(i.num_points)
    print("printing chair")
    for n in chair_list:
        print(n.num_points)
    newPairs = placeStudents(student_list, chair_list)
    print("print pairs")
    for x in newPairs:
        print(x)
