from Utils.FileReader import FileReader
from itertools import permutations
from IntcodeComputer import run

if __name__ == '__main__':
    intcode = FileReader.read_separated_values_as_int("input.txt", ',')
    phase_settings = list(permutations(range(0, 5)))
    thruster_signals = []

    for phase_setting in phase_settings:
        thruster_signals.append(run(intcode.copy(),
                                    [phase_setting[4],
                                     run(intcode.copy(),
                                         [phase_setting[3],
                                          run(intcode.copy(),
                                              [phase_setting[2],
                                               run(intcode.copy(),
                                                   [phase_setting[1],
                                                    run(intcode.copy(),
                                                        [phase_setting[0], 0])[-1]])[-1]])[-1]])[-1]])[-1])
    print(max(thruster_signals))
