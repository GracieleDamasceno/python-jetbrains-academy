# Write your code here
import random

import nltk
import re
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter

# Opening and reading the corpus file
filename = input()
file_content = open(filename, "r", encoding="utf-8")

# Breaking the corpus into individual words
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(file_content.read())
file_content.close()
bigram = list(nltk.bigrams(tokens))

# Building a model based on bigrams of tokens
model = {}
for head, tail in bigram:
    model.setdefault(head, Counter())
    model[head].update([tail])

# Loop to print 10 sentences consisting of pseudo-sentences
for _ in range(10):
    sentence_index = 0
    end_of_sentence = False
    full_sentence = []

# Selecting an Uppercase word as first word of sentence
    random_list = list(model.keys()).copy()
    random.shuffle(random_list)
    for w in random_list:
        if w[0].isupper() and re.search('[.!?]', w) is None:
            previous_word = w
            break
    full_sentence.append(previous_word)

# Building the rest of sentence
    while not end_of_sentence:
        word_list = list(model[previous_word].keys())
        word_weights = tuple(model[previous_word].values())
        word_sentence = random.choices(word_list, weights=word_weights)[0]

# Ending sentence at nearest punctuation mark when sentence is bigger tha 5 words
        if sentence_index >= 3 and re.search('[.!?]', word_sentence) is not None:
            full_sentence.append(word_sentence)
            previous_word = word_sentence
            end_of_sentence = True
            break
        else:
            full_sentence.append(word_sentence)
            previous_word = word_sentence
            sentence_index += 1

    print(" ".join(full_sentence))
