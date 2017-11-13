'''This module contains the TeamMember class used by groupre.'''

from data_structures import GenericEntry


class TeamMember(GenericEntry):
    '''A GenericEntry with an extra TeamID value for team sorting purposes.'''

    team_id = 0

    def __init__(self, fieldList=None, dataList=None):
        GenericEntry.__init__(self, fieldList, dataList)
        self.team_id = int(self.entry_data['TeamID'])
