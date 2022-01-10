# Program to check whether a number is armstrong or not.
# A number of 3-digits is said to be Armstrong if sum of the cube of digits is equals to the number itself.

number = int(input('Enter a number to check: '))
temp = number
sodc = 0        # sodc = sum of digits cube
while number > 0:
    rem = number % 10
    sodc += (rem * rem * rem)
    number //= 10

if sodc == temp:
    print('The number is ARMSTRONG number')
else:
    print('The number is not armstrong number')
