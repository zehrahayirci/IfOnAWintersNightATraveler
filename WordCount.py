import re
from collections import Counter

file_frequent = open('mostFrequent.txt','r')
frequent=file_frequent.read().splitlines()
#with open('texts/TellTaleHearth.txt') as f:
with open('texts/TheLastLeaf.txt') as f:
#with open('texts/TheCantervilleGhost.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]
for element in frequent:
    if element in cap_words:
        cap_words = list(filter((element).__ne__, cap_words))
#print(frequent)
#print(cap_words)


word_counts = Counter(cap_words)

#print(word_counts)

print("Most common:")
for letter, count in word_counts.most_common(20):
    print('%s: %7d' % (letter, count))

print("least common:")
for word in word_counts:
    if word_counts[word]==1:
        print(word)



