'''This module contains the TeamStructure class used by groupre.'''


class TeamStructure():
    '''Data structure to store team attributes.'''

    team_chairs = []
    team_members = []
    score_total = 0
    team_id = None

    def __init__(self, chairs, team_id):
        self.team_id = team_id
        self.team_chairs = [
            chair for chair in chairs if int(chair.chair_id) == team_id]

    def add_member(self, student):
        '''Used to add a member to this team. Increases the score_total and
        adds the member to the team_members list.'''
        self.score_total += int(student.score)
        self.team_members.append(student)
