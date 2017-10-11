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
        if field not in groupre_globals.DEBUG_FIELDS:
            if field in student.entry_data.keys():
                data_fields.append(student.entry_data[field])
            else:
                data_fields.append(chair.entry_data[field])

    # For debugging purposes, rates how well the PriorityMatch went.
    priority_score_val = 0
    for field in priority_fields:
        if str(student.entry_data[field]) not in groupre_globals.NULL_VALUES:
            if student.entry_data[field] == chair.entry_data[field]:
                priority_score_val += 1

    priority_score = '{} of {}'.format(
        priority_score_val, student.specificness)

    # Debug value to see how well priority matching satisfied student priorities.
    # global STUDENT_PRIORITY_VALUE
    groupre_globals.STUDENT_PRIORITY_VALUE += priority_score_val

    # global STUDENT_PRIORITY_TOTAL
    groupre_globals.STUDENT_PRIORITY_TOTAL += student.specificness

    # global STUDENT_FULL_PRIORITY
    if priority_score_val == student.specificness:
        groupre_globals.STUDENT_FULL_PRIORITY += 1

    data_fields.append(priority_score)

    ret = groupre_teammember.TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # Used initially as back-bone for score-matching, may be unused in the future.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret
