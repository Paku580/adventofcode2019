from IntcodeComputer import Computer
from Utils.FileReader import FileReader

if __name__ == '__main__':
    intcode = FileReader.read_separated_values_as_int("input.txt", ',')
    # Part 1
    computer = Computer(intcode.copy(), [1])
    print(computer.run())
    # Part 2
    computer = Computer(intcode.copy(), [5])
    print(computer.run())
