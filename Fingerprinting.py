# Program to check for strings equality (Fingerprinting).

import random

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
strX = '26'     # provide user defined value if you want to.
strY = '26'
check = True


# let generate random prime number
def generatePrime():
    index = random.randint(0, len(prime))
    return prime[index]


p = generatePrime()


def hcX():
    return int(strX) % p


def hcY():
    return int(strY) % p


if hcX() != hcY():
    print('String are not equals')
    check = False

k = 2  # Manto Carlo algorithm
while k and check:
    p = generatePrime()
    print(p)
    if hcX() != hcY():
        print('String are not equals')
        check = False
    k -= 1

if check:
    print('String are equals')
