class Student:
    '''A class dedicated to storing the preferences and specificness level of a given Student.'''

    student_id: int = None
    isVIP: bool = False
    prefersFront = False
    prefersBack = False
    prefersLeft = False
    prefersAisle = False

    def __init__(self, student_id, score, is_vip, *preferences):
        self.student_id = student_id
        if is_vip == "True":
            self.isVIP = True
        else:
            self.isVIP = False
        if "f" in preferences:
            self.prefersFront = True
        if "b" in preferences:
            self.prefersBack = True
        if "l" in preferences:
            self.prefersLeft= True
        if "a" in preferences:
            self.prefersAisle = True

    def __str__(self):
        return ("Student ID: " + self.student_id + " VIP: " + str(self.isVIP) +" Front: " + str(self.prefersFront) +
        " Back: " + str(self.prefersBack) + " Left: " + str(self.prefersLeft) + " Aisle: " + str(self.prefersAisle) )
