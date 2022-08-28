"""
Pokemon Fight Game by Jocelyn, Anita, Joshua, Junyu, Lily

2022-05-01
"""
# import needed modules for Pokemon Platform
import random
import time

# a class to create Pokemon heros


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

    def attack(self):
        return random.randint(1, 10)

    def rps(self):
        rps_list = ["Rock", "Paper", "Scissors"]

        return random.choice(rps_list)


def stadium(pokemon_1, pokemon_2):
    if pokemon_1.health > 0 and pokemon_2.health > 0:
        print("Action, start to fight ~")

        while True:
            attack_1 = pokemon_1.attack()
            attack_2 = pokemon_2.attack()

            print(pokemon_1.name + "_" + str(pokemon_1.health)
                  + " --- " + str(attack_1) + " ---> "
                  + pokemon_2.name + "_" + str(pokemon_2.health))
            pokemon_2.health = pokemon_2.health - attack_1

            if pokemon_2.health <= 0:
                print(pokemon_1.name + " wins this fight.")
                break

            time.sleep(0.5)

            print(pokemon_1.name + "_" + str(pokemon_1.health)
                  + " <--- " + str(attack_2) + " --- "
                  + pokemon_2.name + "_" + str(pokemon_2.health))
            pokemon_1.health = pokemon_1.health - attack_2

            if pokemon_1.health <= 0:
                print(pokemon_2.name + " wins this fight.")
                break

            time.sleep(0.5)


def race_game(p1, p2, r):
    p1_movelist = []

    for x in range(r):
        p1_movelist.append(random.randint(1, 10))

    # print(p1_movelist)

    print("|", end="")

    for x in range(r):
        time.sleep(0.5)
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
        time.sleep(0.5)
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


def main():
    eevee = Pokemon("eevee", 100, 5, 10, 8, 15)
    ditto = Pokemon("ditto", 100, 3, 6, 7, 12)

    # eevee.display()
    # ditto.display()

    choice = True

    while choice:
        print("""
                1. Display your choice
                2. Fight
                3. Race
                4. Exit(Quit)
        """)

        choice = input("What is your choice for your Pokemon: ")

        if choice == "1":
            eevee.display()
            ditto.display()

        elif choice == "2":
            # print("fight")
            #stadium(eevee, ditto)

            while True:
                rps_1 = eevee.rps()
                rps_2 = ditto.rps()

                if rps_1 == rps_2:
                    print("It is a tie")
                    continue
                elif rps_1 == "Rock":
                    if rps_2 == "Paper":
                        stadium(ditto, eevee)
                        break
                    else:
                        stadium(eevee, ditto)
                        break
                elif rps_1 == "Paper":
                    if rps_2 == "Scissors":
                        stadium(ditto, eevee)
                        break
                    else:
                        stadium(eevee, ditto)
                        break
                elif rps_1 == "Scissors":
                    if rps_2 == "Rock":
                        stadium(ditto, eevee)
                        break
                    else:
                        stadium(eevee, ditto)
                        break
                else:
                    print("No fight ~ ")

        elif choice == "3":
            race_game(ditto, eevee, 10)

        elif choice == "4":
            print("See you ~")
            choice = False

        else:
            print("Not valid choice.")


if __name__ == "__main__":
    main()


