'''
Something Good as Indicated by Joshua, Junhao, Junyu, Jason and Colin

'''
import random


def welcome_message():
    print("Welcome to this sorting algorithm")


def create_a_random_list(n):
    arr = []

    for i in range(n):
        arr.append(random.randint(1, 100))

    return arr


def babble_sorting(arr):
    lenth = len(arr)

    for i in range(lenth):
        for j in range(0, lenth-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def main():
    welcome_message()

    arr = create_a_random_list(100)

    print(arr)

    sorted_arr = babble_sorting(arr)

    print(sorted_arr)


if __name__ == "__main__":
    main()
