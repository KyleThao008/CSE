import random
import string
words = ["mississippi", "california", "afghanistan", "japan", "hippopotamus", "germany", "panda", "fruit",
         "mongoose", "moose"]
guesses = 8
letters = string.ascii_lowercase
guessed = []

while guesses is 8:
    word = random.choice(words)
    print(word)
    print(input("Letter. "))
    guesses -= 1
    