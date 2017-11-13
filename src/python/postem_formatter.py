import argparse
import csv
import os
import sys

DEFAULT_COLUMNS = ['PID', 'StudentName', 'CID', 'TeamID']

def process_csv(filename):
    matrix = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            matrix.append(row)
    return matrix


def main(argv):

    argparser = argparse.ArgumentParser()
    #
    # output_csv = None
    # teammates = None

    argparser.add_argument('-o', '--output', help='Output csv file')
    argparser.add_argument('-t', '--teammates', help='Enable teammate list', action='store_true')

    parsed_args = argparser.parse_args()

    output_csv = parsed_args.output
    teammates = parsed_args.teammates

    output = process_csv(output_csv)

    columns = output.pop(0)
    indeces = []
    notfound =[]
    for C in DEFAULT_COLUMNS:
        if C in columns:
            indeces.append(columns.index(C))
        else:
            notfound.append(C)

    if len(notfound) > 0:
        for C in notfound:
            print('Output is missing the ' + C + ' field!')

    final = []
    if teammates:
        DEFAULT_COLUMNS.append('Teammates')
    final.append(DEFAULT_COLUMNS)

    curr_team = 0
    i = 0
    teams = []
    for row in output:
        newrow = []
        for index in indeces:
            newrow.append(row[index])
        if teammates:
            teamid = int(newrow[DEFAULT_COLUMNS.index('TeamID')])
            mates = []
            if teamid > curr_team:
                curr_team = teamid
                mates.append(teamid)
                for index in range(i, len(output)):
                    student = output[index]
                    if teamid == int(student[columns.index('TeamID')]):
                        mates.append(student[columns.index('StudentName')])
                    else:
                        break
                teams.append(mates)
            else:
                for t in teams:
                    if t[0] == teamid:
                        mates = t
            if len(mates) > 0:
                mates.pop(0)
                mates.remove(newrow[DEFAULT_COLUMNS.index('StudentName')])
            mates = ', '.join(mates)
            newrow.append(mates)
        final.append(newrow)
        i += 1
    newname = os.path.join(os.path.dirname(output_csv), output_csv.split('.')[-2] + 'postEm.csv')
    with open(newname, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for f in final:
            writer.writerow(f)

if __name__ == '__main__':
    main(sys.argv)