from twitterDataGatherer.GathererRunner import GathererRunner
from utilities.FileUtils import FileUtils
import threading
from kafka import KafkaConsumer


class MyConsumer(threading.Thread):
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest')
        consumer.subscribe(['test'])
        for message in consumer:
            print(message)


fu = FileUtils("wordlist")
wordList = list(fu.getWords().keys())
fu.closeFile()

t1 = GathererRunner(wordList[0:int(len(wordList)/2)])
t1.start()
t2 = GathererRunner(wordList[int(len(wordList)/2):], "t1.properties")
t2.start()

t3 = MyConsumer()
t3.start()
