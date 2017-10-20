class FileParser:
    """ FileParser is a class used to parse both lines and words from a file. I will also sterilize the data """

    # TODO: When cleaning lines. Check that it's not a whitelisted use of a period

    def __init__(self, file_name):
        """ We read a file named :file_name: and put all of the words and lines into a variable

        :param file_name:       The name of the file we want to parse
        """

        file_reader = open(file_name, "r", encoding="utf8")

        self.words = []
        self.lines = file_reader.read().splitlines()

        # Goes through all the lines, cleans them, then splits it up into words and adds them to the words variable
        for line in self.lines:
            self.words += line.split()

    @staticmethod
    def clean_line(line):
        """ We clean a line. At the moment we just add the [NONE] token at the end of sentences.

        :param line:    The line we want to clean
        :return:        The cleaned line
        """

        return line.replace('.', ' [NONE]')
