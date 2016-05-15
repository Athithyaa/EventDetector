import threading
from twitterDataGatherer.DataGatherer import DataGatherer
from utilities.FileUtils import FileUtils


class GathererRunner(threading.Thread):
    def __init__(self, wl, pfn="t.properties"):
        threading.Thread.__init__(self)
        self.__propFn = pfn
        self.__wordList = wl

    def getKeys(self):
        fu = FileUtils(self.__propFn)
        prop = fu.getProperties()
        fu.closeFile()
        return prop

    def run(self):
        print("=============Starting data gatherer " + self._name + "================")
        dg = DataGatherer()
        keys = self.getKeys()
        dg.authenticate(keys)
        dg.setWordList(self.__wordList)
        dg.initStream()
        print("=============Ending data gatherer==================")

