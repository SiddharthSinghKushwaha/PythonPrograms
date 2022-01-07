# Write a program to check whether a number is prime or not.
# A number is said to be prime number if that number has only two divisor: 1 and number itself.

number = int(input('Enter a number: '))
no_of_divisor = 2
prime_number = True
for i in range(2, number//2 + 1):
    if number % i == 0:
        prime_number = False

if prime_number:
    print('The number ', number, ' is a Prime number')
else:
    print('The number ', number, ' is not prime number')
