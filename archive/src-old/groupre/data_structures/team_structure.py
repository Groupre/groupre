'''This module contains the TeamStructure class used by groupre.'''

from typing import List, Union

from data_structures import Chair, Student


class TeamStructure():
    '''Data structure to store team attributes.'''

    team_chairs: List[Chair] = []
    team_members: List[Student] = []
    # score_total: int = 0
    gender_total: int = 0
    team_id: Union[str, int] = None

    def __init__(self, chairs: List[Chair], team_id: Union[str, int]):
        self.team_id = team_id
        self.team_chairs = [
            chair for chair in chairs if int(chair.team_id) == team_id]

    def add_member(self, student: Student):
        '''Used to add a member to this team.'''
        # self.score_total += int(student.score)
        for preference in student.preferences:
            if preference.name == 'gender':
                self.gender_total += 1
        self.team_members.append(student)
