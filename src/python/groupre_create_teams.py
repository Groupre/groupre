'''This module contains the create_teams method used by groupre.'''

import random

import groupre_globals
import groupre_random_match
import groupre_priority_match


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
        priority_students, key=lambda x: x.specificness, reverse=True)

    teams = []
    for student in sorted_priority_students:
        match = groupre_priority_match.priority_match(
            student, chairs, team_fields, team_structures)

        # See if we got a match.
        if match:
            teams.append(match)

            # Remove the student from students.
            students.remove(student)

    for student in no_priority_students:
        match = groupre_random_match.random_match(
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
        ret_teams.append(team.entry_data.values())

    return ret_teams
