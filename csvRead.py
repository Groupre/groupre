import numbers
import sys
import csv

totalSeats = int(input("Cheers! How many seats are we working with today?"))

print ("Ok, I've got",totalSeats,"total seats.")

for num in range (totalSeats):

    with open('testcsv.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        names = []
        seats = []
        for row in readCSV:
            seat = row[1]
            name = row[0]

            names.append(name)
            seats.append(seat)

        print(names)
        print(seats)

        whichSeat = input('Which seat would you like to know the occupant of?')
        masterIndex = seats.index(whichSeat)
        occupant = names[masterIndex]
        print('The occupant of',whichSeat,'is:',occupant)
