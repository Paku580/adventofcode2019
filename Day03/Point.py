class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def manhattan_distance(self, other_point):
        return abs(self.x - other_point.x) + abs(self.y - other_point.y)

    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return self.__str__()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__key() == other.__key()
        return NotImplemented
