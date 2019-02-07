import random
import string
words = ["mississippi", "california", "afghanistan", "japan", "hippopotamus", "germany", "panda", "fruit",
         "mongoose", "moose"]
guesses = 8
letter = string.ascii_letters
word = random.choice(words)
l_guessed = []
punctuation = string.punctuation

while guesses > 0:
    hidden_output = []
    for letter in word:
        if letter in l_guessed:
            hidden_output.append(letter)
        else:
            hidden_output.append("*")
    print("".join(hidden_output))
    if "*" not in hidden_output:
        print("You have won.")
        guesses -= 100
        continue

    guessed = input("Letter. ")
    l_guessed.append(guessed)
    if guessed in word:
        print("Letter found.")
        print("You have used", l_guessed, "letters already.")
    else:
        print("Wrong letter.")
        print("You have used", l_guessed, "letters already.""You now have", + guesses, "left.")
        guesses -= 1
    if guesses == 0:
        print("You have lost.")
