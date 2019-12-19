from enum import Enum


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JIT = 5
    JIF = 6
    LT = 7
    EQ = 8
    EXIT = 99


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class State(Enum):
    RUNNING = 1
    IDLE = 2
    TERMINATED = -1


class Computer:

    def __init__(self, intcode, inp=None):
        self.intcode = intcode
        if inp is None:
            inp = []
        self.inp = list(inp)
        self.instruction_pointer = 0
        self.state = State.IDLE

    def run(self) -> list:
        self.state = State.RUNNING

        def param_value(index):
            mode = ParameterMode(((self.intcode[self.instruction_pointer] // (10 ** (index + 1))) % 10))
            if mode == ParameterMode.POSITION:
                test = self.intcode[self.instruction_pointer + index]
                test2 = self.intcode[test]
                return test2
            elif mode == ParameterMode.IMMEDIATE:
                return self.intcode[self.instruction_pointer + index]

        def store(offset, value):
            self.intcode[self.intcode[self.instruction_pointer + offset]] = value

        output = []

        while True:
            opcode = Opcode(self.intcode[self.instruction_pointer] % 100)
            if opcode == Opcode.ADD:
                store(3, param_value(1) + param_value(2))
                self.instruction_pointer += 4
            elif opcode == Opcode.MULTIPLY:
                store(3, param_value(1) * param_value(2))
                self.instruction_pointer += 4
            elif opcode == Opcode.INPUT:
                print(self.inp)
                store(1, self.inp.pop(0))
                self.instruction_pointer += 2
            elif opcode == Opcode.OUTPUT:
                output.append(param_value(1))
                self.instruction_pointer += 2
            elif opcode == Opcode.JIT:
                if param_value(1):
                    self.instruction_pointer = param_value(2)
                else:
                    self.instruction_pointer += 3
            elif opcode == Opcode.JIF:
                if not param_value(1):
                    self.instruction_pointer = param_value(2)
                else:
                    self.instruction_pointer += 3
            elif opcode == Opcode.LT:
                store(3, param_value(1) < param_value(2))
                self.instruction_pointer += 4
            elif opcode == Opcode.EQ:
                store(3, param_value(1) == param_value(2))
                self.instruction_pointer += 4
            elif opcode == Opcode.EXIT:
                self.state = State.TERMINATED
                return output
