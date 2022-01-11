# Write your code here
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

# Taking user input to get bigram
while True:
    user_input = input()
    if user_input == "exit":
        break
    try:
        tails = nltk.Counter(model[user_input])
        print(f'Head: {user_input}')
        for tail, count in tails.items():
            print(f"Tail: {tail}\tCount: {count}")
    except KeyError:
        print("Key Error. The requested word is not in the model. Please input another word.")
