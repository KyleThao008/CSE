import random
guesses_left = 5
number = random.randint(0, 10)
win = False

while guesses_left > 0:
    guess = int(input("Enter in a number: "))
    guesses_left -= 1
    if guess == number:
        win = True
        guesses = 0
    elif guess > number:
        print("Your guess is too high. You have", guesses_left, "guesses remaining.")
    elif guess < number:
        print("Your guess is too low. You have", guesses_left, "guesses remaining.")
if win is False:
    print("Sorry, you didn't guess the number", number)
else:
    print("Congrats, you guessed correct")