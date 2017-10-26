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
