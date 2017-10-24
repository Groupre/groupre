'''This module contains the Student class used by groupre.'''

import groupre_globals
import groupre_preference


class Student:
    '''A class dedicated to storing the preferences and specificness level of a given Student.'''

    student_id = None
    student_name = None
    vip = False
    score = None

    preferences = None
    specificness = None
    total_preference_value = None

    def __init__(self, required=None, preferences=None):
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
                        groupre_preference.Preference('front-0'))
                elif preference == 'back':
                    self.preferences.append(
                        groupre_preference.Preference('back-0'))
                elif preference == 'aisle':
                    self.preferences.append(
                        groupre_preference.Preference('aisle-0'))
                else:
                    self.preferences.append(
                        groupre_preference.Preference(preference))

        self.specificness = len(self.preferences)

        for preference in self.preferences:
            self.total_preference_value += preference.value
