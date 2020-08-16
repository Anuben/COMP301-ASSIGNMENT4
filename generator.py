
"""
File Name: generator.py
Author: Anuben Keshavala
Student ID: 301120629
Date: August 16, 2020
File Description:  Generate the sentence
"""
import random

# Read the file, make the tuple temporary list and return words
def getWords(filename):

    fln = open(filename)
    temp_list = list()
    for each_line in fln:
        each_line=each_line.strip()
        temp_list.append(each_line)
    words = tuple(temp_list)
    fln.close()
    return words

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt') 
adjectives = getWords('adjectives.txt')
conjuction = getWords('conjuction.txt')

def sentence():
    
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    adjective = ""
    adjectivePhse = random.randrange(100) + 1
    if(adjectivePhse > 50):
        adjective = adjectivePhase()
    
    return random.choice(articles) + " " + adjective + " " + random.choice(nouns)  

def adjectivePhase():
    return random.choice(adjectives)

def verbPhrase():
    prepoandconjuctionPharse = ""
    prepoandconjuctionsPharse = random.randrange(100) + 1
    if(prepoandconjuctionsPharse > 50):
        prepoandconjuctionPharse  = prepositionalPhrase()

    else:
        prepoandconjuctionPharse  = conjuctionPharse() 
    
    return random.choice(verbs) + " " + nounPhrase() + " " + prepoandconjuctionPharse
    
   
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase() 

def conjuctionPharse():
   return random.choice(conjuction) + " " + nounPhrase() + " " + verbPhrase()

def main():
    
    number = int(input("Enter the number of sentences: "))

    for count in range (number):
        print(sentence())  

main()







