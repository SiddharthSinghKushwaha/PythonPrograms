# Program to search an element using Monte Carlo method
import random
array = [1, 7, 4, 9, 2, 8, 0]
c = 1
key = int(input('Enter a number to search: '))
k_times = int(input('Enter how many times you want to run: '))
while k_times:
    r = random.randint(0, len(array) - 1)
    if array[r] == key:
        print('Try {}: Element found'.format(c))
        break
    else:
        print('Try {}: Not found'.format(c))
    k_times -= 1
    c += 1
