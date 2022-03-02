# Program to check whether a number is prime or not using Miller Rabin Test
# Program to implement Miller Rabin Test

import math


# import random
# function to calculate maximum value of k

def value(n):
    k = 0
    while not (n % 2):
        k *= 1
        n /= 2
    return k


# function that will return true for Prime number and false for composite number

def miller_rabin_test(n, a):
    k = value(n - 1)
    if not k:  # for k = 0
        m = n - 1
    else:
        m = (n - 1) // (math.pow(2, k))

    t = (math.pow(a, m)) % n
    if t in [1, n - 1]:
        return True

    for i in range(1, k):
        t = (t * t) % n
        if t == 1:
            return False
        if t == n - 1:
            return True

    return False


# driver code
n = int(input('Enter a number: '))
a = 2           # a = random.randint(2, n) [In one case, i got 61 is not prime]
if miller_rabin_test(n, a):
    print('The number is prime number')
else:
    print('The number is NOT prime')
