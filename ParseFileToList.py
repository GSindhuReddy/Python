class ParseFileToList:

    def __init__(self, filename):
        self.filename = filename

    def parse_file(self, filename=None):
        if filename is None:
            filename = self.filename
        cities_list = []
        with open(filename) as f:
            line = f.readlines()
            for i in range(len(line) - 1):
                cities_list.append(line[i].split())
        return cities_list
