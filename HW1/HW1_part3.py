#=============================================================
# Information Retrieval -- CSCI 4130
# Homework 1
# by: Colby Sawyer - sawyerc17@students.ecu.edu - B01204512
#=============================================================

from nltk.tokenize import RegexpTokenizer
import os
from nltk.corpus import stopwords
from collections import OrderedDict
from collections import Counter
import itertools
from nltk.stem.porter import PorterStemmer
from colorama import Fore, Style

ps = PorterStemmer()

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
staticNumWords = numWords
print("\n1. Number of Words \t" + str(numWords))

vocabSize = len(tokenUnique)
staticVocabSize = vocabSize
print("\n2. Vocabulary Size\t" + str(vocabSize))

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

target = round(vocabSize * .15);
numTarget = 0
for x in tokenUniqueCount:
    if x >= target:
        numTarget += 1
print("\n5. Number of words that occur " + str(target) + " or more times : " + str(numTarget))

print("\n\nAFTER STEM AND STOP WORD REMOVAL:")
#Stem and Remove Stop Words
#TODO Implement Porter Stemmer
for x in tokens:
    x = ps.stem(x)

#TODO Throw out stop words
stopWords = open("stopwords.txt").read()
countVocabRemoved = 0
for member in dict.copy():
    #print(member)
    if member.lower() in stopWords:
        countVocabRemoved += 1
        dict.pop(member)
        tokens.remove(member)

tokenUnique = dict.keys()
tokenUniqueCount = dict.values()

vocabSizeAfter = len(tokenUnique)
numWords = len(tokens)
print("\n1. Number of Words \t" + str(numWords) + Fore.RED + "(-" + str(staticNumWords-numWords) + ")" + Style.RESET_ALL)

vocabSize = len(tokenUnique)
print("\n2. Vocabulary Size\t" + str(vocabSize)+ Fore.RED + "(-" + str(staticVocabSize - vocabSizeAfter) + ")" + Style.RESET_ALL)

sortedDict = OrderedDict(sorted(dict.items(), key=lambda x: x[1], reverse=True))
topTwenty = {k: sortedDict[k] for k in list(sortedDict)[:20]}
print("\n3. Top 20 Words:\n")
print(topTwenty)

target = round(vocabSize * .15);
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



