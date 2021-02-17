#=============================================================
# Information Retrieval -- CSCI 4130
# Homework 1
# by: Colby Sawyer - sawyerc17@students.ecu.edu - B01204512
#=============================================================

from nltk.tokenize import RegexpTokenizer
import os
from collections import OrderedDict
from collections import Counter
from nltk.corpus import stopwords
import itertools

print("Welcome to the Tokenizer")
tokenizer = RegexpTokenizer(r"\w+")
dir_name = input("Input the collection directory name:")
directory = os.fsencode(dir_name)
tokens = []
for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    #print(str(fileName))
    file_content = open(os.path.join(dir_name, fileName)).read()
    tokens.append(tokenizer.tokenize(file_content))
#print(tokens)
tokens = list(itertools.chain.from_iterable(tokens))

dict = Counter(tokens)
tokenUnique = dict.keys()
tokenUniqueCount = dict.values()

numWords = len(tokens)
print("\n1. Number of Words \t" + str(numWords))

vocabSize = str(len(tokenUnique))
print("\n2. Vocabulary Size\t" + vocabSize)

sortedDict = OrderedDict(sorted(dict.items(), key=lambda x: x[1], reverse=True))
topTwenty = {k: sortedDict[k] for k in list(sortedDict)[:20]}
print("\n3. Top 20 Words:\n")
print(topTwenty)

stopWords = set(stopwords.words('english'))
stopWordsFrom20 = []
for member in topTwenty:
    if member in stopWords:
        stopWordsFrom20.append(member)

print("\n4. Top 20 Words (Stop Words): " + str(len(stopWordsFrom20)))
print(stopWordsFrom20)

target = round(numWords * .15);
numTarget = 0
for x in tokenUniqueCount:
    if x >= target:
        numTarget += 1
print("\n5. Number of words that occur " + str(target) + " or more times : " + str(numTarget))

#=============================================================
#DEBUG SECTION
#=============================================================
#print("\nVocab:")
#print(tokenUnique)
#print(tokenUniqueCount)

#print("\nDictionary:")
#print(dict)

#print("\nSorted Dictionary:")
#print(sortedDict)



