class Pokemon:
    def __init__(self, name, health, level, power, magic, energy):
        self.name = name
        self.health = health
        self.level = level
        self.power = power
        self.magic = magic
        self.energy = energy

    def display(self):
        pokemon_dic = {
            'Name': self.name,
            'Health': self.health,
            'Level': self.level,
            'Power': self.power,
            'Magic': self.magic,
            'Energy': self.energy
        }

        for key, value in pokemon_dic.items():
            print(key, ' : ', value)

        print()


def main():
    bulbasaur = Pokemon('Bulbasaur', 100, 1, 1, 1, 1)

    bulbasaur.display()


if __name__ == '__main__':
    main()