# Program to check whether a number is prime or not.
# Program to implement Fermat Test.
import math
import random

number = int(input('Enter a number to check for Prime: '))
a = random.randint(2, number)
if (int(math.pow(a, (number - 1))) % number) == 1:
    print('The {} is a prime number'.format(number))
else:
    print('Not Prime')
