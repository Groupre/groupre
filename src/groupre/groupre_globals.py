'''This module contains the program-wide variables and constants used by groupre.'''

STUDENT_REQUIRED_FIELDS = ['PID', 'StudentName', 'VIP', 'Score']
CHAIR_REQUIRED_FIELDS = ['CID', 'TeamID']
DEBUG_FIELDS = ['PriorityScore']

TRUE_VALUES = ['1', 'true', 'True', 'TRUE', True]
FALSE_VALUES = ['FALSE', 'false', 'False', '0', False]
NULL_VALUES = ['N/A', 'n/a', '', 'FALSE',
               'false', 'False', '0', 'null', 'NULL', False]

STUDENT_PRIORITY_VALUE = 0
STUDENT_PRIORITY_TOTAL = 0

FALLBACK_ENABLED = False
FALLBACK_LIMIT_FRONT = 2
FALLBACK_LIMIT_BACK = 2
FALLBACK_LIMIT_AISLE = 2
FALLBACK_CHAIRS_FRONT = []
FALLBACK_CHAIRS_BACK = []
FALLBACK_CHAIRS_AISLE = []


def set_all_fallback_limits(limit):
    '''Sets all FALLBACK\_LIMIT_* global variables to the same setting.
    Typically this won't be used since the amount of chairs with the same
    number of fallback options for every attribute will not be the same.'''
    global FALLBACK_LIMIT_FRONT
    global FALLBACK_LIMIT_BACK
    global FALLBACK_LIMIT_AISLE

    FALLBACK_LIMIT_FRONT = limit
    FALLBACK_LIMIT_BACK = limit
    FALLBACK_LIMIT_AISLE = limit


def set_all_fallback_limits_to_max():
    '''Sets all FALLBACK\_LIMIT_* global variables to their maximum possible value.'''
    global FALLBACK_CHAIRS_FRONT
    global FALLBACK_CHAIRS_BACK
    global FALLBACK_CHAIRS_AISLE
    global FALLBACK_LIMIT_FRONT
    global FALLBACK_LIMIT_BACK
    global FALLBACK_LIMIT_AISLE

    FALLBACK_LIMIT_FRONT = len(FALLBACK_CHAIRS_FRONT)
    FALLBACK_LIMIT_BACK = len(FALLBACK_CHAIRS_BACK)
    FALLBACK_LIMIT_AISLE = len(FALLBACK_CHAIRS_AISLE)
