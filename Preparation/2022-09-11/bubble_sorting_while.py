'''
Something Good as Indicated by Joshua, Junhao, Junyu, Jason and Colin

'''
import random


def welcome_message():
    print("Welcome to this bubble sorting algorithm implemented by using while loop")


def create_a_random_list(n):
    arr = []

    for i in range(n):
        arr.append(random.randint(1, 100))

    return arr


def swap(arr, i, j):
    # the following implement how to swap two elements:
    # arr[i], arr[j] = arr[j], arr[i]
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sorting_while(arr):
    n = len(arr)

    while n > 1:
        i = 1

        while i < n:
            if arr[i] < arr[i-1]:
                swap(arr, i, i-1)
            i += 1

        n -= 1 

    return arr


def main():
    welcome_message()

    arr = create_a_random_list(10)
    print(arr)

    sorted_arr = bubble_sorting_while(arr)
    print(sorted_arr)


if __name__ == "__main__":
    main()

main()
