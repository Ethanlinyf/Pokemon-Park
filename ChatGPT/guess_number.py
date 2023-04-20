import random

# # generate a random number between 1 and 100
number = random.randint(1, 100)

# # set the number of guesses to 0
guesses = 0

# loop until the user guesses the number
while True:
    # ask the user to guess the number
    guess = int(input("Guess the number between 1 and 100: "))
    
    # increment the number of guesses
    guesses += 1
    
    # check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", guesses, "guesses.")
        break
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
