

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



def main():
    ditto = Pokemon("Ditto", 6, 5, 100, 50, 20)
    ditto.welcome()

if __name__ == "__main__":
    main()


# Welcome, Ditto to this Pokemon World! 
