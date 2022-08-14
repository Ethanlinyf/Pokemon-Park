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

    def create_random_list(self, number):
        mylist = []

        for i in range(number):
            mylist.append(random.randint(0, 100))

        print(mylist)

def main():
    ditto = Pokemon("Ditto", 6, 5, 100, 50, 20)
    ditto.welcome()

    ditto.create_random_list(5)

if __name__ == "__main__":
    main()
