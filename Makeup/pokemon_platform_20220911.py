"""
Something Good as Indicated by ...
0. import a template
1. create a Pokemon class
2. create a menu
"""

import random
import time
from matplotlib import pyplot as plt
import math


class Pokemon:
    def __init__(self, name, age, health, level, power, magic):
        self.name = name
        self.age = age
        self.health = health
        self.level = level
        self.power = power
        self.magic = magic

    def display(self):
        pokemon_dic = {
            'Name': self.name,
            'Age': self.age,
            'Health': self.health,
            'Level': self.level,
            'Power': self.power,
            'Magic': self.magic,
        }


def welcome_message():
    print("Welcome to this Pokemon-Park")


def race_game(p1, p2, r):
    p1_movelist = []

    for x in range(r):
        p1_movelist.append(random.randint(1, 10))

    # print(p1_movelist)

    print("|", end="")

    for x in range(r):
        # time.sleep(0.5)
        for y in range(p1_movelist[x]):
            print("-", end="")
        print(p1_movelist[x], end="")

    print(p1.name[0].capitalize() + "(" + str(sum(p1_movelist)) + ")")

    p2_movelist = []

    for x in range(r):
        p2_movelist.append(random.randint(1, 10))

    # print(p2_movelist)

    print("|", end="")

    for x in range(r):
        # time.sleep(0.5)
        for y in range(p2_movelist[x]):
            print("-", end="")
        print(p2_movelist[x], end="")

    print(p2.name[0].capitalize() + "(" + str(sum(p2_movelist)) + ")")

    if sum(p1_movelist) > sum(p2_movelist):
        print("Ditto wins this racing game")
    elif sum(p1_movelist) < sum(p2_movelist):
        print("Eevee wins this racing game")
    else:
        print("Finally, it is a tie. ")

    return sum(p1_movelist) - sum(p2_movelist)


def babble_sorting(arr):
    lenth = len(arr)

    for i in range(lenth):
        for j in range(0, lenth-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def main():
    welcome_message()
    eevee = Pokemon("Eevee", 8, 100, 8, 20, 5)
    ditto = Pokemon("Ditto", 6, 100, 9, 18, 3)
    boop = Pokemon("boop", 8, 9, 212, 12, 3)

    competition = []

    for i in range(10):
        competition.append(race_game(eevee, ditto, 10))

    print(competition)
    results = babble_sorting(competition)

    print(results)
    # plt.bar(range(10), results)
    # plt.show()

    print("Eevee wins the most, ", results[9])
    print("Ditto wins the most, ", abs(results[0]))


if __name__ == "__main__":
    main()
