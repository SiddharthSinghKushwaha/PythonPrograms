# Program to perform an operation on two number. Give input: an operator (+, -, *, /) and two number.

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
operator = input('Enter an operator: ')

# operation is performed according to 'operator executed'

if operator == '+':
    print('Addition of ', num1, ' and ', num2, ' is ', num1 + num2)

if operator == '-':
    print('Subtraction of ', num1, ' and ', num2, ' is ', num1 - num2)

if operator == '*':
    print('Multiplication of ', num1, ' and ', num2, ' is ', num1 * num2)

if operator == '/':
    print('Division of ', num1, ' by ', num2, ' is ', num1 - num2)
