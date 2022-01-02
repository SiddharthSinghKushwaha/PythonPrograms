# Program to check whether a number is even or not

# First take input from number and convert it into "int" type because
# the default return of input function is "String type."

num = int(input('Enter a number to check for even: '))
if num % 2 == 0:
    print("The number ", num, " is even")
else:
    print('The number is odd number')
