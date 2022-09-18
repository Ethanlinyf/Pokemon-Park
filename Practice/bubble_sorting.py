"""
Bubble sorting algorithm crated by Mia, Jocelyn, Cherry and Ethan
"""
import random


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
    print("Welcome to this bubble sorting algrithm by ...")


def random_list(n):
    arr = []

    for i in range(n):
        arr.append(random.randint(1, 100))

    return arr


def bubble_sorting(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr 


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


def main():
    welcome_message()

    eevee = Pokemon("Eevee", 8, 100, 5, 20, 15)
    ditto = Pokemon("Ditto", 6, 100, 4, 3, 8)

    race_results = []

    for i in range(10):
        race_results.append(race_game(eevee, ditto, 10))

    print(race_results)

    sorted_race_results = bubble_sorting(race_results)

    print(sorted_race_results)


if __name__ == "__main__":
    main()