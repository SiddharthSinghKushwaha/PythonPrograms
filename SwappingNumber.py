# Program to swap two number (Method 1)
# example: a = 10, b =15
# after swapping: a = 15, b = 10

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# done using an extra variable 'temp' METHOD 1
print("METHOD 1")
print('Value before swapping ', a, ' ', b)

temp = a
a = b
b = temp

print("Value after swapping", a, ' ', b)

# using no extra variable METHOD 2
a, b = 40, 50
print("\nMethod 2")
print('Value before swapping ', a, ' ', b)

a = a + b
b = a - b
a = a - b

print("Value after swapping", a, ' ', b)