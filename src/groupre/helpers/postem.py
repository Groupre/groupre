#!/usr/bin/env python

import argparse
import csv
import sys

DEFAULT_COLUMNS = ['PID', 'StudentName', 'CID', 'TeamID']


def process_csv(filename):
    """Returns a 2D array of the output csv."""
    matrix = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            matrix.append(row)
    return matrix


def postem(argv):
    """Formats a groupre output file for Sakai PostEm format."""
    #TODO clean up the amount of local vars, reduce number of lines
    output_csv = None
    teammates = None

    argparser = argparse.ArgumentParser()

    argparser.add_argument('-o', '--output', help='Output csv file')
    argparser.add_argument('-t', '--teammates', help='Enable teammate list', action='store_true')

    if 'postem.py' in argv[0]:
        parsed_args = argparser.parse_args()
    else:
        parsed_args = argparser.parse_args(argv)

    output_csv = parsed_args.output
    teammates = parsed_args.teammates

    if output_csv is None:
        print('Missing csv file.')
        return

    output = process_csv(output_csv)

    columns = output.pop(0)
    indeces = []
    notfound = []

    for column in DEFAULT_COLUMNS:
        if column in columns:
            indeces.append(columns.index(column))
        else:
            notfound.append(column)

    if len(notfound) > 0:
        for column in notfound:
            print('Output is missing the ' + column + ' field!')

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

    newname = output_csv.split('.csv')[0] + '-postEm.csv'
    with open(newname, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in final:
            writer.writerow(row)

if __name__ == '__main__':
    postem(sys.argv)
