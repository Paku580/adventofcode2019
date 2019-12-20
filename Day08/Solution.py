from Utils.FileReader import FileReader
import textwrap


def find_layer_by_min_occurrences(digit: int) -> int:
    min_layer = 0

    for index, layer in enumerate(image_data):
        counts = [row.count(str(digit)) for row in layer]
        if sum(counts) < count_occurrences(min_layer, digit):
            min_layer = index
    return min_layer


def multiply(layer: int, multiplicand: int, multiplier: int) -> int:
    return count_occurrences(layer, multiplicand) * count_occurrences(layer, multiplier)


def count_occurrences(layer: int, digit: int) -> int:
    return sum([row.count(str(digit)) for row in image_data[layer]])


if __name__ == '__main__':
    image_data = FileReader.read_line_by_line("input.txt")[0]
    width = 25
    height = 6
    image_data = textwrap.wrap(image_data, width)
    image_data = [image_data[i:i + height] for i in range(0, len(image_data), height)]
    # Part 1
    print(multiply(find_layer_by_min_occurrences(0), 1, 2))
