#!/usr/bin/env python
'''This module will be used to take input from a chairs.csv and a students.csv
 and return a csv of sorted teams.'''

import csv
import sys
import random


class GenericEntry:
    '''An object to store data pertaining to input in the context of input.csv.'''

    entry_data = {}

    def __init__(self, fieldList=None, dataList=None):
        # print('---GenericEntry---')
        # print('fieldList:', fieldList)
        # print('dataList:', dataList)

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
            true_values = ['1', 'true', 'True', 'TRUE']
            false_values = ['FALSE', 'false', 'False', '0']

            if (fieldList[i] == 'TeamID' or fieldList[i] == 'PID'
                    or fieldList[i] == 'CID' or fieldList[i] == 'Score'):
                data[fieldList[i]] = dataList[i]
            elif dataList[i] in true_values:
                data[fieldList[i]] = True
            elif dataList[i] in false_values:
                data[fieldList[i]] = False
            else:
                data[fieldList[i]] = dataList[i]

            i += 1

        self.entry_data = data


class Student(GenericEntry):
    '''A GenericEntry with an extra specificness value for student-to-chair matching purposes.'''

    hasPriority = False
    specificness = 0

    def __init__(self, fieldList=None, dataList=None, requiredFieldsList=None):
        # print('---Student---')
        # print('fieldList:', fieldList)
        # print('dataList:', dataList)
        # print('requiredFields:', requiredFieldsList)

        # Argument error processing.
        if requiredFieldsList is None:
            raise ValueError('requiredFieldsList was null')

        GenericEntry.__init__(self, fieldList, dataList)

        # print(self.entry_data)

        for key in self.entry_data:
            if key not in requiredFieldsList:
                null_values = ['N/A', 'n/a', '',
                               'FALSE', 'false', 'False', '0']
                if self.entry_data[key] not in null_values:
                    self.specificness += 1

        # print(self.specificness)


class Team(GenericEntry):
    '''A GenericEntry with an extra TeamID value for team sorting purposes.'''

    team_id = 0

    def __init__(self, fieldList=None, dataList=None):
        GenericEntry.__init__(self, fieldList, dataList)

        self.team_id = int(self.entry_data['TeamID'])

        # print(self.team_id)


class TeamStructure():
    '''Data structure to store team score.'''

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


def create_teams(students, chairs, team_structures,
                 students_required_fields, chairs_required_fields, priority_fields):
    '''Fills out an array of teams to be returned and formatted as a csv.'''

    # Format our header for the categories the input specified.
    team_fields = []
    for field in students_required_fields:
        team_fields.append(field)
    for field in chairs_required_fields:
        team_fields.append(field)
    for field in priority_fields:
        team_fields.append(field)
    team_fields.append('PriorityScore')

    # Randomize our student order.
    random.shuffle(students)

    # Order them by specificness.
    sorted_students = sorted(students, key=lambda x: x.specificness)

    teams = []
    for student in sorted_students:
        teams.append(find_match(student, chairs, priority_fields,
                                team_fields, team_structures))

    # Sort by TeamID
    # for team in teams:
    #    print(team.team_id)
    sorted_teams = sorted(teams, key=lambda x: x.team_id)
    # for team in sorted_teams:
    #    print(team.team_id)

    ret_teams = []
    ret_teams.append(team_fields)
    for team in sorted_teams:
        ret_teams.append(team.entry_data.values())

    # VALIDATION
    i = 0
    while i < len(teams):
        item = teams[i]
        teams.remove(item)
        for other_item in teams:
            # print('item:', item.entry_data['CID'],
            #      'otherItem:', other_item.entry_data['CID'])
            if item.entry_data['CID'] == other_item.entry_data['CID']:
                raise ValueError("CID SEEN TWICE IN OUTPUT!")
        i += 1

    # for teamstruct in team_structures:
    #    print(teamstruct.team_id, teamstruct.score_total)

    return ret_teams


