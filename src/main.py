import csv
from data_structures.student import Student
from data_structures.chair import Chair
 
def placeStudents(student_list, chair_list):
    pairs = []
    VIP_list = []
    pref_list = []
    other_list = []
    valPool = [30,40]
    maxVal = 0
    for student in student_list:
        if student.num_points == 0:
            other_list.append(student)
        elif student.num_points > 998:
            student.num_points -= 999
            VIP_list.append(student)
        else:
            pref_list.append(student)
    for student in VIP_list:
        while (not student.taken):
            print("student points")
            print(student.num_points)
            for chair in chair_list:  
                if not chair.is_broken and not chair.taken:
                    if not student.taken:
                        if chair.num_points == student.num_points:
                            pairs.append([chair,student])
                            chair.taken = True
                            student.taken = True
            if (not student.taken):
                # if no match subtract one value
                for val in range(len(valPool)):
                    if student.num_points >= valPool[val]:
                        maxVal = val
                if (student.num_points == 0):
                    # if student has no pref then add to other list and skip to next student
                    other_list.append(student)
                    student.taken = True
                else:
                    # if no frontish or backish seats
                    if (student.num_points == 5):
                        student.num_points = 0
                    elif (student.num_points == 7):
                        student.num_points = 0
                # if students has only one attribute
                    elif (student.num_points < 20) and ((student.num_points % 10) == 1):
                        student.num_points = 5
                    elif (student.num_points < 20) and ((student.num_points % 10) == 3):
                        student.num_points = 7
                    elif (student.num_points % 10) == 0:
                        student.num_points -= valPool[maxVal]
                    else:
                        student.num_points = 0
    for student in pref_list:
        while (not student.taken):
            for chair in chair_list:
                if not chair.is_broken and not chair.taken:
                    if not student.taken:
                        if chair.num_points == student.num_points:
                            pairs.append([chair,student])
                            chair.taken = True
                            student.taken = True
                        # if no match subtract one value
            if (not student.taken):
                # if no match subtract one value
                for val in range(len(valPool)):
                    if student.num_points > valPool[val]:
                        maxVal = val
                if (student.num_points == 0):
                    # if student has no pref then add to other list and skip to next student
                    other_list.append(student)
                    student.taken = True
                else:
                    # if no frontish or backish seats
                    if (student.num_points == 5):
                        student.num_points = 0
                    elif (student.num_points == 7):
                        student.num_points = 0
                # if students has only one attribute
                    elif (student.num_points < 20) and ((student.num_points % 10) == 1):
                        student.num_points = 5
                    elif (student.num_points < 20) and ((student.num_points % 10) == 3):
                        student.num_points = 7
                    elif (student.num_points % 10) == 0:
                        student.num_points -= valPool[maxVal]
                    else:
                        student.num_points = 0
    for student in other_list:
        for chair in chair_list:
            if not chair.is_broken and not chair.taken:
                if not student.taken:
                    pairs.append([chair,student])
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

    newPairs = placeStudents(student_list, chair_list)
    print("print pairs")
    for x in newPairs:
        # print(x[0].chair_id,x[1].student_id)
        print(x[0])
        print(x[1],"\n")
