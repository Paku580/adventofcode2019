from Utils.FileReader import FileReader

if __name__ == '__main__':
    image_data = FileReader.read_line_by_line("input.txt")[0]
    width = 25
    height = 6
    layers = [image_data[i:i + width * height] for i in range(0, len(image_data), width * height)]

    # Part 1
    layer_with_least_zeroes = min(layers, key=lambda layer: layer.count('0'))
    print(layer_with_least_zeroes.count('1') * layer_with_least_zeroes.count('2'))

    # Part 2
    image = [next(layer[i] for layer in layers if layer[i] != '2') for i in range(width * height)]
    translation_table = {48: ' ', 49: '#'}

    for i in range(0, width*height, 25):
        print(' '.join(image[i:i+width]).translate(translation_table))
