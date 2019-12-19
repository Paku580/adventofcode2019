from Utils.FileReader import FileReader
from IntcodeComputer import Computer

if __name__ == '__main__':
    intcode = FileReader.read_separated_values_as_int("input.txt", ',')
    computer = Computer(intcode.copy())
    computer.run()
    print(computer.intcode[0])

    for i in range(100):
        for j in range(100):
            computer = Computer(intcode.copy())
            computer.intcode[1] = i
            computer.intcode[2] = j
            computer.run()
            if computer.intcode[0] == 19690720:
                print(100 * i + j)
                exit()
