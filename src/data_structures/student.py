class Student:
    '''A class dedicated to storing the preferences and specificness level of a given Student.'''

    student_id: int = None
    is_VIP: bool = False
    has_pref: bool = False
    pref_front: bool = False
    pref_back: bool = False
    pref_fronti: bool = False
    pref_backi: bool = False
    pref_left: bool = False
    pref_aisle: bool = False

    left_section: bool = False
    middle_section: bool = False
    right_section: bool = False

    prefs = []
    numPref = 0
    taken :bool = False


    def __init__(self, student_id, is_vip, preferences):
        self.prefs = [0,0,0]
        self.student_id = student_id
        self.numPref = 0
        if is_vip == "TRUE":
            self.is_VIP = True
        else:
            self.is_VIP = False
        if "f" in preferences:
            self.front = True
            self.prefs[1] = 0.7
            self.numPref += 1

        if "b" in preferences:
            self.back = True
            self.prefs[1] = 2.7
            self.numPref += 1

        if "fi" in preferences:
            self.fronti = True
            self.prefs[1] = 0.5
            self.numPref += 1

        if "bi" in preferences:
            self.backi = True
            self.prefs[1] = 2.5
            self.numPref += 1

        if "la" in preferences:
            self.left = True
            self.prefs[2] = 1.1
            self.numPref += 1

        if "a" in preferences:
            self.aisle = True
            self.prefs[2] = 1.0
            self.numPref += 1

        if "left" in preferences:
            self.left_section = True
            self.prefs[0] = 13
            self.numPref += 1

        if "middle" in preferences:
            self.middle_section = True
            self.prefs[0] = 9
            self.numPref += 1

        if "right" in preferences:
            self.right_section = True
            self.prefs[0] = 17
            self.numPref += 1

    
    def __str__(self):
        return ("Student ID: " + self.student_id + " VIP: " + str(self.is_VIP) + " Front: " + str(self.pref_front) +
                " Back: " + str(self.pref_back) + " Left: " + str(self.pref_left) + " Aisle: " + str(self.pref_aisle))
