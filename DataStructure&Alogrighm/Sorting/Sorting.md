# Introduction
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

## How does Bubble Sort Work?
- First Pass: 
Bubble sort starts with first two elements, comparing them to check which one is greater.
( **5 1** 4 2 8 ) –> ( **1 5** 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
( 1 **5 4** 2 8 ) –>  ( 1 **4 5** 2 8 ), Swap since 5 > 4 
( 1 4 **5 2** 8 ) –>  ( 1 4 **2 5** 8 ), Swap since 5 > 2 
( 1 4 2 **5 8** ) –> ( 1 4 2 **5 8** ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
- Second Pass: 
Now, during second iteration it should look like this:
( **1 4** 2 5 8 ) –> ( **1 4** 2 5 8 ) 
( 1 **4 2** 5 8 ) –> ( 1 **2 4** 5 8 ), Swap since 4 > 2 
( 1 2 **4 5** 8 ) –> ( 1 2 **4 5** 8 ) 
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 ) ? needed

- Third Pass: 
  Now, the array is already sorted, but our algorithm does not know if it is completed.
The algorithm needs one whole pass without any swap to know it is sorted.
( **1 2** 4 5 8 ) –> ( **1 2** 4 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
( 1 **2 4** 5 8 ) –> ( 1 **2 4** 5 8 ) 
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
- The Fouth Pass is needed? 
How to end this looping
- Demonstrate in a figure as follows:

![sorting](bubble-sort.png)

Follow the below steps to solve the problem:

- Run a nested for loop to traverse the input array using two variables i and j, such that 0 ≤ i < n-1 and 0 ≤ j < n-i-1
- If arr[j] is greater than arr[j+1] then swap these adjacent elements, else move on
- Print the sorted array

```python
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
 
# Driver code to test above
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]
 
  bubbleSort(arr)
 
  print("Sorted array is:")
  for i in range(len(arr)):
      print("%d" % arr[i], end="")

```

## How to implemente the babble sorting in Scratch 3?
https://www.youtube.com/watch?v=QdifzKfT9D4&ab_channel=DougHenry
