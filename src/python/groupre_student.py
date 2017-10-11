'''This module contains the Student class used by groupre.'''

import groupre_genericentry
import groupre_globals


class Student(groupre_genericentry.GenericEntry):
    '''A GenericEntry with an extra specificness value for student-to-chair matching purposes.'''

    specificness = 0

    def __init__(self, fieldList=None, dataList=None):
        groupre_genericentry.GenericEntry.__init__(self, fieldList, dataList)

        for field in self.entry_data:
            if field not in groupre_globals.STUDENT_REQUIRED_FIELDS:
                if str(self.entry_data[field]) not in groupre_globals.NULL_VALUES:
                    self.specificness += 1
