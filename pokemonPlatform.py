# Random for create a random number
import random

# a class for creating Pokemon heros
class Pokemon:
    def __init__(self, name, age, level, health, power, magic):
        self.name = name
        self.age = age
        self.level = level
        self.health = health
        self.power = power
        self.magic = magic

    def welcome(self):
        print("Welcome to this Pokemon World!")

    def findTheSmallOne(self, aList):
        theSmallOne = 100

        for i in aList:
            if i < theSmallOne:
                theSmallOne = i

        print(theSmallOne)


def create_random_list(n):
    myList = []

    for i in range(n):
        myList.append(random.randint(1, 100))

    print(myList)
    return myList

def main():
    ditto = Pokemon("Ditto", 6, 5, 100, 50, 20)
    ditto.welcome()

    aList = create_random_list(100)
    ditto.findTheSmallOne(aList)


if __name__ == "__main__":
    main()
