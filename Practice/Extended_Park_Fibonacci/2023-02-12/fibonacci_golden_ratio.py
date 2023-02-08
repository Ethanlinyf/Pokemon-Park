"""
Something Good as Indicated: 
Created by ... on 2023-01-08
"""

import matplotlib.pyplot as plt

def welcome_message(name):
    match name:
        case "Junhao":
            print("Go away ~")
        case "Junyu":
            print("Hi ~ ")
        case "Jason":
            print("Bye")
        case "Colin":
            print("I don't know")
        case _:
            print("Welcome to this Python program.")



def fibo_seq(n):
    fib = [0, 1]

    match n:
        case 1:
            fib = [0]
            return fib
        case 2: 
            return fib
        case _:
            for i in range(n-2):
                fib.append(fib[i]+fib[i+1])

            return fib

def golder_ratio(fib):

    gratio = [fib[i] / float(fib[i-1]) for i in range(2, len(fib))]

    return gratio


def main():
    welcome_message("")
    fib = fibo_seq(20)
    print(fib)

    gratio = golder_ratio(fib)
    print(gratio)

    plt.plot(gratio)
    plt.show()

if __name__ == "__main__":
    main()