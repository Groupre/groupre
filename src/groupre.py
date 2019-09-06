#!/usr/bin/env python
'''This module will be used to take input from a chairs.csv and a students.csv
 and return a csv of sorted teams.'''

import argparse
import csv
import sys
import time
from typing import List

from data_structures.student import Student
from data_structures.chair import Chair
import math

#find the seat difference
def findApprox(cList, sList):
    diff = 0
    for x in range(len(sList.prefs)):
        diff += abs(sList.prefs[x] - cList.prefs[x])
    return diff
#place students into matching/prefered seats
def sortByPrefs(arr):
    # modified insertion sort code from geeks to geeks
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 

        keyInd = arr[i]
        key = arr[i].numPref
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key > arr[j].numPref : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = keyInd

def placeStudents(student_list, chair_list):
    pairs = []
    VIPs = []
    nonVIPs = []
    noPrefs = []
    #split students up into 3 categories
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
    #sort each categories
    sortByPrefs(VIPs)
    sortByPrefs(nonVIPs)
    sortByPrefs(chair_list)

    # find perfect match in VIP list as first priority
    for s in VIPs:
        for c in chair_list:
            if not c.taken and not c.is_broken:
                if s.prefs == c.prefs:
                    pairs.append([c,s])
                    c.taken = True
                    s.taken = True
                    break
    # find close approx. seat for VIP
    for s in VIPs:
        while not s.taken:
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
    # find perfect match in preference list
    for s in nonVIPs:
        for c in chair_list:
            if not c.taken and not c.is_broken:
                if s.prefs == c.prefs:
                    pairs.append([c,s])
                    c.taken = True
                    s.taken = True
                    break
    # find approximate match
    for s in nonVIPs:
        while not s.taken:
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
    # fill the rest of unmatched seats
    for s in noPrefs:
        for c in chair_list:
            if not c.taken and not c.is_broken:
                pairs.append([c,s])
                c.taken = True
                s.taken = True
                break
    return pairs
 

def main(argv):
    '''Takes the input arguments and executes the groupre matching algorithm.'''

    argparser = argparse.ArgumentParser()

    chairs_csv: str = None
    students_csv: str = None
    output_csv: str = None

    # groupre.py -c CHAIRS -s STUDENTS -f FALLBACK -o OUTPUT
    argparser.add_argument(
        '-c', '--chairs', help='Chairs input file')
    argparser.add_argument(
        '-s', '--students', help='Students input file')
    argparser.add_argument(
        '-o', '--output', help='Output file')
    argparser.set_defaults(fallback=False, output_csv='output.csv')

    if 'groupre.py' in argv[0]:
        parsed_args = argparser.parse_args()
    else:
        parsed_args = argparser.parse_args(argv)

    chairs_csv: str = parsed_args.chairs
    students_csv: str = parsed_args.students
    output_csv: str = parsed_args.output

    #file error checking
    if chairs_csv is None:
        print('Missing chairs input file.')
        return
    if '.csv' not in chairs_csv:
        print('Chairs input is of wrong format. Try uploading a .csv instead.')
        return

    if students_csv is None:
        print('Missing students input file.')
        return
    if '.csv' not in students_csv:
        print('Students input is of wrong format. Try uploading a .csv instead.')
        return

    if output_csv is None:
        print('''Output file not specified, and the default was somehow
                replaced. Please try specifying a proper output file.''')
        return
    student_count = sum(1 for line in open(students_csv))-1
    chair_count = sum(1 for line in open(chairs_csv))-1
    chair_list = []
    student_list = []
    
    #read chair file
    with open(chairs_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = True
        for row in csv_reader:
            if first_line:
                first_line = False
            else:
                chair_list.append(Chair(row[0],row[1],row[2:]))
    #read student file
    with open(students_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = True
        for row in csv_reader:
            if first_line: first_line = False   
            else:
                student_list.append(Student(row[0], row[1],row[2], row[4:]))

    # placing students
    newPairs = placeStudents(student_list, chair_list)

    # Write our output to a csv.
    # NOTE 'newline=''' required when writing on an OS that ends lines in CRLF rather than just LF.
    print('----------')
    print('Seats assigned. Writing to csv.')
    # writing outputs
    with open(output_csv,"w",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for x in newPairs:
            writer.writerow([x[0].chair_id,x[0].group_id,x[1].student_id,x[1].onyen])

if __name__ == '__main__':
    # Benchmark timer start.
    time.process_time
    print('----------')
    
    main(sys.argv)

    # Benchmark timer end.
    print(time.process_time, 'seconds elapsed.')
    print('----------')
