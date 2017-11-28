'''This module contains the priority_match method used by groupre.'''

import random

from data_structures import TeamMember
import groupre_globals
from .fallback import fallback
from .range_preference import range_front


def priority_match(student, chairs, team_fields, team_structures):
    '''This functionw will find a chair that is suitable for the student based
    on their preferences.'''

    # Find the possible_chairs that best match this student's priorities.
    scored_chairs = {}
    for chair in chairs:
        score = 0

        for preference in student.preferences:
            score += range_front(preference, chair)

            if score == 0 and preference.name in chair.attributes:
                score += 1

        scored_chairs[chair] = score

    max_score = max(scored_chairs.values())

    if groupre_globals.FALLBACK_ENABLED and max_score == 0:
        # We likely need to see if fallback chairs can provide
        # a better maximum score for this student.

        # Re-score the chairs while looking for fallback options this time.
        scored_chairs = {}
        for chair in chairs:
            score = 0

            for preference in student.preferences:
                score += fallback(preference, chair)

            scored_chairs[chair] = score

        max_score = max(scored_chairs.values())

    best_chairs = [
        chair for chair in scored_chairs if scored_chairs[chair] == max_score]

    # Randomize and choose a chair.
    chair = random.choice(best_chairs)
    chairs.remove(chair)

    # Fill out data fields for the pair we have matched.
    data_fields = []

    data_fields.append(student.student_id)
    data_fields.append(student.student_name)
    data_fields.append(student.vip)
    data_fields.append(student.score)

    data_fields.append(chair.chair_id)
    data_fields.append(chair.team_id)

    priority_score_val = max_score

    priority_score = '{} of {}'.format(
        priority_score_val, student.specificness)

    # Debug value to see how well priority matching satisfied student priorities.
    groupre_globals.STUDENT_PRIORITY_VALUE += priority_score_val
    groupre_globals.STUDENT_PRIORITY_TOTAL += student.specificness

    data_fields.append(priority_score)

    unmatched_preferences = ''
    for preference in student.preferences:
        if 'front-' and ':' in preference.name:
            found_attr = False
            for attribute in chair.attributes:
                if 'front' not in attribute:
                    found_attr = True

            if not found_attr:
                unmatched_preferences += '[' + \
                    preference.name + ']'
        elif preference.name not in chair.attributes:
            unmatched_preferences += '[' + preference.name + ']'
    data_fields.append(unmatched_preferences)

    ret = TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # TODO Use this for score-matching and other team-related matching criteria.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret
