from Utils.FileReader import FileReader
from IntcodeComputer import Computer

if __name__ == '__main__':
    intcode = FileReader.read_separated_values_as_int('input.txt', ',')
    # Part 1
    computer = Computer(intcode.copy(), [1])
    computer.run()
    print(computer.output)
    # Part 2
    computer = Computer(intcode.copy(), [2])
    computer.run()
    print(computer.output)
