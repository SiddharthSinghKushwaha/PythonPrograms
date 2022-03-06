# Program to implement Rabin-Karp Algorithm (PatternMatchingAlgo).

import random

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
string = '876552458'
pattern = '55'
found = False


# let generate random prime number
def generatePrime():
    index = random.randint(0, len(prime))
    return prime[index]


print('Pattern is ', pattern)
p = generatePrime()
print('Prime Number is:', p)
hc_pat = int(pattern) % p
print('Hash Value of Pattern = ', hc_pat)


def hc_sub_str(strX):
    return int(strX) % p


print()

# for loop to iterate through string
for i in range(0, len(string) - len(pattern) + 1):
    check = False
    sub_str = string[i: (i + len(pattern))]
    if hc_sub_str(sub_str) == hc_pat:
        found, check = True, True

    if check:
        print('Hash Value of Sub_String {} = {}'.format(sub_str, hc_sub_str(sub_str)))

        # using for loop to match character by character
        exact = True
        for index in range(0, len(pattern)):
            if sub_str[index] != pattern[index] and exact:
                print('Spurious Hit\n')
                exact = False

        if exact:
            print('Exact Match\n')

        # Instead of writting the loop, we can do the below
        # if sub_str == pattern:
        #    print('Exact Match\n')
        # else:
        #    print('Spurious Hit\n')

if not found:
    print('Pattern Not Found')
