'''This module contains the gender_random_match method used by groupre.'''

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
        # print('team: ' + str(team.team_id) + ' has team.gender_total: ' + str(team.gender_total))
        if int(team.gender_total) > 0:
            if int(team.gender_total) >= 3:
                full_gender.append(team)
            else:
                some_gender.append(team)
        else:
            no_gender.append(team)

    len_some = len(some_gender)
    len_no = len(no_gender)

    team = None
    chair = None
    found_chair = False

    # print('len_some: ' + str(len_some))
    # print('len_no: ' + str(len_no))

    num_checked = 0

    while chair is None:
        if len_some > 0 and num_checked < len_some:
            # Pick a team to help fill up.
            team = random.choice(some_gender)
            some_gender.remove(team)
            # team = some_gender[num_checked]

        elif len_no > 0 and num_checked < len_no:
            # Pick a team to start filling.
            team = random.choice(no_gender)
            no_gender.remove(team)
            # team = no_gender[num_checked]
        else:
            # Add to a full_gender team that only has a gender_total of 3.
            possible_teams = []
            for full_team in full_gender:
                if int(full_team.gender_total) == 3:
                    possible_teams.append(full_team)

            len_possible = len(possible_teams)
            if len_possible == 0:
                print('''We don't have any applicable teams for this student.
                Adding to a random full team.''')
                team = random.choice(full_gender)
                full_gender.remove(team)
            else:
                team = random.choice(possible_teams)
                full_gender.remove(team)
                # team = possible_teams[num_checked]

        # Get an unoccupied chair in the chosen team.
        # string = ''
        # for team_chair in team.team_chairs:
        #     string += team_chair.chair_id + ', '
        # print('team_chairs: ' + string,
        #       'team_gender_total: ' + str(team.gender_total))

        # string = ''
        # for c in chairs:
        #     string += c.chair_id + ', '
        # print('chairs: ' + string)

        for team_chair in team.team_chairs:
            for leftover_chairs in chairs:
                # print(str(team_chair.chair_id) + ' =?= ' + str(leftover_chairs.chair_id))
                if str(team_chair.chair_id) == str(leftover_chairs.chair_id):
                    found_chair = True
                    # print("found chair: " + team_chair.chair_id)

            if found_chair:
                # print("Used team has gender total: " + str(team.gender_total))
                chair = team_chair
                break
        # if not found_chair:
            # print('No available unoccupied chair located in this team.')

        num_checked += 1

    found_chair = False
    # print('using chair: ' + chair.chair_id)
    for other_chair in chairs:
        # print(chair.chair_id + ' =?= ' + other_chair.chair_id)
        if str(chair.chair_id) == str(other_chair.chair_id):
            found_chair = True
            # print('removing chair: ' + other_chair.chair_id)
            chairs.remove(other_chair)

            # string = ''
            # for c in chairs:
            #     string += c.chair_id + ', '
            # print(string)

    if not found_chair:
        print('DIDNT FIND THE CHAIR, THIS IS BAD')
        quit()

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
        if preference.name == 'gender':
            if int(team.gender_total) > 4 or (int(team.gender_total) < 3):
                unmatched_preferences += ('[' + preference.name + ']'
                                          + '(' + str(team.gender_total) + ')')
    data_fields.append(unmatched_preferences)

    ret = TeamMember(team_fields, data_fields)

    # Add member to team_structure.
    # Used initially as back-bone for score-matching, may be unused in the future.
    this_team_id = ret.entry_data['TeamID']
    for team_structure in team_structures:
        if int(this_team_id) == team_structure.team_id:
            team_structure.add_member(student)

    return ret
