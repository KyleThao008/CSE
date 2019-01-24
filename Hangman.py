import random
import string
words = ["mississippi", "california", "afghanistan", "japan", "hippopotamus", "germany", "panda", "fruit",
         "mongoose", "moose"]
guesses = 8
letter = string.ascii_letters
word = random.choice(words)
l_guessed = []
win = False

while guesses > 0:
    output = []
    for letter in word:
        if letter in l_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))
    guessed = input("Letter. ")
    l_guessed.append(guessed)
    if guessed in word:
        print("Letter found.")
        print("You have used", l_guessed, "letters already.")
    else:
        print("Wrong letter.")
        print("You have used", l_guessed, "letters already.""You now have", + guesses, "left.")
        guesses -= 1
    if word is output:
        win = True
if win is False:
    print("You have lost.")
else:
    print("You have won.")
