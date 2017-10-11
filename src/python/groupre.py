#!/usr/bin/env python
'''This module will be used to take input from a chairs.csv and a students.csv
 and return a csv of sorted teams.'''

import csv
import sys
import time

import groupre_globals
import groupre_genericentry
import groupre_student
import groupre_create_teams
import groupre_build_team_structures


def main(args):
    '''Executes the goal of the module.'''

    # Initialization of csv files.
    chairs_csv = None
    students_csv = None

    # Handling of arguments for csv file selection.
    if len(args) == 1:
        print('''Not enough input arguments provided.
        Please provide groupre.py with a chairs csv and students csv (in that order).''')
        return

    # Actual use case: chairs argument must come before students argument.
    print('Argument List:', args[1] + ",", args[2])
    chairs_csv = args[1]
    students_csv = args[2]

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
            chairs.append(groupre_genericentry.GenericEntry(fields, row))

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
            students.append(groupre_student.Student(fields, row))

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
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for team in teams:
            writer.writerow(team)

    print('----------')
    print('Student Priority Rating:',
          round(groupre_globals.STUDENT_PRIORITY_VALUE /
                groupre_globals.STUDENT_PRIORITY_TOTAL * 100, 2), '%')
    # print('Student Full Priority Rating:',
    #       groupre_globals.STUDENT_FULL_PRIORITY / total_students * 100, '%')
    print('----------')


# Benchmark timer start.
time.clock()
print('----------')

main(sys.argv)

# Benchmark timer end.
print(time.clock(), 'seconds elapsed.')
print('----------')
