from Utils.FileReader import FileReader
from Day05.IntcodeComputerV2 import IntcodeComputer


def main():
    intcode = FileReader.read_separated_values_as_int("input.txt", ',')
    intcode_computer = IntcodeComputer(intcode)
    intcode_computer.run_intcode()


if __name__ == '__main__':
    main()
