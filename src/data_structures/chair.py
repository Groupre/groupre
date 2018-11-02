class Chair:
    """A class dedicated to storing the attributes of a given Chair."""

    chair_id: int = None
    front: bool = False
    back: bool = False
    left: bool = False
    aisle: bool = False
    is_open: bool = True

    def __init__(self, chair_id, *preferences):
        self.chair_id = chair_id
        if "f" in preferences:
            self.front = True
        if "b" in preferences:
            self.back = True
        if "l" in preferences:
            self.left = True
        if "a" in preferences:
            self.aisle = True

    def __str__(self):
            return ("Chair ID: " + self.chair_id + " Front: " + str(self.front) + " Back: " + str(self.back) +
            " Left: " + str(self.left) + " Aisle: " + str(self.aisle))

    def __cmp__(self, other):
        if self.chair_id < other.chair_id:
            return -1
        elif self.chair_id > other.chair_id:
            return 1
        else:
            return 0
