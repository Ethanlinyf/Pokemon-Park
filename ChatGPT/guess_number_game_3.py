
import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

# ask the user to input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# calculate the difference between the random number and each number
diff1 = abs(number - num1)
diff2 = abs(number - num2)

# determine which number is closer
if diff1 < diff2:
    closer_num = num1
else:
    closer_num = num2

    # set the number of guesses to 0
guesses = 0

# set the maximum number of guesses
max_guesses = 5

# loop until the user guesses the number or runs out of guesses
while guesses < max_guesses:
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

# if the user runs out of guesses, display the correct number
if guesses == max_guesses:
    print("Sorry, you ran out of guesses. The correct number was", number)

# display the closer number to the generated random number
print("The closer number to the generated random number was", closer_num)


