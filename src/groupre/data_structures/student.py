'''This module contains the Student class used by groupre.'''

from typing import List, Union

import groupre_globals
from data_structures import Preference


class Student:
    '''A class dedicated to storing the preferences and specificness level of a given Student.'''

    student_id: Union[int, str] = None
    student_name: str = None
    vip: bool = False
    score: int = None

    preferences: List[str] = None
    specificness: int = None
    total_preference_value: int = None

    def __init__(self, required=None, preferences: List[str]=None):
        self.student_id = required[0]
        self.student_name = required[1]
        self.vip = required[2]
        self.score = required[3]

        self.preferences = []
        self.specificness = 0
        self.total_preference_value = 0

        for preference in preferences:
            if preference not in groupre_globals.NULL_VALUES:
                if preference == 'front':
                    self.preferences.append(
                        Preference('front-0'))
                elif preference == 'back':
                    self.preferences.append(
                        Preference('back-0'))
                elif preference == 'aisle':
                    self.preferences.append(
                        Preference('aisle-0'))
                else:
                    self.preferences.append(
                        Preference(preference))

        self.specificness = len(self.preferences)

        for preference in self.preferences:
            self.total_preference_value += preference.value
