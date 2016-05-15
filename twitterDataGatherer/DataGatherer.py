from twitterDataGatherer.TStreamListner import TStreamListner
import tweepy


class DataGatherer:
    def __init__(self):
        self.__stream = None
        self.__auth = None
        self.__wordList = ['twitter']

    def authenticate(self, keyDict):
        try:
            self.__auth = tweepy.OAuthHandler(keyDict.get("APIKEY"), keyDict.get("APISECRET"))
            self.__auth.set_access_token(keyDict.get("ACCESSTOKEN"), keyDict.get("ACCESSTOKENSECRET"))
        except ValueError:
            print('unable to find keys')

    def initStream(self):
        if self.__auth is not None:
            try:
                self.__stream = tweepy.Stream(self.__auth, TStreamListner())
                self.__stream.filter(track=self.__wordList, languages=['en'])
            except ValueError:
                print(ValueError)
        else:
            print('authenticate first and set word list')

    def setWordList(self, wl):
        self.__wordList = wl