def find_match(student, chairs, priority_fields, team_fields, team_structures):
    '''This functionw will find a chair that is suitable for the student based
    on their preferences.'''

    # TODO: Team matching with adherance to Score isn't being done yet.

    # Find the chairs that we might fill with this student.
    i = 0
    while i < len(priority_fields):
        priority_field = priority_fields[i]
        # print(priority_field)

        # for chair in chairs:
        #    print('chair:', chair.entry_data[priority_field])

        # print('student:', student.entry_data[priority_field])

        possible_chairs = [chair for chair in chairs if chair.entry_data[priority_field]
                           == student.entry_data[priority_field]]
        # for chair in possible_chairs:
        #    print('possibleChair:', chair.entry_data)

        i += 1

    # Randomize and choose a chair.
    chair = random.choice(possible_chairs)
    chairs.remove(chair)

    # Fill out data fields for the pair we have matched.
    data_fields = []
    for field in team_fields:
        if field != 'PriorityScore':
            if field in student.entry_data.keys():
                data_fields.append(student.entry_data[field])
            else:
                data_fields.append(chair.entry_data[field])

    score_val = 0
    for field in priority_fields:
        if student.entry_data[field] == chair.entry_data[field]:
            score_val += 1
    score = '{} of {}'.format(score_val, student.specificness)
    data_fields.append(score)

    # print('team_fields', team_fields)
    # print('data_fields:', data_fields)

    ret = Team(team_fields, data_fields)
    # print(ret.entry_data)

    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        #print (this_team_id,'==',team_structure.team_id,'?')
        if int(this_team_id) == team_structure.team_id:
            # print('Adding',student.entry_data,'to',team_structure)
            team_structure.add_member(student)

    return ret


def build_team_structures(chairs):
    '''Builds list of lists of chairs based on shared team values.'''

    # Build available teams.
    num_teams = max(int(chair.entry_data['TeamID']) for chair in chairs)

    team_structures = []
    i = 1
    while i <= num_teams:
        team_structures.append(TeamStructure(chairs, i))
        i += 1

    # for team in all_teams:
    #    for chair in team.team_chairs:
    #        print(chair.entry_data)
    #    print(team.scoreTotal)

    return team_structures


def main(args):
    '''Executes the goal of the module.'''

    chairs_csv = ''
    students_csv = ''

    print('Number of extra arguments:', len(args) - 1)
    if len(args) == 1:
        print('No arguments, using default files.')
        chairs_csv = 'chairsTest.csv'
        students_csv = 'studentsTest.csv'
    else:
        print('Argument List:', str(args))

    students_required_fields = ['PID', 'StudentName', 'Score']
    chairs_required_fields = ['CID', 'TeamID']
    priority_fields = []

    chairs = []
    with open(chairs_csv, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = next(reader)

        # Error checking on chair input for minimum required fields.
        for required_field in chairs_required_fields:
            if required_field not in fields:
                raise ValueError(
                    'chairs csv file is lacking a', required_field, 'field!')

        # Pull our priority_fields by process of elimination.
        for field in fields:
            if field not in chairs_required_fields:
                priority_fields.append(field)

        for row in reader:
            chairs.append(GenericEntry(fields, row))

    # print('---BEGIN CHAIRS---')

    # for chair in chairs:
    #    print(chair.entry_data)

    # print('---END CHAIRS---')

    students = []
    with open(students_csv, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = next(reader)

        # Error checking on student input for minimum required fields.
        students_required_fields = ['PID', 'StudentName', 'Score']
        for required_field in students_required_fields:
            if required_field not in fields:
                raise ValueError(
                    'students csv file is lacking a', required_field, 'field!')

        # Since students is filled out after chairs, use the already obtained priority_fields
        # to verify that our csvs match.
        for field in fields:
            if field not in students_required_fields:
                if field not in priority_fields:
                    raise ValueError(
                        'priority_fields between students csv and chairs csv do not match!')

        for row in reader:
            students.append(Student(fields, row, students_required_fields))

    # print('---BEGIN STUDENTS---')

    # for student in students:
    #    print(student.entry_data, student.specificness)

    # print('---END STUDENTS---')

    # Run our algorithm to match students to chairs within teams, keeping in mind their
    # scores and preferences.
    team_structures = build_team_structures(chairs)
    teams = create_teams(students, chairs, team_structures,
                         students_required_fields, chairs_required_fields, priority_fields)

    # print('---BEGIN TEAMS---')

    # for team in teams:
    #    print(team)

    # print('---END TEAMS---')

    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for team in teams:
            writer.writerow(team)


main(sys.argv)
