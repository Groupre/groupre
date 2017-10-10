#!/usr/bin/env python
'''This module will be used to take input from a chairs.csv and a students.csv
 and return a csv of sorted teams.'''

import csv
import sys
import random
import time

STUDENT_REQUIRED_FIELDS = ['PID', 'StudentName', 'Score']
CHAIR_REQUIRED_FIELDS = ['CID', 'TeamID']
DEBUG_FIELDS = ['PriorityScore']

TRUE_VALUES = ['1', 'true', 'True', 'TRUE']
FALSE_VALUES = ['FALSE', 'false', 'False', '0']
NULL_VALUES = ['N/A', 'n/a', '', 'FALSE', 'false', 'False', '0']


global STUDENT_FULL_PRIORITY
STUDENT_FULL_PRIORITY = 0

global STUDENT_PRIORITY_VALUE
STUDENT_PRIORITY_VALUE = 0

global STUDENT_PRIORITY_TOTAL
STUDENT_PRIORITY_TOTAL = 0


class GenericEntry:
    '''An object to store data pertaining to input in the context of input.csv.'''

    entry_data = {}

    def __init__(self, fieldList=None, dataList=None):
        # Argument error processing.
        if fieldList is None:
            raise ValueError('fieldList was null')
        if dataList is None:
            raise ValueError('dataList was null')
        if len(fieldList) != len(dataList):
            raise ValueError(
                'fieldList and dataList do not have the same length')

        # Populate this input's data with the generic input data.
        data = {}
        i = 0
        while i != len(fieldList):
            if fieldList[i] in STUDENT_REQUIRED_FIELDS or fieldList[i] in CHAIR_REQUIRED_FIELDS:
                data[fieldList[i]] = dataList[i]
            elif dataList[i] in TRUE_VALUES:
                data[fieldList[i]] = True
            elif dataList[i] in FALSE_VALUES:
                data[fieldList[i]] = False
            else:
                data[fieldList[i]] = dataList[i]

            i += 1

        self.entry_data = data


class Student(GenericEntry):
    '''A GenericEntry with an extra specificness value for student-to-chair matching purposes.'''

    specificness = 0

    def __init__(self, fieldList=None, dataList=None):
        GenericEntry.__init__(self, fieldList, dataList)

        for field in self.entry_data:
            if field not in STUDENT_REQUIRED_FIELDS:
                if str(self.entry_data[field]) not in NULL_VALUES:
                    self.specificness += 1


class TeamMember(GenericEntry):
    '''A GenericEntry with an extra TeamID value for team sorting purposes.'''

    team_id = 0

    def __init__(self, fieldList=None, dataList=None):
        GenericEntry.__init__(self, fieldList, dataList)
        self.team_id = int(self.entry_data['TeamID'])


class TeamStructure():
    '''Data structure to store team attributes.'''

    team_chairs = []
    team_members = []
    score_total = 0
    team_id = None

    def __init__(self, chairs, team_id):
        self.team_id = team_id
        self.team_chairs = [
            chair for chair in chairs if int(chair.entry_data['TeamID']) == team_id]

    def add_member(self, student):
        '''Used to add a member to this team. Increases the score_total and
        adds the member to the team_members list.'''
        self.score_total += int(student.entry_data['Score'])
        self.team_members.append(student.entry_data)


