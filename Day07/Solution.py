from Utils.FileReader import FileReader
from itertools import permutations
from IntcodeComputer import Computer
from IntcodeComputer import State


def run_amplifier_single_mode(setting_sequences) -> int:
    thruster_signals = []
    for setting_sequence in setting_sequences:
        inp = 0
        for index, phase_setting in enumerate(setting_sequence):
            computer = Computer(intcode.copy(), [phase_setting, inp])
            out = computer.run()[-1]
            inp = out
            if index == len(setting_sequence) - 1:
                output = out
        thruster_signals.append(output)
    return max(thruster_signals)


def run_amplifier_feedback_mode(setting_sequences) -> int:
    thruster_signals = []
    for setting_sequence in setting_sequences:
        inp = 0
        for index, phase_setting in enumerate(setting_sequence):
            computer = Computer(intcode.copy(), [phase_setting])
            while computer.state != State.TERMINATED:
                out = computer.run()[-1]
                if index == len(setting_sequence) - 1:
                    computer.inp = [out]
            if index == len(setting_sequence) - 1:
                output = out
        thruster_signals.append(output)
    return max(thruster_signals)


if __name__ == '__main__':
    intcode = FileReader.read_separated_values_as_int("input.txt", ',')
    # Part 1
    # print(run_amplifier_single_mode(list(permutations(range(0, 5)))))
    # Part 2
    print(run_amplifier_feedback_mode(list(permutations(range(5, 10)))))
