'''This module contains the random_match method used by groupre.'''

import random

from data_structures import TeamMember


def gender_random_match(student, chairs, team_fields, team_structures):
    '''This method will find a team for a given student based on their
    gender attribute..'''

    # This code assumes that teams are of sizes greater than at least 4.

    # Find a team to put this student in.
    full_gender = []
    some_gender = []
    no_gender = []
    for team in team_structures:
        if team.gender_total > 0:
            if team.gender_total >= 3:
                full_gender.append(team)
            else:
                some_gender.append(team)
        else:
            no_gender.append(team)

    len_some = len(some_gender)
    len_no = len(no_gender)

    chair = None
    while chair is None:
        if len_some > 0:
            # Pick a team to help fill up.
            team = random.choice(some_gender)
        elif len_no > 0:
            # Pick a team to start filling.
            team = random.choice(no_gender)
        else:
            # Add to a full_gender team that only has a gender_total of 3.
            possible_teams = []
            for full_team in full_gender:
                if full_team.gender_total == 3:
                    possible_teams.append(full_team)

            len_possible = len(possible_teams)
            if len_possible == 0:
                print('''We don't have any applicable teams for this student.
                Adding to a random full team.''')
                team = random.choice(full_gender)
            else:
                team = random.choice(possible_teams)

        # Get an unoccupied chair in the chosen team.
        for team_chair in team.team_chairs:
            if team_chair in chairs:
                chair = team_chair
            else:
                print('No available unoccupied chair located in this team.')

    chairs.remove(chair)

   # Fill out data fields for the pair we have matched.
    data_fields = []

    data_fields.append(student.student_id)
    data_fields.append(student.student_name)
    data_fields.append(student.vip)
    data_fields.append(student.score)

    data_fields.append(chair.chair_id)
    data_fields.append(chair.team_id)

    # Fill priority_score field with NULL.
    data_fields.append('NULL')

    unmatched_preferences = ''
    for preference in student.preferences:
        if preference not in chair.attributes:
            unmatched_preferences += '[' + preference + ']'
    data_fields.append(unmatched_preferences)

    ret = TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # Used initially as back-bone for score-matching, may be unused in the future.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret
