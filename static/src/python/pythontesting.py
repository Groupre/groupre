#!/usr/bin/env

import platform
import csv

print(platform.python_version())

try:
    with open('test.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, 10):
            writer.writerow([i, i+1])
except TypeError:
    print('Error')