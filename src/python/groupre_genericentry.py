'''This module contains the GenericEntry class used by groupre.'''

import groupre_globals


class GenericEntry:
    '''An object to store data pertaining to input in the context of input.csv.'''

    entry_data = {}

    def __init__(self, fieldList=None, dataList=None):
        # Argument error processing.
        if fieldList is None:
            raise ValueError('fieldList was null')
        if dataList is None:
            raise ValueError('dataList was null')
        if len(fieldList) != len(dataList):
            raise ValueError(
                'fieldList and dataList do not have the same length')

        # Populate this input's data with the generic input data.
        data = {}
        i = 0
        while i != len(fieldList):
            if (fieldList[i] in groupre_globals.STUDENT_REQUIRED_FIELDS
                    or fieldList[i] in groupre_globals.CHAIR_REQUIRED_FIELDS):
                data[fieldList[i]] = dataList[i]
            elif dataList[i] in groupre_globals.TRUE_VALUES:
                data[fieldList[i]] = True
            elif dataList[i] in groupre_globals.FALSE_VALUES:
                data[fieldList[i]] = False
            else:
                data[fieldList[i]] = dataList[i]

            i += 1

        self.entry_data = data
