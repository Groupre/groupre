class Student:
    '''A class dedicated to storing the preferences and specificness level of a given Student.'''

    student_id: int = None
    is_VIP: bool = False
    has_pref: bool = False
    pref_front: bool = False
    pref_back: bool = False
    pref_left: bool = False
    pref_aisle: bool = False
    num_points: int = 0
    taken :bool = False


    def __init__(self, student_id, is_vip, preferences):
        self.student_id = student_id
        if is_vip == "True":
            self.is_VIP = True
            self.num_points += 100
        else:
            self.is_VIP = False
        if "f" in preferences:
            self.pref_front = True
            self.has_pref = True
            self.num_points += 1
        if "b" in preferences:
            self.pref_back = True
            self.has_pref = True
            self.num_points += 30
        if "l" in preferences:
            self.pref_left = True
            self.has_pref = True
            self.num_points += 20
        if "a" in preferences:
            self.pref_aisle = True
            self.has_pref = True
            self.num_points += 40
    def __str__(self):
        return ("Student ID: " + self.student_id + " VIP: " + str(self.is_VIP) + " Front: " + str(self.pref_front) +
                " Back: " + str(self.pref_back) + " Left: " + str(self.pref_left) + " Aisle: " + str(self.pref_aisle))
