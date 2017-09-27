import csv

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
            row.append(int(c[0]))
    return teams


chairs = []
with open('chairs.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    row = []
    for row in reader:
        chairs.append(row)
students = []
with open('test1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        students.append(row)
teams = create_teams(chairs)

with open('teams.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for t in teams:
        writer.writerow(t)
