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
    num_points : int = 0
    taken :bool = False

    def __init__(self, chair_id, preferences):
        self.chair_id = chair_id
        if "front" in preferences:
            self.front = True
            self.num_points += 1
        if "back" in preferences:
            self.back = True
            self.num_points += 3
        if "fronti" in preferences:
            self.fronti = True
            self.num_points += 5
        if "backi" in preferences:
            self.backi = True
            self.num_points += 7
        if "left" in preferences:
            self.left = True
            self.num_points += 40
        if "aisle" in preferences:
            self.aisle = True
            self.num_points += 30
        if "broken" in preferences:
            self.is_broken = True

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
