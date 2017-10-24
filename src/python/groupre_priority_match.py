'''This module contains the priority_match method used by groupre.'''

import random

import groupre_globals
import groupre_teammember


def priority_match(student, chairs, team_fields, team_structures):
    '''This functionw will find a chair that is suitable for the student based
    on their preferences.'''

    print('\n-----\nmatching student:', student)
    for preference in student.preferences:
        print(preference.name, preference.value)

    # Find the possible_chairs that best match this student's priorities.
    scored_chairs = {}
    for chair in chairs:
        score = 0

        for preference in student.preferences:

            if preference.name == 'front-0':
                print(chair.attributes)

            # print(student.preferences)

            # Handling of front-BEGIN:END range preference.
            if 'front-' and ':' in preference.name:
                range_values = ('' + preference.name).split('-',
                                                            1)[1].split(':', 1)

                # print('range_values:', range_values)

                applicable_attributes = []
                current_value = int(range_values[0])
                while current_value <= int(range_values[1]):
                    applicable_attributes.append('front-' + str(current_value))
                    current_value += 1

                # print('applicable_attributes:', applicable_attributes)

                for attribute in applicable_attributes:
                    if attribute in chair.attributes:
                        # NOTE Adjusing score in the below manner can be misleading
                        # when debugging and using the priority rating we have at the moment.

                        # Score is adjusted by closeness to "origin".
                        # Should assign seats closer to the front with higher value.
                        found_value = int(('' + attribute).split('-', 1)[1])
                        score += (1 * ((int(range_values[1]) - int(found_value) +
                                        1) / (int(range_values[1]) + 1)))

                        # print('found chair with attribute:',
                        #       attribute, '|', 'score:', score)

            elif preference.name in chair.attributes:
                score += 1

            # if preference == 'front-0':
            #     exit()

        scored_chairs[chair] = score

    max_score = max(scored_chairs.values())

    print('initial max_score:', max_score)

    if groupre_globals.FALLBACK_ENABLED:
        if max_score == 0:
            # We likely need to see if fallback chairs can provide
            # a better maximum score for this student.

            # Re-score the chairs, but also look for fallback options this time.
            scored_chairs = {}
            for chair in chairs:
                score = 0
                for preference in student.preferences:
                    if preference.name in chair.attributes:
                        score += 1
                    else:
                        # We need to get the fallbacks for the preference
                        # that the student wasn't able to find a match for.

                        has_attribute = False
                        preference_found = False

                        # We start at fallback_kevel 1 since we know that
                        # level 0 (the original) was not found.
                        fallback_level = 1

                        if 'front' in preference.name:
                            for attribute in chair.attributes:
                                if 'front-' in attribute:
                                    has_attribute = True

                            if has_attribute:
                                while (not preference_found
                                       and fallback_level <= groupre_globals.FALLBACK_LIMIT_FRONT):
                                    if groupre_globals.FALLBACK_CHAIRS_FRONT in chair.attributes:
                                        score += (1 * ((groupre_globals.FALLBACK_LIMIT_BACK
                                                        - fallback_level + 1) /
                                                       (groupre_globals.FALLBACK_LIMIT_BACK + 1)))
                                        preference_found = True
                                    else:
                                        fallback_level += 1

                        elif 'back' in preference.name:
                            for attribute in chair.attributes:
                                if 'back-' in attribute:
                                    has_attribute = True

                            if has_attribute:
                                while (not preference_found
                                       and fallback_level <= groupre_globals.FALLBACK_LIMIT_BACK):
                                    if groupre_globals.FALLBACK_CHAIRS_BACK in chair.attributes:
                                        score += (1 * ((groupre_globals.FALLBACK_LIMIT_BACK
                                                        - fallback_level + 1) /
                                                       groupre_globals.FALLBACK_LIMIT_BACK + 1))
                                        preference_found = True
                                    else:
                                        fallback_level += 1

                        elif 'aisle' in preference.name:
                            for attribute in chair.attributes:
                                if 'aisle-' in attribute:
                                    has_attribute = True

                            if has_attribute:
                                while (not preference_found
                                       and fallback_level <= groupre_globals.FALLBACK_LIMIT_AISLE):
                                    if groupre_globals.FALLBACK_CHAIRS_AISLE in chair.attributes:
                                        score += (1 * ((groupre_globals.FALLBACK_LIMIT_BACK
                                                        - fallback_level + 1) /
                                                       groupre_globals.FALLBACK_LIMIT_BACK + 1))
                                        preference_found = True
                                    else:
                                        fallback_level += 1

                scored_chairs[chair] = score

            max_score = max(scored_chairs.values())
            print('fallback max_score:', max_score)

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

    print('chosen chair:', chair)
    print(chair.attributes, '\n')

    # Fill out data fields for the pair we have matched.
    data_fields = []

    data_fields.append(student.student_id)
    data_fields.append(student.student_name)
    data_fields.append(student.vip)
    data_fields.append(student.score)

    data_fields.append(chair.chair_id)
    data_fields.append(chair.team_id)

    # For debugging purposes, rates how well the PriorityMatch went.
    # priority_score_val = 0
    # for preference in student.preferences:
    #     if preference in chair.attributes:
    #         priority_score_val += 1
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

    ret = groupre_teammember.TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # Used initially as back-bone for score-matching, may be unused in the future.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret
