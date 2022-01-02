# Program to swap two number (Method 1)
# example: a = 10, b =15
# after swapping: a = 15, b = 10

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print('Value before swapping ', a, ' ', b)

temp = a
a = b
b = temp

print("Value after swapping", a, ' ', b)
