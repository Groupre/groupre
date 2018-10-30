class Chair:
    """A class dedicated to storing the attributes of a given Chair."""

    chair_id = None
    front = False
    back = False
    left = False
    aisle = False
    def __init__(self, chair_id, *preferences):
        self.chair_id = chair_id
        self.front = preferences[0]
        self.back = preferences[1]
        self.left = preferences[2]
        self.aisle = preferences[3]
