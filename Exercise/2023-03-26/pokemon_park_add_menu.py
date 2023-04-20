# import needed modules for Pokemon Platform
import random
import time
import os
import matplotlib.pyplot as plt


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


def main():
    fibo = Pokemon_Fib("Fibo", 100, 5, 30, 22, 50)
    fibo.display()
    print(fibo.fibo_sequence(10))
    print(fibo.golden_ratio(10))

    fibo.plot(10)

    print(fibo.fibo_sequence(10))


if __name__ == "main":
    main()

main()
