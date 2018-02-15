'''This module contains the fallback methods used by groupre.'''

import groupre_globals


def fallback(preference, chair):
    '''Fallback mechanic shared starting code.'''
    score = 0

    if preference.name in chair.attributes:
        # NOTE "NOT" preference modifier:
        if '!' in preference.name:
            not_modifier = True
        else:
            not_modifier = False

        if not_modifier:
            score -= 1
        else:
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
    '''Handles fallback for the front-* and front-*:* preferences.'''

    score = 0
    preference_found = False
    fallback_level = 1

    # NOTE "NOT" preference modifier:
    if '!' in preference.name:
        not_modifier = True
        pref_name = preference.name[1:len(preference.name)]
    else:
        not_modifier = False
        pref_name = preference.name

    if ':' in pref_name:
        fallback_start = int(pref_name.split('-', 1)[1].split(':', 1)[1])
    else:
        fallback_start = int(pref_name.split('-', 1)[1])

    if any('front-' in attribute for attribute in chair.attributes):
        while (not preference_found
               and fallback_start + fallback_level < groupre_globals.FALLBACK_LIMIT_FRONT):
            if groupre_globals.FALLBACK_CHAIRS_FRONT[
                    fallback_start + fallback_level] in chair.attributes:
                if not_modifier:
                    score -= ((groupre_globals.FALLBACK_LIMIT_FRONT - fallback_level + 1)
                              / (groupre_globals.FALLBACK_LIMIT_FRONT + 1))
                else:
                    score += ((groupre_globals.FALLBACK_LIMIT_FRONT - fallback_level + 1)
                              / (groupre_globals.FALLBACK_LIMIT_FRONT + 1))
                preference_found = True
            else:
                fallback_level += 1

    return score


def fallback_back(preference, chair):
    '''Handles fallback for the back-* and back-*:* preferences.'''

    score = 0
    preference_found = False
    fallback_level = 1

    # NOTE "NOT" preference modifier:
    if '!' in preference.name:
        not_modifier = True
        pref_name = preference.name[1:len(preference.name)]
    else:
        not_modifier = False
        pref_name = preference.name

    if ':' in pref_name:
        fallback_start = int(pref_name.split('-', 1)[1].split(':', 1)[1])
    else:
        fallback_start = int(pref_name.split('-', 1)[1])

    if any('back-' in attribute for attribute in chair.attributes):
        while (not preference_found
               and fallback_start + fallback_level < groupre_globals.FALLBACK_LIMIT_BACK):
            if groupre_globals.FALLBACK_CHAIRS_BACK[
                    fallback_start + fallback_level] in chair.attributes:
                if not_modifier:
                    score -= ((groupre_globals.FALLBACK_LIMIT_FRONT - fallback_level + 1)
                              / (groupre_globals.FALLBACK_LIMIT_FRONT + 1))
                else:
                    score += ((groupre_globals.FALLBACK_LIMIT_FRONT - fallback_level + 1)
                              / (groupre_globals.FALLBACK_LIMIT_FRONT + 1))
                preference_found = True
            else:
                fallback_level += 1
    return score


def fallback_aisle(preference, chair):
    '''Handles fallback for the aisle-* and aisle-*:* preferences.'''

    score = 0
    preference_found = False
    fallback_level = 1

    # NOTE "NOT" preference modifier:
    if '!' in preference.name:
        not_modifier = True
        pref_name = preference.name[1:len(preference.name)]
    else:
        not_modifier = False
        pref_name = preference.name

    if ':' in pref_name:
        fallback_start = int(pref_name.split('-', 1)[1].split(':', 1)[1])
    else:
        fallback_start = int(pref_name.split('-', 1)[1])

    if any('aisle-' in attribute for attribute in chair.attributes):
        while (not preference_found
               and fallback_start + fallback_level < groupre_globals.FALLBACK_LIMIT_AISLE):
            if groupre_globals.FALLBACK_CHAIRS_AISLE[
                    fallback_start + fallback_level] in chair.attributes:
                if not_modifier:
                    score -= ((groupre_globals.FALLBACK_LIMIT_FRONT - fallback_level + 1)
                              / (groupre_globals.FALLBACK_LIMIT_FRONT + 1))
                else:
                    score += ((groupre_globals.FALLBACK_LIMIT_FRONT - fallback_level + 1)
                              / (groupre_globals.FALLBACK_LIMIT_FRONT + 1))
                preference_found = True
            else:
                fallback_level += 1

    return score
