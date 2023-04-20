import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

# set the maximum number of guesses
max_guesses = 8

def guess_number(guess):
    if guess == number:
        print("Congratulations, you guessed guesses!")
        return 1
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    
def main(guesses):
    # loop until the user guesses the number or runs out of guesses
    while guesses < max_guesses:
        # get the user's guess
        guess = int(input("Guess a number between 1 and 100: "))

        # increment the number of guesses
        guesses += 1

        # check if the guess is correct
        if guess_number(guess):
            break

    # if the user runs out of guesses, print the correct number
    if guesses == max_guesses:
        print("Sorry, you ran out of guesses. The correct number was", number)

if __name__ == "__main__":
    main(0)
main(0)
