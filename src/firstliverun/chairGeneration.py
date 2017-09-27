import csv

def justFirstLive(seat, seatnummax):
    team = seat[0]
    seatName = seat[1]
    if team == '':
        return "N/A"
    row = []
    row.append(seatName)
    row.append(team)
    seatRow = seatName[0].strip()
    seatNum = seatName.split(seatRow, 1)[1]
    if seatNum == '17' or seatNum == '19':
        if team != 8 or team != 83:
            row.append(1)
        else:
            row.append(0)
    else:
        row.append(0)
    if seatRow == 'A':
        row.append('Front')
    elif seatRow in ['B', 'C', 'D', 'E', 'F', 'G']:
        row.append('First 7')
    elif seatRow == 'O':
        row.append('Back')
    elif seatRow in ['H', 'J', 'K']:
        row.append('Middle')
    else:
        row.append('')
    if seatNum == '1' or seatNum == seatnummax:
        row.append('1')
    else:
        row.append('0')
    return row

def process_csv(filename):
    matrix = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            matrix.append(row)
    return matrix

chairs = process_csv(input("Path to Room CSV:\t"))
chairs_modified = []
chairs_modified.append(['CID', 'TeamID', 'Left-Handed', 'Position', 'Aisle'])

row_maximum = []
for chair in chairs:
    if chair[0] != 'Group Number':
        seatName = chair[1]
        seatRow = seatName[0].strip()
        seatNum = seatName.split(seatRow, 1)[1]
        if not row_maximum:
            row_maximum.append([seatRow, seatNum])
        if seatRow == row_maximum[-1][0]:
            if int(seatNum) > int(row_maximum[-1][1]):
                row_maximum.append([seatRow, seatNum])

for chair in chairs:
    if chair[0] != 'Group Number':
        seatRow = chair[1][0].strip()
        max = 0
        for row in row_maximum:
            if row[0] == seatRow:
                max = row[1]
                break
        row = justFirstLive(chair, max)
        if row != "N/A":
            chairs_modified.append(row)

with open('chairsFirst.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for c in chairs_modified:
        writer.writerow(c)