'''This module contains the random_match method used by groupre.'''

import random

import groupre_globals
import groupre_teammember


def random_match(student, chairs, team_fields, team_structures):
    '''This functionw will find a chair for the student at random.'''

    # Randomly choose a chair.
    chair = random.choice(chairs)
    chairs.remove(chair)

    # Fill out data fields for the pair we have matched.
    data_fields = []
    for field in team_fields:
        if field not in groupre_globals.DEBUG_FIELDS:
            if field in student.entry_data.keys():
                data_fields.append(student.entry_data[field])
            else:
                data_fields.append(chair.entry_data[field])

    # Fill priority_score field with NULL.
    data_fields.append("NULL")

    ret = groupre_teammember.TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # Used initially as back-bone for score-matching, may be unused in the future.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret
