'''
Something Good as Indicated by Joshua, Junhao, Junyu, Jason and Colin

'''

from pp_welcome import welcome_message
from pp_class import Pokemon
from pp_race_game import race_game
from pp_bubble_sorting import * 
from matplotlib import pyplot as plt

def main():
    welcome_message()

    eevee = Pokemon("Eevee", 8, 100, 6, 20, 10)
    ditto = Pokemon("Ditto", 6, 100, 12, 15, 12)

    race_results = []

    for i in range(7):
        race_results.append(race_game(eevee, ditto, 10))

    print(race_results)

    race_results_sorted = bubble_sorting(race_results)

    print(race_results_sorted)

    plt.bar(range(7), race_results_sorted)
    plt.show()


if __name__ == "__main__":
    main()
