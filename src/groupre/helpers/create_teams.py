'''This module contains the create_teams method used by groupre.'''

import random

import groupre_globals
from matching_algorithms import priority_match, random_match


def create_teams(students, chairs, team_structures):
    '''Fills out an array of teams to be returned and formatted as a csv.'''

    # Format our header for the categories the input specified.
    team_fields = []
    for field in groupre_globals.STUDENT_REQUIRED_FIELDS:
        team_fields.append(field)
    for field in groupre_globals.CHAIR_REQUIRED_FIELDS:
        team_fields.append(field)

    # For debugging purposes:
    team_fields.append('Priority Score')
    team_fields.append('Unsatisfied Preferences')

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
        priority_students, key=lambda x: (
            x.vip, x.specificness, x.total_preference_value), reverse=True)

    # for student in sorted_priority_students:
    #     print(student, student.vip, student.specificness,
    #           student.total_preference_value)
    #     for preference in student.preferences:
    #         print(preference.name)

    # for student in sorted_priority_students:
    #     print(student.vip, student.specificness)

    teams = []
    for student in sorted_priority_students:
        match = priority_match(
            student, chairs, team_fields, team_structures)

        # See if we got a match.
        if match:
            teams.append(match)

            # Remove the student from students.
            students.remove(student)

    for student in no_priority_students:
        match = random_match(
            student, chairs, team_fields, team_structures)

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
        current_ret = []
        for field in team_fields:
            current_ret.append(team.entry_data.get(field))
        ret_teams.append(current_ret)

    return ret_teams
