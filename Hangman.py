import random
import string
words = ["mississippi", "california", "afghanistan", "japan", "hippopotamus", "germany", "panda", "fruit",
         "mongoose", "moose"]
guesses = 8
letter = string.ascii_lowercase
word = random.choice(words)
guessed = []
l_guessed = []
string = word

while guesses > 0:
    print(word)
    guessed = input("Letter. ")
    l_guessed.append(guessed)
    if guessed in word:
        print("Letter found.")
        print("You have used", l_guessed, "letters already.")
    else:
        print("Wrong letter.")
        print("You have used", l_guessed, "letters already.""You now have", + guesses, "left.")
        guesses -= 1

