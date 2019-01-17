import random
import string
words = ["mississippi", "california", "afghanistan", "japan", "hippopotamus", "germany", "panda", "fruit",
         "mongoose", "moose"]
guesses = 8
letter = string.ascii_lowercase
guessed = []
word = random.choice(words)

while guesses > 0:

    print(word)
    guessed = input("Letter. ")
    print(guessed)
    if guessed in word:
        print("Letter found.")
        print("You have used", guessed, "letters already.")
    else:
        print("Wrong letter.")
        print("You have used", guessed, "letters already.")
        guesses -= 1
