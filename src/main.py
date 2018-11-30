import csv
from data_structures.student import Student
from data_structures.chair import Chair


def sortStudentFunc(student_list):
    student_pool = [[], [], [], [], [], [], []]

    for student in student_list:
        if student.has_pref:
            pref_count = -1
            if not student.is_VIP:
                pref_count += 3
            if student.pref_front:
                pref_count += 1
            if student.pref_back:
                pref_count += 1
            if student.pref_aisle:
                pref_count += 1
            if student.pref_left:
                pref_count += 1
            student_pool[pref_count].append(student)
        else:
            student_pool[6].append(student)

    return student_pool[0] + student_pool[1] + student_pool[2] + student_pool[3] + student_pool[4] + student_pool[5] + student_pool[6]


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key.chair_id < arr[j].chair_id:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


def sort_group(group_list):
    #Sort the groups on number of preferences (most to least)
    return group_list


def placeStudents(student_list, chair_list):
    for chair in chair_list:
        if chair.is_broken:
            continue
        top = 0
        top_student = student_list[0]
        for student in student_list:
            this = 0
            if chair.front and student.pref_front:
                this += 10
            elif chair.back and student.pref_back:
                this += 10
            if chair.aisle and student.pref_aisle:
                this += 10
            if chair.left and student.pref_left:
                this += 1
            if this > top:
                top = this
                top_student = student
        chair.student_id = top_student.student_id
        del student_list[student_list.index(top_student)]
    return student_list


if __name__ == '__main__':
    student_file = '../test/randomizedTests/students/test_students_1.csv'
    chair_file = '../test/newTests/room.csv'
    student_count = sum(1 for line in open(student_file))-1
    chair_count = sum(1 for line in open(chair_file))-1
    student_list = []
    chair_list = []

    with open(student_file, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            student_list.append(Student(*row))
    with open(chair_file, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            chair_list.append(Chair(*row))

    sorted_student_list = sortStudentFunc(student_list)
    insertionSort(chair_list)

    for chair in chair_list:
        print(chair)
    for student in sorted_student_list:
            print(student)

    placeStudents(sorted_student_list, chair_list)

    for chair in chair_list:
        print(chair)
