# print("Hello World")
# # single line comment
# cars = 5
# driving = True
# # cars = 5 → "5"
#
# print("I have %s cars." % cars)
# """
# age = input("How old are you?")
# print("You're %s? That's cool I guess." % age)
# """
#
# colors = ["blue", "yellow", "orange", "green",  "red"]
# colors.append("cyan")
#
# print(colors)
#
# colors.pop(0)
# print(len(colors))
# print(colors)
#
# print(colors[2])
#
# for i in range(len(word)):

import random
import string
words = ["miss_issippi"]
guesses = 8
letter = string.ascii_letters
word = random.choice(words)
l_guessed = []

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

