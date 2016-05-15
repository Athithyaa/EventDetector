import tweepy
from kafka import KafkaProducer
from kafka.common import KafkaError


class TStreamListner(tweepy.StreamListener):

    def __init__(self):
        tweepy.StreamListener.__init__(self)
        self.__kProducer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def on_status(self, status):
        self.__kProducer.send('test', str(status.text).encode())

