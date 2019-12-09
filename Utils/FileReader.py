class FileReader:

    @staticmethod
    def read_file_line_by_as_int(file_name):
        with open(file_name, "r") as file:
            numbers = []
            for line in file:
                numbers.append(int(line))

        return numbers
