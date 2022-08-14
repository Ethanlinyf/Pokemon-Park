"""
This is a guess number game  

"""

import random
import time 

# Welcome message
print("Welcome to this Guess Number Game!")


def comparision(randomNumber, guessNumber):
    pass 

def main():
    randomNumber = random.randint(0, 100)
    guessNumber = int(input("Please enter your guess number: "))

    comparision(randomNumber, guessNumber)
    



if __name__ == "__main__":
    main()