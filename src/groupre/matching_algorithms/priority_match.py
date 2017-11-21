'''This module contains the priority_match method used by groupre.'''

import random

import groupre_globals
from data_structures import TeamMember


def fallback(preference, chair):
    '''Fallback mechanic shared starting code.'''
    score = 0

    if preference.name in chair.attributes:
        score += 1
        return score
    else:
        if 'front' in preference.name:
            score += fallback_front(preference, chair)
        elif 'back' in preference.name:
            score += fallback_back(preference, chair)
        elif 'aisle' in preference.name:
            score += fallback_aisle(preference, chair)

    return score


def fallback_front(preference, chair):
    '''Handles fallback for the front-* preference.'''

    # TODO This likely doesn't handle the fallback case for the front-BEGIN:END range preference
    # correctly as of yet. Will either need to create a new version for the range variant of the
    # preference and make this one ignore any preference with a ':' included.

    score = 0
    has_attribute = False
    preference_found = False
    fallback_level = 1
    fallback_start = int(preference.name.split('-', 1)[1])

    for attribute in chair.attributes:
        if 'front-' in attribute:
            has_attribute = True
            break

    if has_attribute:
        while (not preference_found
               and fallback_start + fallback_level <= groupre_globals.FALLBACK_LIMIT_FRONT):
            if groupre_globals.FALLBACK_CHAIRS_FRONT[
                    fallback_start + fallback_level] in chair.attributes:
                score += ((groupre_globals.FALLBACK_LIMIT_BACK - fallback_level + 1)
                          / (groupre_globals.FALLBACK_LIMIT_BACK + 1))
                preference_found = True
            else:
                fallback_level += 1

    return score


def fallback_back(preference, chair):
    '''Handles fallback for the back-* preference.'''

    score = 0
    has_attribute = False
    preference_found = False
    fallback_level = 1
    fallback_start = int(preference.name.split('-', 1)[1])

    for attribute in chair.attributes:
        if 'back-' in attribute:
            has_attribute = True
            break

    if has_attribute:
        while (not preference_found
               and fallback_start + fallback_level <= groupre_globals.FALLBACK_LIMIT_BACK):
            if groupre_globals.FALLBACK_CHAIRS_BACK[
                    fallback_start + fallback_level] in chair.attributes:
                score += ((groupre_globals.FALLBACK_LIMIT_BACK - fallback_level + 1)
                          / (groupre_globals.FALLBACK_LIMIT_BACK + 1))
                preference_found = True
            else:
                fallback_level += 1

    return score


def fallback_aisle(preference, chair):
    '''Handles fallback for the aisle-* preference.'''

    score = 0
    has_attribute = False
    preference_found = False
    fallback_level = 1
    fallback_start = int(preference.name.split('-', 1)[1])

    for attribute in chair.attributes:
        if 'aisle-' in attribute:
            has_attribute = True
            break

    if has_attribute:
        while (not preference_found
               and fallback_start + fallback_level <= groupre_globals.FALLBACK_LIMIT_AISLE):
            if groupre_globals.FALLBACK_CHAIRS_AISLE[
                    fallback_start + fallback_level] in chair.attributes:
                score += ((groupre_globals.FALLBACK_LIMIT_BACK - fallback_level + 1)
                          / (groupre_globals.FALLBACK_LIMIT_BACK + 1))
                preference_found = True
            else:
                fallback_level += 1

    return score


def range_front(preference, chair):
    '''Handles the front-BEGIN:END range preference.'''
    score = 0

    if 'front-' and ':' in preference.name:
        range_values = ('' + preference.name).split('-', 1)[1].split(':', 1)

        applicable_attributes = []
        current_value = int(range_values[0])
        while current_value <= int(range_values[1]):
            applicable_attributes.append('front-' + str(current_value))
            current_value += 1

        for attribute in applicable_attributes:
            if attribute in chair.attributes:
                # NOTE Adjusting score in the below manner can be misleading
                # when debugging and using the priority rating we have at the moment.

                # Score is adjusted by closeness to "origin".
                # Should assign seats closer to the front with higher value.
                found_value = int(('' + attribute).split('-', 1)[1])
                score += ((int(range_values[1]) - int(found_value) + 1)
                          / (int(range_values[1]) + 1))
    return score


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
