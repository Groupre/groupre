'''This module contains the range_preference related functions used by groupre.'''

from typing import List

from data_structures import Chair


def range_preference(pref_name: str, chair: Chair):
    '''Handles the preference-BEGIN:END range preference.'''
    score: int = 0

    # ':' is assumed to be in pref_name

    pref_prefix = pref_name.split('-', 1)[0] + '-'
    range_values = pref_name.split('-', 1)[1].split(':', 1)

    applicable_attributes: List[str] = []
    current_value = int(range_values[0])
    while current_value <= int(range_values[1]):
        applicable_attributes.append(pref_prefix + str(current_value))
        current_value += 1

    for attribute in applicable_attributes:
        if attribute in chair.attributes:
            # NOTE Adjusting score in the below manner can be misleading
            # when debugging and using the priority rating we have at the moment.

            # Score is adjusted by closeness to "origin".
            # Should assign seats closer to the front with higher value.
            found_value = int(attribute.split('-', 1)[1])

            score += ((int(range_values[1]) - int(found_value) + 1)
                      / (int(range_values[1]) + 1))

    return score
