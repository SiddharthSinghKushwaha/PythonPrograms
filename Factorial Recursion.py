# Program to Find Factorial of Number Using Recursion

# defining a factorial function
def factorial_rec(n):
    if n in [0, 1]:
        return 1
    return n * factorial_rec(n-1)


# server - function called from here
num = int(input('Enter a number to find the factorial: '))
print('The factorial of', num, 'is', factorial_rec(num))
