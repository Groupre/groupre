'''This module contains the create_teams method used by groupre.'''

import random

import groupre_globals
from matching_algorithms import (priority_match, random_match,
                                 gender_random_match)


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

    teams = []

    # Does not work, since this comparison changes as more students are matched.
    # For an accurate representation, we would need to do this loop after the sorting is done.
    if groupre_globals.GENDER_ENABLED:
        # Split our students into those who have the gender attribute and those who don't.
        # print('DEBUG: DOING GENDER MATCH')
        non_gender_students = []
        gender_students = []
        for student in students:
            has_gender = False
            for preference in student.preferences:
                if preference.name == 'gender':
                    # print('DEBUG: HAS GENDER')
                    has_gender = True

            if has_gender:
                gender_students.append(student)
            else:
                non_gender_students.append(student)

        # Randomize our student list orders.
        random.shuffle(non_gender_students)
        random.shuffle(gender_students)

        # Order our priority students by specificness.
        # sorted_gender_students = sorted(
        #     gender_students, key=lambda x: (
        #         x.vip, x.specificness, x.total_preference_value), reverse=True)

        # For this, we aren't considering other preferences.
        # TODO Implement gender matching on top of preference matching.
        for student in gender_students:
            match = gender_random_match(
                student, chairs, team_fields, team_structures)
            # See if we got a match.
            if match:
                teams.append(match)
                # Remove the student from students.
                students.remove(student)

        for student in non_gender_students:
            match = random_match(
                student, chairs, team_fields, team_structures)
            # See if we got a match.
            if match:
                teams.append(match)
                # Remove the student from students.
                students.remove(student)
    else:
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

        # Order our priority students by specificness.
        sorted_priority_students = sorted(
            priority_students, key=lambda x: (
                x.vip, x.total_preference_value, x.specificness), reverse=True)

        # NOTE debug
        # for student in sorted_priority_students:
        #     print(student.student_name, student.total_preference_value,
        #           student.specificness)

        # for student in sorted_priority_students:
        #     print(student.student_name, student.specificness)

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
    sorted_teams = sorted(teams, key=lambda x: (
        x.team_id, x.entry_data.get('CID')))

    ret_teams = []
    ret_teams.append(team_fields)
    for team in sorted_teams:
        current_ret = []
        for field in team_fields:
            current_ret.append(team.entry_data.get(field))
        ret_teams.append(current_ret)

    return ret_teams
