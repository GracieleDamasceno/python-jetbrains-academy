# Write your code here
import random

import nltk
from nltk.tokenize import WhitespaceTokenizer

# Opening and reading the corpus file
filename = input()
file_content = open(filename, "r", encoding="utf-8")

# Breaking the corpus into individual words
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(file_content.read())
file_content.close()
bigram = list(nltk.bigrams(tokens))

model = {}

for head, tail in bigram:
    model.setdefault(head, []).append(tail)

last_word = random.choice(tokens)
for i in range(10):
    tails = nltk.Counter(model[last_word])
    sentence = ""
    for j in range(10):
        tails_list = list(tails.keys())
        weights_list = list(tails.values())
        next_word = ''.join(random.choices(tails_list, weights_list))
        sentence = sentence + " " + next_word
        tails = nltk.Counter(model[next_word])
        if j == 10:
            last_word = tails_list[-1]
    print(sentence)
