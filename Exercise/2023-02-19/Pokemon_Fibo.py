
import os
import matplotlib.pyplot as plt

def display_option():
    os.system("clear")
    print("1. Welcome to this extended Pokemon Gardon")
    print("2. Create a Fibonacci Sequence")
    print("3. Generate a golden ratio")
    print("4. Plot the generated ratio list")

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

    fib = [0, 1]
    
    for i in range(n):
        fib.append(fib[i] + fib[i+1])
        
    return fib

def golder_ratio(fib):

    gratio = [fib[i] / float(fib[i-1]) for i in range(2, len(fib))]

    return gratio

def extended_menu(choice):
    match choice:
        case "1":
            welcome_message("Ethan")
        case "2":
            print(fibo_sequence(10))
        case "3":
            print(golder_ratio(fibo_sequence(10)))
        case "4":
            gratio = golder_ratio(fibo_sequence(10))
            plt.plot(gratio)
            plt.show()
        case _:
            print("Not valid choice.")


def main():
    extended_menu(display_option())


if __name__ == '__main__':
    main()

main()
