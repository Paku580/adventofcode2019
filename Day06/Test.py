from Utils.FileReader import FileReader
from itertools import chain

orbit_you = "S2C"
orbit_san = "QKC"
count = 0
steps = []


def count_orbits(orbit_map, key):
    global count

    if key in orbit_map.keys():
        for v in orbit_map[key]:
            count += 1
            count_orbits(orbit_map, v)


def steps_to_santa(orbit_map):
    get_key_by_value(orbit_map)


def get_key_by_value(orbit_map):
    for k, v in orbit_map.items():
        if v == orbit_you:
            print(k)


if __name__ == '__main__':
    map_data = FileReader.read_line_by_line("input.txt")
    orbit_map = {}
    for item in map_data:
        data = item.split(')')
        if data[0] not in orbit_map.keys():
            orbit_map[data[0]] = [data[1]]
        else:
            orbit_map[data[0]].append(data[1])

    for k in orbit_map.keys():
        count_orbits(orbit_map, k)
    print(count)
    steps_to_santa(orbit_map)
