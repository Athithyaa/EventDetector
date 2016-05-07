from twitterDataGatherer.TStreamListner import TStreamListner
from utilities.FileUtils import FileUtils
import tweepy


class DataGatherer:

    def __init__(self):
        self.__listner = TStreamListner()
        self.__stream = tweepy.Stream()
        fu = FileUtils()
        prop = fu.getProperties()
        self.auth = tweepy.Stream(auth = )
