'''This module contains the Preference class used by groupre.'''


class Preference:
    '''A class dedicated to storing the preferences and specificness level of a given Student.'''

    name = None
    value = None

    def __init__(self, name):
        self.name = name

        if name == 'front-0':
            self.value = 5
        elif name == 'back-0':
            self.value = 5
        elif name == 'aisle-0':
            self.value = 5
        else:
            self.value = 1
