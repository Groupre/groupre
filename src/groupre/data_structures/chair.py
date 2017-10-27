'''This module contains the Chair class used by groupre.'''

import groupre_globals


class Chair:
    '''A class dedicated to storing the attributes of a given Chair.'''

    chair_id = None
    team_id = None
    attributes = None

    def __init__(self, required=None, attributes=None):
        self.chair_id = required[0]
        self.team_id = required[1]
        self.attributes = []

        for attribute in attributes:
            if attribute not in groupre_globals.NULL_VALUES:
                self.attributes.append(attribute)
