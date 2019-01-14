import random
words = ["mississippi", "california", "afghanistan", "japan", "hippopotamus", "germany", "panda", "fruit",
         "mongoose", "moose"]
letter = input("Guess a letter. ")
guesses = 8
letters = ["a", "b", "c", "d", "e", "f", "g"]
guess = letters

word = random.choice(words)
print(word)
if letter in word:
    letter.join(letters)
