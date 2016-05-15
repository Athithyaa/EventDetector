

class FileUtils:

    def __init__(self, f="t.properties"):
        self.__fn = f
        self.__file = open(self.__fn, "r")

    def getProperties(self):
        try:
            dict = {}
            for line in self.__file:
                line = line.replace("\n", "")
                splitStr = line.split("=")
                dict[splitStr[0]] = splitStr[1]
            return dict
        except ValueError:
            print(ValueError)
            return None

    def getWords(self):
        try:
            dict = {}
            for line in self.__file:
                line = line.replace("\n", "")
                line = line.replace(" ", "")
                # TODO: prioritize tweets by assigning ranks to words
                dict[line] = 10
            return dict
        except ValueError:
            print(ValueError)
            return None

    def closeFile(self):
        try:
            self.__file.close()
        except ValueError:
            print('unable to close file')
