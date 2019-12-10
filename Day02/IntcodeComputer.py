from Utils.FileReader import FileReader


class IntcodeComputer:
    intcode = []
    intcode_pointer = 0

    def __init__(self, intcode):
        self.intcode = intcode

    def run_intcode(self):
        while True:
            self.switch_opcode(self.intcode[self.intcode_pointer])

    def add(self):
        self.intcode[self.intcode[self.intcode_pointer + 3]] = self.intcode[self.intcode[self.intcode_pointer + 1]] \
                                                 + self.intcode[self.intcode[self.intcode_pointer + 2]]
        self.increment_pointer()

    def multiply(self):
        self.intcode[self.intcode[self.intcode_pointer + 3]] = self.intcode[self.intcode[self.intcode_pointer + 1]] \
                                                 * self.intcode[self.intcode[self.intcode_pointer + 2]]
        self.increment_pointer()

    def finish(self):
        print(self.intcode[0])
        exit()

    def switch_opcode(self, opcode):
        opcode = int(opcode)
        switcher = {
            1: self.add,
            2: self.multiply,
            99: self.finish
        }
        func = switcher.get(opcode, lambda: print("Ooop unknown opcode"))
        func()

    def increment_pointer(self):
        self.intcode_pointer += 4


def main():
    intcode = FileReader.read_comma_separated_values_as_int("input.txt")
    intcode_computer = IntcodeComputer(intcode)
    intcode_computer.run_intcode()


if __name__ == '__main__':
    main()
