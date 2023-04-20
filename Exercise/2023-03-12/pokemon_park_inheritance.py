# import needed modules for Pokemon Platform
import random
import time
import os
import matplotlib.pyplot as plt
from numpy.lib.arraypad import pad

# a class to create Pokemon heroes
class Pokemon:
    def __init__(self, name, health, level, power, magic, energy):
        self.name = name
        self.health = health
        self.level = level
        self.power = power
        self.magic = magic
        self.energy = energy

    def display(self):
        pokemon_dic = {
            'Name': self.name,
            'Health': self.health,
            'Level': self.level,
            'Power': self.power,
            'Magic': self.magic,
            'Energy': self.energy
        }

        for key, value in pokemon_dic.items():
            print(key, ' : ', value)

        print()

    def attack(self):
        return random.randint(1, 10)

    def rps(self):
        rps_list = ["Rock", "Paper", "Scissors"]

        return random.choice(rps_list)

    
class Pokemon_Fib(Pokemon):
    def __init__(self, name, health, level, power, magic, energy):
        super().__init__(name, health, level, power, magic, energy)

    def fibo_sequence(self, n):
        fib = [0, 1]

        for i in range(n):
            fib.append(fib[i] + fib[i + 1])

        return fib

    def golden_ratio(self, n):  

        gratio = [self.fibo_sequence(n)[i] / float(self.fibo_sequence(n)[i - 1]) for i in range(2, len(self.fibo_sequence(n)))]

        return gratio

    def plot(self, n):
        gratio = self.golden_ratio(n)
        plt.plot(gratio)
        plt.show()

    def menu_message(self):
        pass

    def menu_items(self):
        pass


def Pokemon_menu (pokemon):
    print("Next, we are in xxx building ~ to have some practices about Fibonacci")

    choice = True
    while choice:
        print("""
                1. Display your choice
                2. Fight
                3. Race
                4. Exit(Quit)
        """)

        choice = input("What is your choice for your Pokemon: ")

        if choice == "1":
            pokemon.item_1()

        elif choice == "2":
            pokemon.item2()

        elif choice == "3":
            pokemon.item3()

        elif choice == "4":
            pokemon.item4()

        else:
            print("Not valid choice.")
    

def main():

    print("Welcome to this Pokemon game: ")

    fibo = Pokemon_Fib("Fibo", 100, 5, 30, 22, 50)

    Pokemon_menu(fibo)
    
    fibo.display()
    print(fibo.fibo_sequence(10))
    print(fibo.golden_ratio(10))

    fibo.plot(10)

    Pokemon_menu(fibo.display(), print(fibo.fibo_sequence(10)), print(fibo.golden_ratio(10)), fibo.plot(10))


if __name__ == "main":
    main()

main()
