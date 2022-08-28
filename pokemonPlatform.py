# Random for create a random number
import random


class Pokemon:

    def __init__(self, name, age, level, health, power, magic):
        self.name = name
        self.age = age
        self.level = level
        self.health = health
        self.power = power
        self.magic = magic

    def welcome(self):
        print("Welcome, %s to this Pokemon World!" % self.name)

    def find_the_small_one(self, a_list):
        the_small_one = 100
        for i in a_list:
            if i < the_small_one:
                the_small_one = i
        print("Well done, %s the smallest one is" % self.name, the_small_one)

    def find_the_biggest_one(self, a_list):
        the_biggist = 0

        for i in a_list:
            if i > the_biggist:
                the_biggist = i
        
        print("The biggist one is ", the_biggist)

def statium(pokemon_1, pokemon_2):
    pass

def create_random_list(n):
    my_list = []

    for i in range(n):
        my_list.append(random.randint(1, 100))

    print(my_list)
    return my_list


def main():
    ditto = Pokemon("Ditto", 6, 5, 100, 50, 20)
    ditto.welcome()

    a_list = create_random_list(100)
    ditto.find_the_small_one(a_list)
    ditto.find_the_biggest_one(a_list)



if __name__ == "__main__":
    main()
