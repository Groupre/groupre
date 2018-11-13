class Student:
    '''A class dedicated to storing the preferences and specificness level of a given Student.'''

    student_id: int = None
    is_VIP: bool = False
    has_pref: bool = False

    pref_front: bool = False
    pref_back: bool = False
    pref_left: bool = False
    pref_aisle: bool = False

    def __init__(self, student_id, score, is_vip, *preferences):
        self.student_id = student_id
        if is_vip == "True":
            self.is_VIP = True
        else:
            self.is_VIP = False
        if "f" in preferences:
            self.pref_front = True
            self.has_pref = True
        if "b" in preferences:
            self.pref_back = True
            self.has_pref = True
        if "l" in preferences:
            self.pref_left = True
            self.has_pref = True
        if "a" in preferences:
            self.pref_aisle = True
            self.has_pref = True

    def __str__(self):
        return ("Student ID: " + self.student_id + " VIP: " + str(self.is_VIP) +" Front: " + str(self.pref_front) +
        " Back: " + str(self.pref_back) + " Left: " + str(self.pref_left) + " Aisle: " + str(self.pref_aisle) )
