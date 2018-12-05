# !/usr/bin/env python
'''This module will be used to take input from a chairs.csv and a students.csv
 and return a csv of sorted teams.'''

import argparse
import csv
import sys
import time
from typing import List

# import groupre_globals
# from data_structures import Chair, Student, TeamStructure
# from helpers import build_team_structures, create_teams

import csv
from data_structures_new.student import Student
from data_structures_new.chair import Chair

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

def main(argv):
    '''Takes the input arguments and executes the groupre matching algorithm.'''

    argparser = argparse.ArgumentParser()

    chairs_csv: str = None
    students_csv: str = None
    fallback: bool = None
    metrics: bool = None
    output_csv: str = None
    gender: bool = None

    # groupre.py -c CHAIRS -s STUDENTS -f FALLBACK -o OUTPUT
    argparser.add_argument(
        '-c', '--chairs', help='Chairs input file')
    argparser.add_argument(
        '-s', '--students', help='Students input file')
    argparser.add_argument(
        '-f', '--fallback', help='Enable fallback functionality', action='store_true')
    argparser.add_argument(
        '-m', '--metrics', help='Enable metrics functionality', action='store_true')
    argparser.add_argument(
        '-o', '--output', help='Output file')
    argparser.add_argument(
        '-g', '--gender', help='Enable gender functionality', action='store_true')
    argparser.set_defaults(fallback=False, output_csv='output.csv')

    if 'groupre.py' in argv[0]:
        parsed_args = argparser.parse_args()
    else:
        parsed_args = argparser.parse_args(argv)

    chairs_csv: str = parsed_args.chairs
    students_csv: str = parsed_args.students
    fallback: bool = parsed_args.fallback
    metrics: bool = parsed_args.metrics
    output_csv: str = parsed_args.output
    gender: bool = parsed_args.gender

    print('Arguments: Chairs {}, Students {}, Fallback {}, Gender {}, Output {}'.format(
        parsed_args.chairs, parsed_args.students, parsed_args.fallback,
        parsed_args.gender, parsed_args.output))

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


    student_file = students_csv
    chair_file = chairs_csv
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
    # groupre_globals.METRICS_ENABLED = metrics

    # if groupre_globals.METRICS_ENABLED:
    #     timing = time.time()

    # groupre_globals.FALLBACK_ENABLED = fallback
    # groupre_globals.GENDER_ENABLED = gender

    # priority_fields = []

    # chairs = []
    # with open(chairs_csv, 'r') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     fields = next(reader)
    #     print(fields)
    #     # Error checking on chair input for minimum required fields.
    #     for required_field in groupre_globals.CHAIR_REQUIRED_FIELDS:
    #         if required_field not in fields:
    #             raise ValueError(
    #                 'chairs csv file is lacking a', required_field, 'field!')

    #     # Pull our priority_fields by process of elimination.
    #     for field in fields:
    #         print(field)
    #         if field not in groupre_globals.CHAIR_REQUIRED_FIELDS:
    #             priority_fields.append(field)

    #     for row in reader:
    #         chairs.append(Chair(    
    #             row[:len(groupre_globals.CHAIR_REQUIRED_FIELDS)],
    #             row[len(groupre_globals.CHAIR_REQUIRED_FIELDS):]))

    # if groupre_globals.FALLBACK_ENABLED:
    #     # Process chairs to find all fallback options.
    #     for chair in chairs:
    #         for attribute in chair.attributes:
    #             if 'front' in attribute:
    #                 if attribute not in groupre_globals.FALLBACK_CHAIRS_FRONT:
    #                     print(attribute)
    #                     groupre_globals.FALLBACK_CHAIRS_FRONT.append(attribute)
    #             elif 'back' in attribute:
    #                 if attribute not in groupre_globals.FALLBACK_CHAIRS_BACK:
    #                     groupre_globals.FALLBACK_CHAIRS_BACK.append(attribute)
    #             elif 'aisle' in attribute:
    #                 if attribute not in groupre_globals.FALLBACK_CHAIRS_AISLE:
    #                     groupre_globals.FALLBACK_CHAIRS_AISLE.append(attribute)
    #     for x in groupre_globals.FALLBACK_CHAIRS_FRONT:
    #         print("groupre_globals: " + x)
    #     # Sort our fallback options.
    #     groupre_globals.FALLBACK_CHAIRS_FRONT.sort(
    #         key=lambda x: (int)(('' + x).split('-', 1)[1]), reverse=False)
    #     groupre_globals.FALLBACK_CHAIRS_BACK.sort(
    #         key=lambda x: (int)(('' + x).split('-', 1)[1]), reverse=False)
    #     groupre_globals.FALLBACK_CHAIRS_AISLE.sort(
    #         key=lambda x: (int)(('' + x).split('-', 1)[1]), reverse=False)

    #     # groupre_globals.set_all_fallback_limits_to_max()

    # students = []
    # with open(students_csv, 'r') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     fields = next(reader)

    #     # Error checking on student input for minimum required fields.
    #     for required_field in groupre_globals.STUDENT_REQUIRED_FIELDS:
    #         if required_field not in fields:
    #             raise ValueError(
    #                 'students csv file is lacking a', required_field, 'field!')

    #     for row in reader:
    #         students.append(Student(
    #             row[:len(groupre_globals.STUDENT_REQUIRED_FIELDS)],
    #             row[len(groupre_globals.STUDENT_REQUIRED_FIELDS):]))

    # # Benchmarking statement.
    # total_students = len(students)
    # total_chairs = len(chairs)
    # print('Processing', total_students,
    #       'students to be seated in', total_chairs, 'chairs...')

    # if groupre_globals.METRICS_ENABLED:
    #     groupre_globals.METRICS = []
    #     groupre_globals.METRICS.append('Students: ' + str(total_students))
    #     groupre_globals.METRICS.append('Seats: ' + str(total_chairs))

    # # Run our algorithm to match students to chairs within teams, keeping in mind their
    # # scores and preferences.
    # team_structures: List[TeamStructure] = build_team_structures(chairs)

    # teams = create_teams(students, chairs, team_structures)

    # # Write our output to a csv.
    # # NOTE 'newline=''' required when writing on an OS that ends lines in CRLF rather than just LF.
    # print('----------')
    # print('Seats assigned. Writing to csv.')
    # with open(output_csv, 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=',',
    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     for team in teams:
    #         # print("this " + team)
    #         writer.writerow(team)

    # priority_rating = ''
    # print("lalalalalalal")
    # print('----------')
    # if groupre_globals.STUDENT_PRIORITY_TOTAL != 0:
    #     priority_rating = ('Student Priority Rating: ' + str(
    #         round(groupre_globals.STUDENT_PRIORITY_VALUE /
    #               groupre_globals.STUDENT_PRIORITY_TOTAL * 100, 2)) + '%')
    #     print(priority_rating)
    # print('----------')

    # if groupre_globals.METRICS_ENABLED:
    #     print('lalala')
    #     print('lalalaxsada')
    #     groupre_globals.METRICS.append(priority_rating)
    #     metrics_file = output_csv.split('.', 1)[0] + '-metrics.txt'
    #     print(metrics_file)
    #     groupre_globals.METRICS.append(
    #         'Time Elapsed: ' + str(time.time() - timing) + ' seconds')
    #     with open(metrics_file, 'w') as file:
    #         for metric in groupre_globals.METRICS:
    #             file.write(metric + '\n')
if __name__ == '__main__':
    # Benchmark timer start.
    time.clock()
    print('----------')

    # When importing groupre, you can provide arguments by calling it as such:
    #   groupre.main('groupre.py', ARGS)

    main(sys.argv)

    # Benchmark timer end.
    print(time.clock(), 'seconds elapsed.')
    print('----------')
