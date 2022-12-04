'''
Something Good as Indicated by Junhao, Junyu, Jason, Colin

Topic: Dictionary in Python
'''


class Pokemon:
    def __init__(self, name, age, typee, level, agility, strenght, intelligence):
        self.name = name
        self.age = age
        self.typee = typee
        self.level = level
        self.agility = agility
        self.strenght = strenght
        self.intelligence = intelligence

    def display(self):
        pokemon_dic = {
            'Name': self.name,
            'Age': self.age,
            'Type': self.typee,
            'Level': self.level,
            }

        for key, value in pokemon_dic.items():
            print(key, ' : ', value)
        


def welcome_message():
    print("Welcome to Pokemon Park!")

    
def main():
    welcome_message()

    ditto = Pokemon("Ditto", 2, 'fire', 1000, 10, 1, 7)

    eevee = Pokemon("Eevee", 5, 'water', 2, 8, 9, 22)

    ditto.display()
    print(ditto.test)


if __name__ == "__main__":
    main()