def create_teams(students, chairs, team_structures, priority_fields):
    '''Fills out an array of teams to be returned and formatted as a csv.'''

    # Format our header for the categories the input specified.
    team_fields = []
    for field in STUDENT_REQUIRED_FIELDS:
        team_fields.append(field)
    for field in CHAIR_REQUIRED_FIELDS:
        team_fields.append(field)
    for field in priority_fields:
        team_fields.append(field)

    # For debugging purposes, rates how well the PriorityMatch went.
    team_fields.append('PriorityScore')

    # Split our students into those who have priorities and those who don't.
    no_priority_students = []
    priority_students = []
    for student in students:
        if student.specificness == 0:
            no_priority_students.append(student)
        elif student.specificness > 0:
            priority_students.append(student)

    # Randomize our student list orders.
    random.shuffle(no_priority_students)
    random.shuffle(priority_students)

    # Order our priority students  by specificness.
    sorted_priority_students = sorted(
        priority_students, key=lambda x: x.specificness, reverse=True)

    teams = []
    for student in sorted_priority_students:
        match = priority_match(student, chairs, priority_fields,
                               team_fields, team_structures)

        # See if we got a match.
        if match:
            teams.append(match)

            # Remove the student from students.
            students.remove(student)

    for student in no_priority_students:
        match = random_match(student, chairs, team_fields, team_structures)

        # See if we got a match.
        if match:
            teams.append(match)

            # Remove the student from students.
            students.remove(student)

    # Sort by TeamID
    sorted_teams = sorted(teams, key=lambda x: x.team_id)

    ret_teams = []
    ret_teams.append(team_fields)
    for team in sorted_teams:
        ret_teams.append(team.entry_data.values())

    # DEBUG: VALIDATION (Relies on CID being unique!)
    # i = 0
    # while i < len(teams):
    #    item = teams[i]
    #    teams.remove(item)
    #    for other_item in teams:
    #     print('item:', item.entry_data['CID'],
    #          'otherItem:', other_item.entry_data['CID'])
    #        if item.entry_data['CID'] == other_item.entry_data['CID']:
    #            raise ValueError("CID SEEN TWICE IN OUTPUT!")
    #    i += 1
    # DEBUG: VALIDATION (Relies on CID being unique!)

    return ret_teams


def random_match(student, chairs, team_fields, team_structures):
    '''This functionw will find a chair for the student at random.'''

    # Randomly choose a chair.
    chair = random.choice(chairs)
    chairs.remove(chair)

    # Fill out data fields for the pair we have matched.
    data_fields = []
    for field in team_fields:
        if field not in DEBUG_FIELDS:
            if field in student.entry_data.keys():
                data_fields.append(student.entry_data[field])
            else:
                data_fields.append(chair.entry_data[field])

    # Fill priority_score field with NULL.
    data_fields.append("NULL")

    ret = TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # Used initially as back-bone for score-matching, may be unused in the future.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret


def priority_match(student, chairs, priority_fields, team_fields, team_structures):
    '''This functionw will find a chair that is suitable for the student based
    on their preferences.'''

    # Find the possible_chairs that best match this student's priorities.
    scored_chairs = {}
    for chair in chairs:
        score = 0
        i = 0
        while i < len(priority_fields):
            priority_field = priority_fields[i]
            if chair.entry_data[priority_field] == student.entry_data[priority_field]:
                score += 1
            i += 1
        scored_chairs[chair] = score

    max_score = max(scored_chairs.values())
    to_remove = []
    num_found = 0
    for chair in scored_chairs:
        if scored_chairs[chair] != max_score:
            to_remove.append(chair)
        else:
            num_found += 1

    for chair in to_remove:
        scored_chairs.pop(chair)

    best_chairs = []
    for chair in scored_chairs:
        best_chairs.append(chair)

    # Randomize and choose a chair.
    chair = random.choice(best_chairs)
    chairs.remove(chair)

    # Fill out data fields for the pair we have matched.
    data_fields = []
    for field in team_fields:
        if field not in DEBUG_FIELDS:
            if field in student.entry_data.keys():
                data_fields.append(student.entry_data[field])
            else:
                data_fields.append(chair.entry_data[field])

    # For debugging purposes, rates how well the PriorityMatch went.
    priority_score_val = 0
    for field in priority_fields:
        if str(student.entry_data[field]) not in NULL_VALUES:
            if student.entry_data[field] == chair.entry_data[field]:
                priority_score_val += 1

    priority_score = '{} of {}'.format(
        priority_score_val, student.specificness)

    # Debug value to see how well priority matching satisfied student priorities.
    global STUDENT_PRIORITY_VALUE
    STUDENT_PRIORITY_VALUE += priority_score_val

    global STUDENT_PRIORITY_TOTAL
    STUDENT_PRIORITY_TOTAL += student.specificness

    global STUDENT_FULL_PRIORITY
    if priority_score_val == student.specificness:
        STUDENT_FULL_PRIORITY += 1

    data_fields.append(priority_score)

    ret = TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # Used initially as back-bone for score-matching, may be unused in the future.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret


