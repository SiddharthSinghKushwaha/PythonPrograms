# Program to print FACTORIAL of a number
# Factorial of a number is equals to multiplication from that number to 1.
# For example: 5! = 5 X 4 X 3 X 2 X 1 = 120

num = int(input('Enter a number: '))

if num < 0:                              # case 1: If input number is negative
    print('Invalid input. Factorial of Negative number is not defined.')
elif num == 0 or num == 1:              # case 2: If input number is 0 or 1
    print('The factorial of ', num, ' is 1')
else:
    print(num, '! = ', end=" ")
    factorial = 1
    for i in range(num, 0, -1):
        factorial *= i
        print(i, 'X', end=" ")
    print('\b\b\b = ', factorial)
