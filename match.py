import time
import csv
import sys
from sqlite3 import connect
from TeamNamer import *
from Dee import *

def preference_match(students, chairs, teams):
    for student in students:
        for team in teams:
            seated = scoring_match(student, team)
            if seated != "Not a good fit" or seated[1] != "Not a good fit":
                del teams[index_intable(teams, seated[0])]
                teams.append(seated[0])
                del chairs[index_intable(chairs, seated[1])]
                del students[index_intable(students, student)]
    return [students, chairs, teams]

def random_match():
    return 0

def scoring_match(student, team):
    chair = "Not a good fit"
    if team[4] == 0:
        team[4] = student
        chair = team[1]
    else:
        i = 4
        for classmate in team[4:-1]:
            i += 1
            if classmate == 0:
                break
            if classmate[4] != student[4]:
                team[i] = student
                chair = team[i-4]
        if i >= len(team):
            return chair
            #TODO make teams not just carry CIDs and check number of chairs that meet prefs
            # score_diff = abs(student_score - classmate)
            # if score_diff == 3:
            #     last_slot = find_emptyslot(team)
            #     if last_slot != "N/A":
            #         team[last_slot] = student
    return [team, chair]

def find_emptyslot(array):
    i = 0
    for slot in array:
        if slot == 0:
            return i
        i+=1
    return "N/A"

#TODO currently no error checking
def index_intable(table, id, column = None):
    i = 0
    if column is None:
        for row in table:
            if row[0] == id[0]:
                return i
            i+=1

    else:
        for row in table:
            i+=1
            if row[column] == id[column]:
                return i


#TODO fix this ramshackle thing
def create_subset(table, category, column=None):
    subset = []
    if column == None:
        for row in table:
            if row[-1] == category:
                subset.append(row)
                table.remove(row)
    else:
        for row in table:
            if row[column] == category:
                subset.append(row)
                table.remove(row)
    return [subset, table]

def create_teams(chairs):
    teams = []
    teams.append(["TeamID", "Chair1", "Chair2", "Chair3", "Chair4", "Student1", "Student2", "Student3", "Student4"])
    row = []
    i = 1
    for c in chairs:
        if c[1] != "TeamID":
            if int(c[1]) > i:
                row.extend([0,0,0,0])
                teams.append(row.copy())
                i+=1
                row.clear()
            if len(row) == 0:
                row.append(i)
            row.append(c)
    return teams[1:-1]

#function converts values in 2d array into ints if applicable
#TODO this function convers all numbers into ints, even floats. Insert error handling for this
def twod_intconver(twod):
    twod_converted = []
    for row in twod:
        row_c = []
        for cell in row:
            try:
                cell_c = int(cell)
                row_c.append(cell_c)
            except ValueError:
                row_c.append(cell)
                pass
        twod_converted.append(row_c.copy())
        row_c.clear()
    return twod_converted


#TODO: potentially extend this function to transfer from CSV to DB
def get_csv(filename):
    twodimensional = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            twodimensional.append(row)
    return twod_intconver(twodimensional[1:-1])

#TODO replace hardcoding with sys.argv
roster = get_csv("CSVScripts/test1.csv")
classroom = get_csv("CSVScripts/chairs.csv")
teams = create_teams(classroom)

roster = create_subset(roster, "No Priority")
roster_pref = roster[1]
roster_remaining = roster[0]

classroom_remaining = create_subset(classroom, 1, 2)
classroom_left = classroom_remaining[0]
#TODO preference match in between all of these

classroom_remaining = create_subset(classroom_remaining[1], "Front", 3)
classroom_front = classroom_remaining[0]

classroom_remaining = create_subset(classroom_remaining[1], "Back", 3)
classroom_back = classroom_remaining[0]

classroom_remaining = create_subset(classroom_remaining[1], 1, 4)
classroom_aisle = classroom_remaining[0]

#TODO subdivide roster_pref as well
preferenced = preference_match(roster_pref, classroom, teams)
roster_remaining.extend(preferenced[0])
classroom.extend(preferenced[preferenced[1]])
teams = preferenced[2]

