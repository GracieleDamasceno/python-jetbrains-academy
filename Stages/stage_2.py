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

# Printing information
print("Number of bigrams: %s", len(bigram))

# Taking user input to get bigram
while True:
    user_input = input()
    if user_input == "exit":
        break
    try:
        integer = int(user_input)
        print("Head: " + bigram[integer][0] + " Tail: " + bigram[integer][1])
    except ValueError:
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")