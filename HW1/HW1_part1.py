#=============================================================
# Information Retrieval -- CSCI 4130
# Homework 1
# by: Colby Sawyer - sawyerc17@students.ecu.edu - B01204512
#=============================================================

import os
from collections import Counter
import itertools
import string

#TODO:Implement own tokenizer
def customTokenizer(content):
    tokens = []
    filecontent = content
    tokens = filecontent.split()
    for x in tokens:
        index = tokens.index(x)
        if x == " " or x == "\n" or x == "\t" or x in string.punctuation:
            #print("Found One: " + x)
            tokens.remove(x)
        else:
            for y in x:
                if y == " " or y == "\n" or y == "\t" or y in string.punctuation:
                    newString = x.replace(y, '')
                    tokens[index] = newString
    return tokens

print("Welcome to the Tokenizer")
dir_name = input("Input the collection directory name:")
directory = os.fsencode(dir_name)
tokens = []
for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    #print(str(fileName))
    file_content = open(os.path.join(dir_name, fileName)).read()
    tokens.append(customTokenizer(file_content))
#print(tokens)
tokens = list(itertools.chain.from_iterable(tokens))

dict = Counter(tokens)
tokenUnique = dict.keys()
tokenUniqueCount = dict.values()

numWords = len(tokens)
print("\n1. Number of Words \t" + str(numWords))

vocabSize = str(len(tokenUnique))
print("\n2. Vocabulary Size\t" + vocabSize)

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





