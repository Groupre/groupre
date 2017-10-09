import csv

with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, 10):
        writer.writerow([i, i+1])