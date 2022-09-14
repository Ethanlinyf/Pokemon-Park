'''
Something Good as Indicated by Joshua, Junhao, Junyu, Jason and Colin

'''
import random


def welcome_message():
    print("Welcome to this Pokemon Platform with sorting algorithm")


class Pokemon:

    def __init__(self, name, age, health, level, power, magic):
        self.name = name
        self.age = age
        self.health = health
        self.level = level
        self.power = power
        self.magic = magic


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


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sorting(arr):
    n = len(arr)

    while n > 1:
        i = 1
    
        while i < n:
            if arr[i] < arr[i-1]:
                swap(arr, i, i-1)
            i += 1

        n -= 1
    
    return arr


def main():
    welcome_message()

    eevee = Pokemon("Eevee", 8, 100, 6, 20, 10)
    ditto = Pokemon("Ditto", 6, 100, 12, 15, 12)

    # race_game(eevee, ditto, 10)

    race_results = []

    for i in range(7):
        race_results.append(race_game(eevee, ditto, 10))

    print(race_results)

    race_results_sorted = bubble_sorting(race_results)

    print(race_results_sorted)


if __name__ == "__main__":
    main()