def build_team_structures(chairs):
    '''Builds a team_structure for every team provided. Provides unfinished
    backbone for matching criteria among members that belong to a given team.'''

    # Build and return structures for all available teams.
    num_teams = max(int(chair.entry_data['TeamID']) for chair in chairs)
    team_structures = []
    i = 1
    while i <= num_teams:
        team_structures.append(TeamStructure(chairs, i))
        i += 1
    return team_structures


def main(args):
    '''Executes the goal of the module.'''

    # Initialization of csv files.
    chairs_csv = None
    students_csv = None

    # Handling of arguments for csv file selection.
    if len(args) == 1:
        print('''Not enough input arguments provided.
        Please provide groupre27.py with a chairs csv and students csv (in that order).''')
        return
    # Debug default case, use internal test files.
    # TODO Replace with an automated test that invokes groupre27.py for all tests.
    # print('No arguments, using default files.')
    # chairs_csv = 'chairsTest.csv'
    # students_csv = 'studentsTest.csv'
    # else:

    # Actual use case: chairs argument must come before students argument.
    print('Argument List:', str(args[1:2]))
    chairs_csv = args[1]
    students_csv = args[2]

    priority_fields = []

    chairs = []
    with open(chairs_csv, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = next(reader)

        # Error checking on chair input for minimum required fields.
        for required_field in CHAIR_REQUIRED_FIELDS:
            if required_field not in fields:
                raise ValueError(
                    'chairs csv file is lacking a', required_field, 'field!')

        # Pull our priority_fields by process of elimination.
        for field in fields:
            if field not in CHAIR_REQUIRED_FIELDS:
                priority_fields.append(field)

        for row in reader:
            chairs.append(GenericEntry(fields, row))

    students = []
    with open(students_csv, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = next(reader)

        # Error checking on student input for minimum required fields.
        for required_field in STUDENT_REQUIRED_FIELDS:
            if required_field not in fields:
                raise ValueError(
                    'students csv file is lacking a', required_field, 'field!')

        # Since students is filled out after chairs, use the already obtained priority_fields
        # to verify that our csvs match.
        for field in fields:
            if field not in STUDENT_REQUIRED_FIELDS:
                if field not in priority_fields:
                    raise ValueError(
                        'priority_fields between students csv and chairs csv do not match!')

        for row in reader:
            students.append(Student(fields, row))

    # Benchmarking statement.
    total_students = len(students)
    print('Processing', total_students, 'students...')

    # Run our algorithm to match students to chairs within teams, keeping in mind their
    # scores and preferences.
    team_structures = build_team_structures(chairs)
    teams = create_teams(students, chairs, team_structures, priority_fields)

    # Write our output to a csv.
    # NOTE "newline=''" required when writing on an OS that ends lines in CRLF rather than just LF.
    print('----------')
    print('Seats assigned. Writing to csv.')
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for team in teams:
            writer.writerow(team)

    print('----------')
    print('Student Priority Rating:',
          round(STUDENT_PRIORITY_VALUE / STUDENT_PRIORITY_TOTAL * 100, 2), '%')
    print('Student Full Priority Rating:',
          STUDENT_FULL_PRIORITY / total_students * 100, '%')
    print('----------')


# Benchmark timer start.
time.clock()
print('----------')

main(sys.argv)

# Benchmark timer end.
print(time.clock(), 'seconds elapsed.')
print('----------')
