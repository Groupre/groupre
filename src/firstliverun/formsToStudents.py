import csv
import random
import sys

POSITIONS = ["I want to sit in the front row", "I want to sit in the first 7 rows", "I want to sit in the back rows", "I need a left handed desk"]

def find_preference(row, roster):
    new_row = []
    #new_row.append(random.randrange(100000001, 999999999))
    if '@' in row[2]:
        name = row[2].split('@', 1)
        if name[1].strip() != "live.unc.edu" or name[1].strip() != "unc.edu":
            name = roster_find(row, roster)
            if name == "N/A":
                name = "Please find my onyen. " + row[2]
        else:
            name = name[0]
        row[2] = name
    if is_number(row[2]):
        row[2] = roster_find(row, roster)
    new_row.append(row[2].lower())
    new_row.append(row[1].strip() + ' ' + row[0].strip())
    new_row.append(0)
    #new_row.append(random.randrange(1, 4, 1))
    choice = row[3]
    if choice == POSITIONS[3]:
        new_row.append('TRUE')
        new_row.append('N/A')
    else:
        new_row.append('FALSE')
        if choice == POSITIONS[0]:
            new_row.append('Front')
        elif choice == POSITIONS[1]:
            new_row.append('First 7')
        elif choice == POSITIONS[2]:
            new_row.append('Back')
        elif choice == 'Middle':
            new_row.append('Middle')
        else:
            new_row.append('')
    if choice == 'Aisle':
        new_row.append('TRUE')
    else:
        new_row.append('FALSE')
    return new_row

def no_preference(row):
    new_row = []
    new_row.append(row[0])
    st_first = row[1].split(',', 1)
    st_last = st_first[0].strip()
    st_first = st_first[1].strip()
    new_row.append(st_first + ' ' + st_last)
    new_row.append(0)
    new_row.append(0)
    new_row.append('')
    new_row.append(0)
    return new_row

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def roster_find(row, roster):
    last = row[0].strip()
    first = row[1].strip()
    for student in roster:
        if student[0] != 'Student ID':
            st_first = student[1].split(',', 1)
            st_last = st_first[0].strip()
            st_first = st_first[1].strip()
            if last == st_last:
                if first == st_first:
                    return student[0]
    return "N/A"

def process_csv(filename):
    matrix = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            matrix.append(row)
    return matrix

roster = process_csv(input("Roster path:"))
requests = process_csv(input("Request path:"))

processed = []
final = []
processed.append(['PID', 'StudentName', 'Score', 'Left-Handed', 'Position', 'Aisle'])
for r in requests:
    new_row = find_preference(r, roster)
    processed.append(new_row)

processed_copy = processed.copy()
processed = []
for i in processed_copy:
  if i not in processed:
      processed.append(i)

students_nopref = []
for r in roster:
    if r[0] != 'Student ID':
        flag = True
        for student in processed:
            if r[0] == student[0]:
                flag = False
                break
        if flag:
            students_nopref.append(r)

for r in students_nopref:
    processed.append(no_preference(r))


# for r in requests:
#     for student in roster:
#         if r[0] == student[0]:
#             final.append(r)

with open('studentsFirst.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for f in processed:
        writer.writerow(f)