import csv
from data_structures.student import Student
from data_structures.chair import Chair
 
def indexSort(valList, rankList):
        # Traverse through 1 to len(arr) 
    for i in range(1, len(valList)): 
  
        key = valList[i] 
        keyRank = rankList[i]
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position  
        j = i-1
        while j >=0 and key < valList[j] : 
                valList[j+1] = valList[j] 
                rankList[j+1] = rankList[j]
                j -= 1
        valList[j+1] = key 
        rankList[j+1] = keyRank
def studentPref(student):
    studentPrefList = [0,0,0,0,0,0]
    if student.has_pref:
        if student.pref_front:
            studentPrefList[0] = 1
        elif student.pref_back:
            studentPrefList[1] = 1
        elif student.pref_fronti:
            studentPrefList[2] = 1
        elif student.pref_backi:
            studentPrefList[3] = 1
        elif student.pref_aisle:
            studentPrefList[4] = 1
        elif student.pref_left:
            studentPrefList[5] = 1

    return studentPrefList


def placeStudents(student_list, chair_list):
    pairs = []
    VIP_list = []
    pref_list = []
    other_list = []
    pointPool = [1,3,5,7,30,40]
    valPool = [0,0,0,0,0,0]
    rankPool = [0,1,2,3,4,5]
    
    for chair in chair_list:
        if chair.front:
            valPool[0] += 1
        elif chair.back:
            valPool[1] += 1
        elif chair.fronti:
            valPool[2] += 1
        elif chair.backi:
            valPool[3] += 1
        elif chair.aisle:
            valPool[4] += 1
        elif chair.left:
            valPool[5] += 1   
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
            for chair in chair_list:  
                if not chair.is_broken and not chair.taken:
                    if not student.taken:
                        if chair.num_points == student.num_points:
                            if chair.front:
                                valPool[0] -= 1
                            elif chair.back:
                                valPool[1] -= 1
                            elif chair.fronti:
                                valPool[2] -= 1
                            elif chair.backi:
                                valPool[3] -= 1
                            elif chair.aisle:
                                valPool[4] -= 1
                            elif chair.left:
                                valPool[5] -= 1
                            pairs.append([chair,student])
                            chair.taken = True
                            student.taken = True
            if (not student.taken):
                # if no match subtract one value
                tempVal = valPool.copy()
                tempRanked = rankPool.copy()
                indexSort(tempVal,tempRanked)
                print(valPool, tempRanked)
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
                        # see what preferences student have
                        studentList = studentPref(student)
                        prefList = []
                        for i in range(len(studentList)):
                            if studentList[i] == 1:
                                prefList.append(i)
                        # find the less common val
                        minY = 999
                        for x in prefList:
                            for y in range(len(tempRanked)):
                                if x == tempRanked[y]:
                                    if y < minY:
                                        minY = y                                 
                        print(student.num_points, pointPool[tempRanked[minY]]) 
                        student.num_points -= pointPool[tempRanked[minY]]
                    else:
                        student.num_points = 0
    for student in pref_list:
        while (not student.taken):
            for chair in chair_list:
                if not chair.is_broken and not chair.taken:
                    if not student.taken:
                        if chair.num_points == student.num_points:
                            if chair.front:
                                valPool[0] -= 1
                            elif chair.back:
                                valPool[1] -= 1
                            elif chair.fronti:
                                valPool[2] -= 1
                            elif chair.backi:
                                valPool[3] -= 1
                            elif chair.left:
                                valPool[4] -= 1
                            elif chair.aisle:
                                valPool[5] -= 1
                            pairs.append([chair,student])
                            chair.taken = True
                            student.taken = True
                        # if no match subtract one value
            if (not student.taken):
                # if no match subtract one value
                tempVal = valPool.copy()
                tempRanked = rankPool.copy()
                indexSort(tempVal,tempRanked)
                print(valPool, tempRanked)
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
                        # see what preferences student have
                        studentList = studentPref(student)
                        prefList = []
                        for i in range(len(studentList)):
                            if studentList[i] == 1:
                                prefList.append(i)
                        # find the less common val
                        minY = 999
                        for x in prefList:
                            for y in range(len(tempRanked)):
                                if x == tempRanked[y]:
                                    if y < minY:
                                        minY = y                                 
                        print(student.num_points, pointPool[tempRanked[minY]]) 
                        student.num_points -= pointPool[tempRanked[minY]]
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
    student_file = '../test/BIOL201_007Student.csv'
    chair_file = '../test/BIOL201_007Room.csv'
    output_file = '../test/BIO201_007newOutput.csv'
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
    with open(output_file,"w",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["ids","isVIP","front","back","frontish","backish","aisle","left"])
        for x in newPairs:
            writer.writerow([x[0].chair_id,"",x[0].front,x[0].back,x[0].fronti,x[0].backi,x[0].aisle,x[0].left,x[1].student_id,x[1].is_VIP,x[1].pref_front,x[1].pref_back,x[1].pref_fronti,x[1].pref_backi,x[1].pref_aisle,x[1].pref_left])
            writer.writerow([x[1].student_id,x[1].is_VIP,x[1].pref_front,x[1].pref_back,x[1].pref_fronti,x[1].pref_backi,x[1].pref_aisle,x[1].pref_left])
            writer.writerow([""])
    for x in newPairs:
        # print(x[0].chair_id,x[1].student_id)
        print(x[0])
        print(x[1],"\n")
