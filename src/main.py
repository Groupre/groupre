import csv
from data_structures.student import Student
from data_structures.chair import Chair

def sortStudentFunc(student_list):
    vipList = []
    prefList = []
    genList = []

    for student in student_list:
        if student.isVIP:
            print(student.isVIP)
            vipList.append(student)
        elif student.prefersFront or student.prefersBack or student.prefersLeft or student.prefersAisle:
            prefList.append(student)
        else:
            genList.append(student)
    finalList = vipList + prefList + genList

    return finalList

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key.chair_id < arr[j].chair_id:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def placeStudents(sorted_student_list, ):
    return

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
    with open('../test/randomizedTests/chairs/test_chairs_1.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            chair_list.append(Chair(*row))

    for chair in chair_list:
        print(chair)

    sorted_student_list = sortStudentFunc(student_list)
    for student in sorted_student_list:
        print(student)

    insertionSort(chair_list)
    for chair in chair_list:
        print(chair)
