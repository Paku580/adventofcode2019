import itertools


class IntcodeComputer:
    intcode = []
    instruction_pointer = 0

    def __init__(self, intcode):
        self.intcode = intcode
        self.running = False
        self.input = 1

    def run_intcode(self):
        self.running = True
        while self.running:
            self.switch_opcode(self.intcode[self.instruction_pointer])

    def add(self, addend1, addend2):
        self.intcode[self.intcode[self.instruction_pointer + 3]] = addend1 + addend2
        self.increment_pointer(4)

    def multiply(self, multiplicand, multiplier):
        self.intcode[self.intcode[self.instruction_pointer + 3]] = multiplicand * multiplier
        self.increment_pointer(4)

    def store_value(self, address):
        self.intcode[address] = self.input
        self.increment_pointer(2)

    def output_value(self, value):
        print(value)
        self.increment_pointer(2)

    def finish(self):
        print("finish")
        self.running = False

    def switch_opcode(self, opcode):
        switcher = {
            1: self.add,
            2: self.multiply,
            3: self.store_value,
            4: self.output_value,
            99: self.finish
        }
        opcode = f"{opcode:05d}"
        args = self.get_parameter_values(opcode)
        func = switcher.get(int(opcode[-2:]), lambda: print("Ooops unknown opcode"))
        func(*args)

    def get_parameter_values(self, opcode):
        instruction = int(opcode[-2:])
        modes = [int(mode) for mode in opcode[:-2]]
        params = []

        if instruction < 3:
            for index, mode in enumerate(itertools.islice(reversed(modes), 0, len(modes) - 1)):
                if mode == 0:
                    params.append(self.intcode[self.intcode[self.instruction_pointer + index + 1]])
                else:
                    params.append(self.intcode[self.instruction_pointer + index + 1])
        elif instruction == 3:
            params.append(self.intcode[self.instruction_pointer + 1])
        elif instruction == 99:
            return params
        else:
            if int(opcode[-3]) == 0:
                params.append(self.intcode[self.intcode[self.instruction_pointer + 1]])
            else:
                params.append(self.intcode[self.instruction_pointer + 1])
        return params

    def increment_pointer(self, value):
        self.instruction_pointer += value
