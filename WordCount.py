import re
from collections import Counter
import random

class Text():
    def __init__(self, title, number):
        self.title=title
        self.number=number
        file_frequent = open('mostFrequent.txt','r')
        self.frequent=file_frequent.read().splitlines()
        self.processTextFile()

    def processTextFile(self):
        file_name = 'texts/' + self.title + '.txt'
        with open(file_name) as f:
            passage = f.read()
        passage = re.sub("\d+", " ", passage)
        words = re.findall(r'\w+', passage)
        cap_words = [word.upper() for word in words]
        for element in self.frequent:
            if element in cap_words:
                cap_words = list(filter((element).__ne__, cap_words))
        self.word_counts = Counter(cap_words)

    def mostCommon(self):
        print("Most common:")
        s = []
        for letter, count in self.word_counts.most_common(self.number):
            print('%s: %7d' % (letter, count))
            s.append(letter.lower())    
        return s

    def leastComon(self):
        least_common=[]
        print("least common:")
        for word in self.word_counts:
            if self.word_counts[word]==1:
                least_common.append(word.lower())

        small_list = random.sample(least_common, self.number)
        print(small_list)
        return small_list       
