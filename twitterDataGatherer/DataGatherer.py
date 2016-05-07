from twitterDataGatherer.TStreamListner import TStreamListner
from utilities.FileUtils import FileUtils
import tweepy


class DataGatherer:

    def __init__(self):
        fu = FileUtils()
        prop = fu.getProperties()
        auth = tweepy.OAuthHandler(prop.get("APIKEY"), prop.get("APISECRET"))
        auth.set_access_token(prop.get("ACCESSTOKEN"), prop.get("ACCESSTOKENSECRET"))
        self.__stream = tweepy.Stream(auth, TStreamListner())
        fu = FileUtils("wordlist")
        wordDict = fu.getWords()
        wordList = list(wordDict.keys())
        self.__stream.filter(track=wordList)




DataGatherer()