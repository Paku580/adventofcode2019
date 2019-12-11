class IntcodeComputer:
    intcode = []
    instruction_pointer = 0

    def __init__(self, intcode):
        self.intcode = intcode
        self.running = False

    def run_intcode(self):
        self.running = True
        while self.running:
            self.switch_opcode(self.intcode[self.instruction_pointer])

    def add(self):
        self.intcode[self.intcode[self.instruction_pointer + 3]] = self.intcode[
                                                                       self.intcode[self.instruction_pointer + 1]] \
                                                                   + self.intcode[
                                                                       self.intcode[self.instruction_pointer + 2]]
        self.increment_pointer()

    def multiply(self):
        self.intcode[self.intcode[self.instruction_pointer + 3]] = self.intcode[
                                                                       self.intcode[self.instruction_pointer + 1]] \
                                                                   * self.intcode[
                                                                       self.intcode[self.instruction_pointer + 2]]
        self.increment_pointer()

    def finish(self):
        print(self.intcode[0])
        self.running = False

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
        self.instruction_pointer += 4
