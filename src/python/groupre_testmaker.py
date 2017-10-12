'''This module is used to produce test input files to be used by groupre.'''

import random
import uuid
import csv
import math
import argparse
import string


def make_test_pair(test_identifier, student_count, chair_count,
                   student_minimum_specificness, student_maximum_specificness,
                   possible_chair_attributes, possible_student_preferences, team_count):
    '''Creates chairs and students csvs with given parameters.'''

    make_students(test_identifier, student_count, student_minimum_specificness,
                  student_maximum_specificness, possible_student_preferences)

    make_chairs(test_identifier, chair_count,
                possible_chair_attributes, team_count)


def make_students(test_identifier, student_count, student_minimum_specificness,
                  student_maximum_specificness, possible_student_preferences):
    '''Makes a student csv file with the given parameters.'''

    sids = []
    for i in range(student_count):
        while True:
            new_sid = random.randint(1, 999999)
            if new_sid not in sids:
                sids.append(new_sid)
                break

    students = []
    for i in range(student_count):
        student = []

        student_id = random.choice(sids)
        sids.remove(student_id)

        # student_name = str(uuid.uuid4())
        student_name = i
        student_score = random.randint(1, 4)

        student.append(student_id)
        student.append(student_name)
        student.append(student_score)

        student_attribute_count = random.randint(
            student_minimum_specificness, student_maximum_specificness)

        for j in range(student_attribute_count):
            possible_pref = random.choice(possible_student_preferences)
            if possible_pref not in student:
                student.append(possible_pref)

        students.append(student)

    with open('../../test/randomizedTests/students/test_students_'
              + test_identifier + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["PID", "StudentName", "Score", "Preferences"])
        for student in students:
            writer.writerow(student)


def make_chairs(test_identifier, chair_count, possible_chair_attributes,
                team_count):
    '''Makes a chairs csv file with the given parameters.'''

    cids = []
    for i in range(chair_count):
        while True:
            new_pid = random.randint(1, chair_count)
            if new_pid not in cids:
                cids.append(new_pid)
                break

    teams = []
    for i in range(team_count):
        for j in range(math.ceil(chair_count / team_count)):
            teams.append(i)

    chairs = []
    for i in range(chair_count):
        chair = []

        chair_id = random.choice(cids)
        cids.remove(chair_id)

        team_id = random.choice(teams)
        teams.remove(team_id)

        chair.append(chair_id)
        chair.append(team_id)

        chair_attribute_count = random.randint(
            0, len(possible_chair_attributes))

        for j in range(chair_attribute_count):
            possible_attr = random.choice(possible_chair_attributes)
            if possible_attr not in chair:
                chair.append(possible_attr)

        chairs.append(chair)

    with open('../../test/randomizedTests/chairs/test_chairs_'
              + test_identifier + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["CID", "TeamID", "Attributes"])
        for chair in chairs:
            writer.writerow(chair)


def main():
    '''Used to create test files from test shell scripts.'''

    argparser = argparse.ArgumentParser()

    test_identifier = None
    student_count = None
    chair_count = None
    student_minimum_specificness = None
    student_maximum_specificness = None
    possible_chair_attributes = None
    possible_student_preferences = None
    team_count = None

    # groupre_testmaker.py -id TESTID -sc STUDENTCOUNT -cc CHAIRCOUNT -mins
    # MINSPECIFICNESS -maxs MAXSPECIFICNESS -ca CHAIRATTRIBUTES -sp
    # STUDENTPREFERENCES -tc TEAMCOUNT
    argparser.add_argument('-id', '--testid', help='Test identifier')
    argparser.add_argument('-sc', '--studentcount',
                           help='Student count', type=int)
    argparser.add_argument('-cc', '--chaircount', help='Chair count', type=int)
    argparser.add_argument('-mins', '--minspecificness',
                           help='Minimum student specificness', type=int)
    argparser.add_argument('-maxs', '--maxspecificness',
                           help='Maximum student specificness', type=int)
    argparser.add_argument('-ca', '--chairattrs',
                           help='Possible chair attributes', type=list)
    argparser.add_argument('-sp', '--studentprefs',
                           help='Possible student preferences', type=list)
    argparser.add_argument('-tc', '--teamcount', help='Team count', type=int)

    parsed_args = argparser.parse_args()

    test_identifier = parsed_args.testid
    student_count = parsed_args.studentcount
    chair_count = parsed_args.chaircount
    student_minimum_specificness = parsed_args.minspecificness
    student_maximum_specificness = parsed_args.maxspecificness
    possible_chair_attributes = parsed_args.chairattrs
    possible_student_preferences = parsed_args.studentprefs
    team_count = parsed_args.teamcount

    print('''Arguments: test_identifier {}, student_count {}, chair_count {},
        student_minimum_specificness {}, student_maximum_specificness {}, 
        possible_chair_attributes {}, possible_student_preferences {}, team_count {}'''
          .format(parsed_args.testid, parsed_args.studentcount,
                  parsed_args.chaircount, parsed_args.minspecificness,
                  parsed_args.maxspecificness, parsed_args.chairattrs,
                  parsed_args.studentprefs, parsed_args.teamcount))

    make_test_pair(test_identifier, student_count, chair_count,
                   student_minimum_specificness, student_maximum_specificness,
                   possible_chair_attributes, possible_student_preferences, team_count)


main()
