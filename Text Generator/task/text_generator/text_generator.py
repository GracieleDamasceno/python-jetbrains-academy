# Write your code here
from nltk.tokenize import WhitespaceTokenizer
# Opening and reading the corpus file
filename = input()
file_content = open(filename, "r", encoding="utf-8")
# Breaking the corpus into individual words
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(file_content.read())
file_content.close()
# Printing information
print("Corpus statistics")
print("All tokens: ", len(tokens))
print("Unique tokens: ", len(set(tokens)))
# Taking user input
while True:
    user_input = input()
    if user_input == "exit":
        break
    try:
        integer = int(user_input)
        print(tokens[integer])
    except ValueError:
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
