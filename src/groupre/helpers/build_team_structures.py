'''This module contains the build_team_structures method used by groupre.'''

from data_structures.team_structure import TeamStructure


def build_team_structures(chairs):
    '''Builds a team_structure for every team provided. Provides unfinished
    backbone for matching criteria among members that belong to a given team.'''

    # Build and return structures for all available teams.
    num_teams = max(int(chair.team_id) for chair in chairs)
    team_structures = []
    i = 1
    while i <= num_teams:
        team_structures.append(TeamStructure(chairs, i))
        i += 1
    return team_structures
