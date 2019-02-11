import csv
from data_structures.student import Student
from data_structures.chair import Chair
import math
 
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
def findApprox(cList, sList):
    diff = 0
    for x in range(len(sList.prefs)):
        diff += abs(sList.prefs[x] - cList.prefs[x])
    return diff
def placeStudents(student_list, chair_list):
    pairs = []
    VIPs = []
    nonVIPs = []
    noPrefs = []
    for student in student_list:
        if student.is_VIP:
            VIPs.append(student)
        else:
            noPref = True
            for x in student.prefs:
                if x != 0:
                    noPref = False
            if noPref:
                noPrefs.append(student)
            else:
                nonVIPs.append(student)
    print(len(student_list),len(VIPs),len(nonVIPs),len(noPrefs))
    for s in VIPs:
        while not s.taken:
            print('looping')
            for c in chair_list:
                print(s.student_id, s.prefs,c.prefs)
                if not c.taken and not c.is_broken:
                    if s.prefs == c.prefs:
                        pairs.append([c,s])
                        c.taken = True
                        s.taken = True
                        break
            if not s.taken:
                min = 999
                minC = None
                for c in chair_list:
                    if not c.taken and not c.is_broken:
                        if findApprox(s,c) < min:
                            min = findApprox(c,s)
                            minC = c
                pairs.append([minC,s])
                minC.taken = True
                s.taken = True
            print('loop ends')
    for s in nonVIPs:
        while not s.taken:
            print('looping')
            for c in chair_list:
                print(s.student_id, s.prefs,c.prefs)
                if not c.taken and not c.is_broken:
                    if s.prefs == c.prefs:
                        pairs.append([c,s])
                        c.taken = True
                        s.taken = True
                        break
            if not s.taken:
                min = 999
                minC = None
                for c in chair_list:
                    if not c.taken and not c.is_broken:
                        if findApprox(s,c) < min:
                            min = findApprox(c,s)
                            minC = c
                pairs.append([minC,s])
                minC.taken = True
                s.taken = True
            print('loop ends')
    for s in noPrefs:
        print('looping')
        for c in chair_list:
            print(s.student_id, s.prefs,c.prefs)
            if not c.taken and not c.is_broken:
                # if s.prefs == c.prefs:
                pairs.append([c,s])
                c.taken = True
                s.taken = True
                break
        print('loop ends')
    return pairs
 
 
if __name__ == '__main__':
    student_file = '../test/BIOL101_001Students.csv'
    chair_file = '../test/BIOL101_001Room.csv'
    output_file = '../test/BIO101_001Output2.csv'
    student_count = sum(1 for line in open(student_file))-1
    chair_count = sum(1 for line in open(chair_file))-1

    chair_list = []
    student_list = []

    with open(student_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = True
        for row in csv_reader:
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
            # writer.writerow([x[0].chair_id,"",x[0].front,x[0].back,x[0].fronti,x[0].backi,x[0].aisle,x[0].left,x[1].student_id,x[1].is_VIP,x[1].pref_front,x[1].pref_back,x[1].pref_fronti,x[1].pref_backi,x[1].pref_aisle,x[1].pref_left])
            # writer.writerow([x[1].student_id,x[1].is_VIP,x[1].pref_front,x[1].pref_back,x[1].pref_fronti,x[1].pref_backi,x[1].pref_aisle,x[1].pref_left])
            writer.writerow([x[0].chair_id,"",x[0].prefs])
            writer.writerow([x[1].student_id,x[1].is_VIP,x[1].prefs])
            writer.writerow([""])
    for x in newPairs:
        # print(x[0].chair_id,x[1].student_id)
        print(x[0])
        print(x[1],"\n")
