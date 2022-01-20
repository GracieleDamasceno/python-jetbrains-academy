# Write your code here
import random

import nltk
import re
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter

# Opening and reading the corpus file
filename = "corpus.txt"#input()
file_content = open(filename, "r", encoding="utf-8")

# Breaking the corpus into individual words
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(file_content.read())
file_content.close()
trigram = list(nltk.trigrams(tokens))

# Building a model based on trigram of tokens
model = {}
for lead_head, second_head, tail in trigram:
    new_head = "{head1} {head2}".format(head1=lead_head, head2=second_head)
    model.setdefault(new_head, Counter())
    model[new_head].update([tail])

# Loop to print 10 sentences
index = 0
while index < 10:
    sentence_index = 0
    end_of_sentence = False
    full_sentence = []

# Selecting an uppercase word as first word of sentence
    random_list = list(model.keys()).copy()
    random.shuffle(random_list)
    for random_list_element in random_list:
        if random_list_element[0].isupper() and re.search('[.!?]', random_list_element) is None:
            previous_word = random_list_element
            break
    full_sentence.append(previous_word)

# Building the rest of sentence
    while not end_of_sentence:
        word_list = list(model[previous_word].keys())
        word_weights = tuple(model[previous_word].values())
        word_sentence = random.choices(word_list, weights=word_weights)

# Removing sentences too small to avoid two sentences at same line
        if len(full_sentence) <= 5 and re.search('[.!?]', " ".join(full_sentence)):
            full_sentence = []
            sentence_index = 0
            end_of_sentence = True
            break

# Ending sentence at nearest punctuation mark when sentence is bigger tha 5 words
        if sentence_index >= 4 and re.search('[.!?]', word_sentence[0]) is not None:
            full_sentence.append(word_sentence[0])
            previous_word = word_sentence[0]
            end_of_sentence = True
            break
        else:
            full_sentence.append(word_sentence[0])
            string_full_sentence = " ".join(full_sentence).split()
            previous_word = " ".join(string_full_sentence[-2:])
            sentence_index += 1

# Printing complete sentence
    if full_sentence:
        print(" ".join(full_sentence))
        index += 1
