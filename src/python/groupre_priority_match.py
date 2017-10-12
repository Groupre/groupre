'''This module contains the priority_match method used by groupre.'''

import random

import groupre_globals
import groupre_teammember


def priority_match(student, chairs, priority_fields, team_fields, team_structures):
    '''This functionw will find a chair that is suitable for the student based
    on their preferences.'''

    # Find the possible_chairs that best match this student's priorities.
    scored_chairs = {}
    for chair in chairs:
        score = 0
        for preference in student.preferences:
            if preference in chair.attributes:
                score += 1
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

    data_fields.append(student.student_id)
    data_fields.append(student.student_name)
    data_fields.append(student.score)

    data_fields.append(chair.chair_id)
    data_fields.append(chair.team_id)

    # For debugging purposes, rates how well the PriorityMatch went.
    priority_score_val = 0
    for preference in student.preferences:
        if preference in chair.attributes:
            priority_score_val += 1

    priority_score = '{} of {}'.format(
        priority_score_val, student.specificness)

    # Debug value to see how well priority matching satisfied student priorities.
    groupre_globals.STUDENT_PRIORITY_VALUE += priority_score_val
    groupre_globals.STUDENT_PRIORITY_TOTAL += student.specificness

    data_fields.append(priority_score)

    unmatched_preferences = ""
    for preference in student.preferences:
        if preference not in chair.attributes:
            unmatched_preferences += "[" + preference + "]"
    data_fields.append(unmatched_preferences)

    ret = groupre_teammember.TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # Used initially as back-bone for score-matching, may be unused in the future.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret
