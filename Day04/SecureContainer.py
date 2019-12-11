from Utils.FileReader import FileReader
import itertools
import operator


def matching_passwords():
    bounds = FileReader.read_separated_values_as_int("input.txt", '-')
    range_start = bounds[0]
    range_end = bounds[1]
    password_count = 0

    for password in range(range_start, range_end + 1):
        digit_list = [int(password) for password in str(password)]
        if (any(map(operator.eq, digit_list, itertools.islice(digit_list, 1, None)))
                # for part 1 comment out line below
                and any(len(list(v)) == 2 for _, v in itertools.groupby(str(password)))
                and digit_list == sorted(digit_list)):
            password_count += 1
    print(password_count)


def main():
    matching_passwords()


if __name__ == '__main__':
    main()
