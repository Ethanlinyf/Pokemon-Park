'''
Something Good as indicated by ...

'''
import random


def welcome_message():  # Welcome message
    print("Welcome to this sorting algorithm")


def create_a_random_list(n):
    arr = []

    for i in range(n):
        arr.append(random.randint(1, 100))

    return arr


def babble_sorting(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


def main():
    welcome_message()
    arr = create_a_random_list(5)
    print(arr)

    babble_sorting(arr)


if __name__ == "__main__":
    main()
