# Program to search an element using Les Vegas method

import random
array = [1, 7, 4, 9, 2, 8, 0]
c = 1
key = int(input('Enter a number to search: '))
while True:
    r = random.randint(0, len(array) - 1)
    if array[r] == key:
        print('Try {}: Element found'.format(c))
        break
    else:
        print('Try {}: Not found'.format(c))
    c += 1
