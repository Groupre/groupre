import csv
from data_structures.student import Student
from data_structures.chair import Chair

def sortStudentFunc(student_list):
    vipList3 = []
    vipList2 = []
    vipList1 = []
    prefList3 = []
    prefList2 = []
    prefList1 = []
    genList = []

    for student in student_list:
        if student.isVIP:
            num_of_prefs = 0
            if (student.prefersFront or student.prefersBack):
                num_of_prefs = num_of_prefs+1
            if student.prefersAisle:
                num_of_prefs = num_of_prefs+1
            if student.prefersLeft:
                num_of_prefs = num_of_prefs+1
            if (num_of_prefs == 0):
                vipList1.append(student)
            if (num_of_prefs == 1):
                vipList2.append(student)
            if (num_of_prefs == 2):
                vipList3.append(student)
        elif student.prefersFront or student.prefersBack or student.prefersAisle or student.prefersLeft:
            num_of_prefs = 0
            if (student.prefersFront or student.prefersBack):
                num_of_prefs = num_of_prefs+1
            if student.prefersAisle:
                num_of_prefs = num_of_prefs+1
            if student.prefersLeft:
                num_of_prefs = num_of_prefs+1
            if (num_of_prefs == 0):
                prefList1.append(student)
            if (num_of_prefs == 1):
                prefList2.append(student)
            if (num_of_prefs == 2):
                prefList3.append(student)
        else:
            genList.append(student)
    return vipList3, vipList2, vipList1, prefList3, prefList2, prefList1, genList

def sort_group(group_list):
    #Sort the groups on number of preferences (most to least) and
    return group_list

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key.chair_id < arr[j].chair_id:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def placeStudents(student_list, chair_list):
    for student in student_list:
        if student.isVIP:
            if student.prefersFront:
                chair_list[5].student = student
            elif student.prefersBack:
                chair_list[95].student = student
            if student.prefersAisle:
                chair_list[59]
            if student.prefersLeft:
                chair_list[50]
    return student_list

if __name__ == '__main__':
    student_file = '../test/randomizedTests/students/test_students_1.csv'
    chair_file = '../test/newTests/room-g101--10-10.csv'
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
        if chair.is_broken:
            chair.student_id = None
        else:
            for student in sorted_student_list[0]:
                if True:
                    chair.student_id = student.student_id
                    sorted_student_list[0].remove(student)
                else:
                    sorted_student_list[1].append
            for student in sorted_student_list[1]:
                if (student.prefersFront and chair.front) or (student.prefersBack and chair.back) and (student.prefersAisle and chair.aisle):
                    chair.student_id = student.student_id
                    sorted_student_list[1].remove(student)
                elif (student.prefersFront and chair.front) or (student.prefersBack and chair.back) and (student.prefersLeft and chair.left):
                    chair.student_id = student.student_id
                    sorted_student_list[1].remove(student)
                elif (student.prefersLeft and chair.left) and (student.prefersAisle and chair.aisle):
                    chair.student_id = student.student_id
                    sorted_student_list[1].remove(student)
            for student in sorted_student_list[2]:
                    chair.student_id = student.student_id
                    sorted_student_list[2].remove(student)
            for student in sorted_student_list[3]:
                    chair.student_id = student.student_id
                    sorted_student_list[3].remove(student)
            for student in sorted_student_list[4]:
                    chair.student_id = student.student_id
                    sorted_student_list[4].remove(student)
            for student in sorted_student_list[5]:
                    chair.student_id = student.student_id
                    sorted_student_list[5].remove(student)
            for student in sorted_student_list[6]:
                    chair.student_id = student.student_id
                    sorted_student_list[6].remove(student)

    for chair in chair_list:
        print(chair)
