from Utils.FileReader import FileReader
from Day02.IntcodeComputer import IntcodeComputer


def main():
    intcode = FileReader.read_separated_values_as_int("input.txt", ',')

    for i in range(100):
        intcode[1] = i
        for j in range(100):
            intcode[2] = j
            intcode_computer = IntcodeComputer(intcode.copy())
            intcode_computer.run_intcode()
            if intcode_computer.intcode[0] == 19690720:
                print("i: " + str(i) + ", j: " + str(j))
                exit()


if __name__ == '__main__':
    main()
