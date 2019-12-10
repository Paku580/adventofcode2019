from Utils.FileReader import FileReader
from Day03.Point import Point


def move_right(point):
    point.move(1, 0)


def move_left(point):
    point.move(-1, 0)


def move_up(point):
    point.move(0, 1)


def move_down(point):
    point.move(0, -1)


def start():
    wires = FileReader.read_line_by_line("input.txt")
    points = []
    switcher = {
        'R': move_right,
        'L': move_left,
        'U': move_up,
        'D': move_down
    }

    for wire in wires:
        point = Point(0, 0)
        directions = wire.split(',')
        temp_points = []
        for direction in directions:
            func = switcher.get(direction[0], lambda: print("ayayay"))
            direction_length = int(direction[1:])
            for i in range(direction_length):
                point = Point(point.x, point.y)
                func(point)
                temp_points.append(point)
        points.append(temp_points)

    common_points = list(set(points[0]).intersection(points[1]))
    print(common_points)

    closest_intersection = common_points[0].manhattan_distance(Point(0, 0))

    for point in common_points:
        intersection = point.manhattan_distance(Point(0, 0))
        if intersection <= closest_intersection:
            closest_intersection = intersection

    print(closest_intersection)
