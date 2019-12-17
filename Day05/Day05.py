from IntcodeComputer import run
from Utils.FileReader import FileReader

if __name__ == '__main__':
    intcode = FileReader.read_separated_values_as_int("input.txt", ',')
    run(list(intcode), [1])
    run(list(intcode), [5])
