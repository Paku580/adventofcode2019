from Utils.FileReader import FileReader

total_fuel_requirement = 0


def calc_total_fuel_requirement(part2):
    masses = FileReader.read_line_by_line_as_int("input.txt")
    for mass in masses:
        calc_fuel_requirement(mass, part2)


def calc_fuel_requirement(mass, part2):
    global total_fuel_requirement
    mass = int(mass / 3 - 2)
    if mass > 0:
        total_fuel_requirement += mass
        if part2:
            calc_fuel_requirement(mass, part2)


def main():
    # Day 1 Part 1
    part2 = False
    calc_total_fuel_requirement(part2)
    print(total_fuel_requirement)

    # Day 1 Part 2
    part2 = True
    calc_total_fuel_requirement(part2)
    print(total_fuel_requirement)


if __name__ == '__main__':
    main()
