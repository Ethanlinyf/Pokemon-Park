'''
Something Good as Indicated by Joshua, Junhao, Junyu, Jason and Colin

'''


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


def main():
    welcome_message()


if __name__ == "__main__":
    main()
