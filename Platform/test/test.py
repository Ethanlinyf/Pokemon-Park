def fibonacci(n):
    # initialize variables
    a, b = 0, 1
    # loop through n times
    for i in range(n):
        # print current value of a
        print(a)
        # update variables
        a, b = b, a + b

fibonacci(10)
