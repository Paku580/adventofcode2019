from enum import Enum


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    STORE = 3
    OUTPUT = 4
    JIT = 5
    JIF = 6
    LT = 7
    EQ = 8
    EXIT = 99


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


def run(intcode, inp=None):
    instruction_pointer = 0
    inp = list(inp)

    def param_value(index):
        mode = ParameterMode(((intcode[instruction_pointer] // (10 ** (index + 1))) % 10))
        if mode == ParameterMode.POSITION:
            test = intcode[instruction_pointer + index]
            test2 = intcode[test]
            return test2
        elif mode == ParameterMode.IMMEDIATE:
            return intcode[instruction_pointer + index]

    def store(offset, value):
        intcode[intcode[instruction_pointer + offset]] = value

    while True:
        opcode = Opcode(intcode[instruction_pointer] % 100)
        if opcode == Opcode.ADD:
            store(3, param_value(1) + param_value(2))
            instruction_pointer += 4
        elif opcode == Opcode.MULTIPLY:
            store(3, param_value(1) * param_value(2))
            instruction_pointer += 4
        elif opcode == Opcode.STORE:
            store(1, inp.pop(0))
            instruction_pointer += 2
        elif opcode == Opcode.OUTPUT:
            print(param_value(1))
            instruction_pointer += 2
        elif opcode == Opcode.JIT:
            if param_value(1):
                instruction_pointer = param_value(2)
            else:
                instruction_pointer += 3
        elif opcode == Opcode.JIF:
            if not param_value(1):
                instruction_pointer = param_value(2)
            else:
                instruction_pointer += 3
        elif opcode == Opcode.LT:
            store(3, param_value(1) < param_value(2))
            instruction_pointer += 4
        elif opcode == Opcode.EQ:
            store(3, param_value(1) == param_value(2))
            instruction_pointer += 4
        elif opcode == Opcode.EXIT:
            return
