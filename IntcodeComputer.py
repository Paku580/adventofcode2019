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
        self.output = []

    def param_value(self, index):
        mode = ParameterMode(((self.intcode[self.instruction_pointer] // (10 ** (index + 1))) % 10))
        if mode == ParameterMode.POSITION:
            return self.intcode[self.intcode[self.instruction_pointer + index]]
        elif mode == ParameterMode.IMMEDIATE:
            return self.intcode[self.instruction_pointer + index]

    def store(self, offset, value):
        self.intcode[self.intcode[self.instruction_pointer + offset]] = value

    def run(self) -> list:
        self.state = State.RUNNING
        while self.state != State.TERMINATED:
            self.execute_step()
        return self.output

    def run_until_output(self) -> int:
        self.state = State.RUNNING
        output_length = len(self.output)
        while (output_length == len(self.output)) and (self.state != State.TERMINATED):
            output = self.execute_step()
        return output

    def execute_step(self) -> int:

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
            value = self.param_value(1)
            self.output.append(value)
            self.instruction_pointer += 2
            return value
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
        elif opcode == Opcode.EXIT:
            self.state = State.TERMINATED
