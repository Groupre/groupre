#!/usr/bin/env python
'''This module will be used to take input from a chairs.csv and a students.csv
 and return a csv of sorted teams.'''

import argparse
import csv
import time

import groupre_build_team_structures
import groupre_chair
import groupre_create_teams
import groupre_globals
import groupre_student


def main():
    '''Takes the input arguments and executes the groupre matching algorithm.'''

    argparser = argparse.ArgumentParser()

    chairs_csv = None
    students_csv = None
    fallback = None
    output_csv = None

    # groupre.py -c CHAIRS -s STUDENTS -f FALLBACK -o OUTPUT
    argparser.add_argument(
        "-c", "--chairs", help="Chairs input file", dest=chairs_csv)
    argparser.add_argument(
        "-s", "--students", help="Students input file", dest=students_csv)
    argparser.add_argument(
        "-f", "--fallback", help="Enable fallback functionality",
        dest=fallback, action='store_true')
    argparser.add_argument(
        "-o", "--output", help="Output file", dest=output_csv)
    argparser.set_defaults(fallback=False, output_csv="output.csv")

    parsed_args = argparser.parse_args()

    chairs_csv = parsed_args.chairs
    students_csv = parsed_args.students
    fallback = parsed_args.fallback
    output_csv = parsed_args.output

    print("Arguments: Chairs {}, Students {}, Fallback {}, Output {}".format(
        parsed_args.chairs, parsed_args.students, parsed_args.fallback, parsed_args.output))

    if chairs_csv is None:
        print("Missing chairs input file.")
        return
    if ".csv" not in chairs_csv:
        print("Chairs input is of wrong format. Try uploading a .csv instead.")
        return

    if students_csv is None:
        print("Missing students input file.")
        return
    if ".csv" not in students_csv:
        print("Students input is of wrong format. Try uploading a .csv instead.")
        return

    if output_csv is None:
        print('''Output file not specified, and the default was somehow
            replaced. Please try specifying a proper output file.''')
        return

    priority_fields = []

    chairs = []
    with open(chairs_csv, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = next(reader)

        # Error checking on chair input for minimum required fields.
        for required_field in groupre_globals.CHAIR_REQUIRED_FIELDS:
            if required_field not in fields:
                raise ValueError(
                    'chairs csv file is lacking a', required_field, 'field!')

        # Pull our priority_fields by process of elimination.
        for field in fields:
            if field not in groupre_globals.CHAIR_REQUIRED_FIELDS:
                priority_fields.append(field)

        for row in reader:
            chairs.append(groupre_chair.Chair(
                row[:len(groupre_globals.CHAIR_REQUIRED_FIELDS)],
                row[len(groupre_globals.CHAIR_REQUIRED_FIELDS):]))

        # for chair in chairs:
        #     print('Chair:', chair.chair_id, chair.team_id, chair.attributes)

    students = []
    with open(students_csv, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = next(reader)

        # Error checking on student input for minimum required fields.
        for required_field in groupre_globals.STUDENT_REQUIRED_FIELDS:
            if required_field not in fields:
                raise ValueError(
                    'students csv file is lacking a', required_field, 'field!')

        # Since students is filled out after chairs, use the already obtained priority_fields
        # to verify that our csvs match.
        for field in fields:
            if field not in groupre_globals.STUDENT_REQUIRED_FIELDS:
                if field not in priority_fields:
                    raise ValueError(
                        'priority_fields between students csv and chairs csv do not match!')

        for row in reader:
            students.append(groupre_student.Student(
                row[:len(groupre_globals.STUDENT_REQUIRED_FIELDS)],
                row[len(groupre_globals.STUDENT_REQUIRED_FIELDS):]))

        # for student in students:
        #     print('Student:', student.student_id, student.preferences)

    # Benchmarking statement.
    total_students = len(students)
    total_chairs = len(chairs)
    print('Processing', total_students,
          'students to be seated in', total_chairs, 'chairs...')

    # Run our algorithm to match students to chairs within teams, keeping in mind their
    # scores and preferences.
    team_structures = groupre_build_team_structures.build_team_structures(
        chairs)
    teams = groupre_create_teams.create_teams(
        students, chairs, team_structures, priority_fields)

    # Write our output to a csv.
    # NOTE "newline=''" required when writing on an OS that ends lines in CRLF rather than just LF.
    print('----------')
    print('Seats assigned. Writing to csv.')
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for team in teams:
            writer.writerow(team)

    print('----------')
    print('Student Priority Rating:',
          round(groupre_globals.STUDENT_PRIORITY_VALUE /
                groupre_globals.STUDENT_PRIORITY_TOTAL * 100, 2), '%')
    print('----------')


# Benchmark timer start.
time.clock()
print('----------')

main()

# Benchmark timer end.
print(time.clock(), 'seconds elapsed.')
print('----------')
