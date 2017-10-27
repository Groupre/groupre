#!/usr/bin/env python
'''This module is used to test groupre.'''

import sys
sys.path.insert(0, sys.path[0].replace('python', 'groupre'))
print(sys.path)

import groupre

if __name__ == '__main__':
    ARGS = ['-f',
            '-s', '../../test/testFiles/fallback/students_fallback.csv',
            '-c', '../../test/testFiles/fallback/chairs_fallback.csv',
            '-o', '../../test/testFiles/fallback/test_output.csv']
    groupre.main(ARGS)
