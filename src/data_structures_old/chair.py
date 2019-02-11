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
    
    has_section: bool = False
    left_section: bool = False
    middle_section: bool = False
    right_section: bool = False

    num_points : int = 0
    taken :bool = False

    def __init__(self, chair_id, preferences):
        self.chair_id = chair_id
        if "f" in preferences:
            self.front = True
            self.num_points += 1
        if "b" in preferences:
            self.back = True
            self.num_points += 3
        if "fi" in preferences:
            self.fronti = True
            self.num_points += 5
        if "bi" in preferences:
            self.backi = True
            self.num_points += 7
        if "l" in preferences:
            self.left = True
            self.num_points += 40
        if "a" in preferences:
            self.aisle = True
            self.num_points += 30
        if "br" in preferences:
            self.is_broken = True
        if "left" in preferences:
            self.left_section = True
            self.has_section = True
            self.num_points += 100
        if "middle" in preferences:
            self.middle_section = True
            self.has_section = True
            self.num_points += 200
        if "right" in preferences:
            self.right_section = True
            self.has_section = True
            self.num_points += 300

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
