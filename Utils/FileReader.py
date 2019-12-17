class FileReader:

    @staticmethod
    def read_line_by_line_as_int(file_name):
        with open(file_name, "r") as file:
            numbers = []
            for line in file:
                numbers.append(int(line))

        return numbers

    @staticmethod
    def read_line_by_line(file_name):
        with open(file_name, 'r') as file:
            lines = []
            for line in file:
                lines.append(line)

        return lines

    @staticmethod
    def read_separated_values_as_int(file_name, separator):
        with open(file_name, "r") as file:
            data = file.read()
            data_array = data.split(separator)
            data_array = [int(i) for i in data_array]

        return data_array
