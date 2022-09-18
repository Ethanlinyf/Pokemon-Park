from g_swap import swap


def bubble_sorting(arr):
    n = len(arr)

    while n > 1:
        i = 1
    
        while i < n:
            if arr[i] < arr[i-1]:
                swap(arr, i, i-1)
            i += 1

        n -= 1
    
    return arr