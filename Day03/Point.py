class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.step_count = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def manhattan_distance(self, other_point):
        return abs(self.x - other_point.x) + abs(self.y - other_point.y)

    def __str__(self):
        return f"Point{{X: {self.x}, Y: {self.y}, step_count: {self.step_count}}}"

    def __repr__(self):
        return self.__str__()

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__key() == other.__key()
        return NotImplemented
