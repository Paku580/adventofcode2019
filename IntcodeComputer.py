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
    ARB = 9
    EXIT = 99


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class State(Enum):
    RUNNING = 1
    IDLE = 2
    TERMINATED = -1


class Computer:

    def __init__(self, intcode: list, inp=None):
        self.intcode = intcode
        self.intcode.extend([0] * (len(self.intcode) * 5000))
        if inp is None:
            inp = []
        self.inp = list(inp)
        self.instruction_pointer = 0
        self.state = State.IDLE
        self.output = []
        self.relative_base = 0

    def relative_param(self, index):
        mode = ParameterMode(((self.intcode[self.instruction_pointer] // (10 ** (index + 1))) % 10))
        if mode == ParameterMode.POSITION:
            return self.intcode[self.instruction_pointer + index]
        elif mode == ParameterMode.IMMEDIATE:
            return self.instruction_pointer + index
        elif mode == ParameterMode.RELATIVE:
            return self.intcode[self.instruction_pointer + index] + self.relative_base

    def param_value(self, index):
        return self.intcode[self.relative_param(index)]

    def store(self, index, value):
        self.intcode[self.relative_param(index)] = value

    def run(self):
        self.state = State.RUNNING
        while self.state != State.TERMINATED:
            self.execute_step()

    def run_until_output(self):
        self.state = State.RUNNING
        output_length = len(self.output)
        while (output_length == len(self.output)) and (self.state != State.TERMINATED):
            self.execute_step()

    def execute_step(self):

        opcode = Opcode(self.intcode[self.instruction_pointer] % 100)
        if opcode == Opcode.ADD:
            self.store(3, self.param_value(1) + self.param_value(2))
            self.instruction_pointer += 4
        elif opcode == Opcode.MULTIPLY:
            self.store(3, self.param_value(1) * self.param_value(2))
            self.instruction_pointer += 4
        elif opcode == Opcode.INPUT:
            self.store(1, self.inp.pop(0))
            self.instruction_pointer += 2
        elif opcode == Opcode.OUTPUT:
            self.output.append(self.param_value(1))
            self.instruction_pointer += 2
        elif opcode == Opcode.JIT:
            if self.param_value(1):
                self.instruction_pointer = self.param_value(2)
            else:
                self.instruction_pointer += 3
        elif opcode == Opcode.JIF:
            if not self.param_value(1):
                self.instruction_pointer = self.param_value(2)
            else:
                self.instruction_pointer += 3
        elif opcode == Opcode.LT:
            self.store(3, self.param_value(1) < self.param_value(2))
            self.instruction_pointer += 4
        elif opcode == Opcode.EQ:
            self.store(3, self.param_value(1) == self.param_value(2))
            self.instruction_pointer += 4
        elif opcode == Opcode.ARB:
            self.relative_base += self.param_value(1)
            self.instruction_pointer += 2
        elif opcode == Opcode.EXIT:
            self.state = State.TERMINATED
