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
        the_biggest = 0

        for i in a_list:
            if i > the_biggest:
                the_biggest = i

        print("The biggist one is ", the_biggest)