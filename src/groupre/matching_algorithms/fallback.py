'''This module contains the fallback methods used by groupre.'''

import groupre_globals


def fallback(preference, chair):
    '''Fallback mechanic shared starting code.'''
    score = 0

    # NOTE "NOT" preference modifier:
    if '!' in preference.name:
        not_modifier = True
        pref_name = preference.name[1:len(preference.name)]
    else:
        not_modifier = False
        pref_name = preference.name

    if pref_name in chair.attributes:
        score += 1
    else:
        if 'front' in pref_name:
            fallback_limit = groupre_globals.FALLBACK_LIMIT_FRONT
        elif 'back' in pref_name:
            fallback_limit = groupre_globals.FALLBACK_LIMIT_BACK
        elif 'aisle' in pref_name:
            fallback_limit = groupre_globals.FALLBACK_LIMIT_AISLE

        preference_found = False
        fallback_level = 1

        if ':' in pref_name:
            fallback_start = int(pref_name.split('-', 1)[1].split(':', 1)[1])
        else:
            fallback_start = int(pref_name.split('-', 1)[1])

        if any('front-' in attribute for attribute in chair.attributes):
            while (not preference_found
                   and fallback_start + fallback_level < fallback_limit):
                if groupre_globals.FALLBACK_CHAIRS_FRONT[
                        fallback_start + fallback_level] in chair.attributes:
                    score += ((fallback_limit - fallback_level + 1)
                              / (fallback_limit + 1))
                    preference_found = True
                else:
                    fallback_level += 1
    if not_modifier:
        return -score
    else:
        return score
