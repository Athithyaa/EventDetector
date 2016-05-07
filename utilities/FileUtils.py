

class FileUtils:

    def __init__(self):
        self.__fn = "../twitterDataGatherer/t.properties"
        self.__file = open(self.__fn, "w")

    def __init__(self, f):
        self.__fn = f
        self.__file = open(self.__fn, "w")

    def getProperties(self):
        dict = {}
        for line in self.__file:
            splitStr = line.split("=")
            dict[splitStr[0]] = splitStr[1]
        return dict

