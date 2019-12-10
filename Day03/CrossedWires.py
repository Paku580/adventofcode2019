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


def direction_switcher(direction):
    switcher = {
        'R': move_right,
        'L': move_left,
        'U': move_up,
        'D': move_down
    }
    return switcher.get(direction, lambda: print("ayayay"))


def start():
    wires = FileReader.read_line_by_line("input.txt")
    points = []

    for wire in wires:
        point = Point()
        directions = wire.split(',')
        temp_points = []
        step_count = 0
        for direction in directions:
            func = direction_switcher(direction[0])
            direction_length = int(direction[1:])
            for i in range(direction_length):
                point = Point(point.x, point.y)
                func(point)
                step_count += 1
                point.step_count = step_count
                temp_points.append(point)
        points.append(temp_points)

    common_points = list(set(points[0]).intersection(points[1]))

    for i in range(len(common_points)):
        first_index = points[0].index(common_points[i])
        second_index = points[1].index(common_points[i])

        common_points[i].step_count = points[0][first_index].step_count + points[1][second_index].step_count

    minimum = min(common_points, key=lambda p: p.step_count)

    closest_intersection = common_points[0].manhattan_distance(Point())

    for point in common_points:
        intersection = point.manhattan_distance(Point())
        if intersection <= closest_intersection:
            closest_intersection = intersection

    # Part 1
    print(closest_intersection)
    # Part 2
    print(minimum.step_count)
