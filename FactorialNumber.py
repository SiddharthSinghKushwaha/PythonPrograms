# Program to print FACTORIAL of a number

# Factorial of a number is equals to multiplication of from that number to 1.
# For example: 5! = 5 X 4 X 3 X 2 X 1
# 5! = 120

num = int(input('Enter a number: '))

factorial = 1
# if range[end]: 0 to end-1
for i in range(1, num + 1):       # range [start, end]: start to end-1
    factorial *= i

print('The factorial of ', num, ' is ', factorial)
