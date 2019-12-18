from Utils.FileReader import FileReader
from IntcodeComputer import run

if __name__ == '__main__':
    intcode = FileReader.read_separated_values_as_int("input.txt", ',')
    temp_intcode = list(intcode)
    run(temp_intcode)
    print(temp_intcode[0])

    temp_intcode = list(intcode)

    for i in range(100):
        for j in range(100):
            temp_intcode = list(intcode)
            temp_intcode[1] = i
            temp_intcode[2] = j
            run(temp_intcode)
            if temp_intcode[0] == 19690720:
                print(100*i+j)
                exit()
