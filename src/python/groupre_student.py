'''This module contains the Student class used by groupre.'''

import groupre_globals


class Student:
    '''A class dedicated to storing the preferences and specificness level of a given Student.'''

    student_id = None
    student_name = None
    score = None

    preferences = None
    specificness = None

    def __init__(self, required=None, preferences=None):
        self.student_id = required[0]
        self.student_name = required[1]
        self.score = required[2]
        self.preferences = []
        self.specificness = 0

        for preference in preferences:
            if preference not in groupre_globals.NULL_VALUES:
                self.preferences.append(preference)

        self.specificness = len(self.preferences)
