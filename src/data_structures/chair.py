class Chair:
    """A class dedicated to storing the attributes of a given Chair."""

    chair_id: int = None
    front: bool = False
    back: bool = False
    fronti: bool = False
    backi : bool = False
    left: bool = False
    aisle: bool = False
    is_broken: bool = False
    
    left_section: bool = False
    middle_section: bool = False
    right_section: bool = False

    prefs = []
    taken :bool = False

    def __init__(self, chair_id, preferences):
        self.prefs = [0,0,0]
        self.chair_id = chair_id
        if "f" in preferences:
            self.front = True
            self.prefs[1] = 1.1
        if "b" in preferences:
            self.back = True
            self.prefs[1] = 8.1
        if "fi" in preferences:
            self.fronti = True
            self.prefs[1] = 1.0
        if "bi" in preferences:
            self.backi = True
            self.prefs[1] = 8.0
        if "la" in preferences:
            self.left = True
            self.prefs[2] = 1.1
        if "a" in preferences:
            self.aisle = True
            self.prefs[2] = 1.0
        if "br" in preferences:
            self.is_broken = True
        if "left" in preferences:
            self.left_section = True
            self.prefs[0] = 1.0
        if "middle" in preferences:
            self.middle_section = True
            self.prefs[0] = 0.9
        if "right" in preferences:
            self.right_section = True
            self.prefs[0] = 1.1
    def __str__(self):
            return ("Chair ID: " + self.chair_id + " Front: " + str(self.front) + " Back: " + str(self.back) +
            " Left: " + str(self.left) + " Aisle: " + str(self.aisle) + " Broken: " + str(self.is_broken))

    def __cmp__(self, other):
        if self.chair_id < other.chair_id:
            return -1
        elif self.chair_id > other.chair_id:
            return 1
        else:
            return 0
