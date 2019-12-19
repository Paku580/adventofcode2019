from Utils.FileReader import FileReader


def count_orbits(orbit_map):
    def orbiters(omap, x):
        return {i[0] for i in omap.items() if i[1] == x}

    count = 0
    visit = [('COM', 1)]
    while len(visit):
        o, depth = visit.pop()
        l = list(orbiters(orbit_map, o))
        count += len(l) * depth
        visit += [(x, depth + 1) for x in l]
    return count


def steps_to_santa(orbit_map):
    def route_to_com(start):
        route = [start]
        while route[-1] != 'COM':
            route.append(orbit_map[route[-1]])
        print(route)
        return route

    you_to_com = route_to_com('YOU')
    san_to_com = route_to_com('SAN')
    for i, x in enumerate(you_to_com):
        if x in san_to_com:
            return san_to_com.index(x) + i - 2


if __name__ == '__main__':
    map_data = FileReader.read_line_by_line("input.txt")
    orbit_map = {}
    for item in map_data:
        data = item.split(')')
        orbit_map[data[1]] = data[0]
    # Part 1
    print(count_orbits(orbit_map))
    # Part 2
    print(steps_to_santa(orbit_map))
