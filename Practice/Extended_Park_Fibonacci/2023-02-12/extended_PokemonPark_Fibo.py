
import os
from Fibonacci_gui import *
from fibonacci_golden_ratio import *


def display_option():
    os.system("clear")
    print("1. Welcome to this extended Pokemon Gardon")
    print("2. Create a Fibonacci Sequence")
    print("3. Plot the Fibonacci figures")
    print("4. Generate a golden ratio")

    return input("Your Choice: ")


def welcome_message(name):
    if name == "Junhao":
        print("Welcome")
    elif name == "Jason": 
        print("Dont Go Away ~")
    elif name == "Junyu":
        print("Welcom to this Fibonacci world")
    else:
        print("Welcome to this extended Pokemon Park")


def fibo_sequence(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def extended_menu(choice):
    match choice:
        case "1":
            welcome_message("Ethan")
        case "2":
            fibo_sequence(10)
        case "3":
            draw_Fib_Squares(8)
            sprial()
            wn.exitonclick()
        case "4":
            fib = fibo_seq(20)
            print(fib)

            gratio = golder_ratio(fib)
            print(gratio)

            plt.plot(gratio)
            plt.show()
        case _:
            print("Not valid choice.")


def main():
    extended_menu(display_option())


if __name__ == '__main__':
    main()
