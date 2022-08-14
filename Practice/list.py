'''
Create a list with 10 numbers

'''

import random

myList = []

for x in range(10):
    myList.append(random.randint(1, 100))

print(myList)