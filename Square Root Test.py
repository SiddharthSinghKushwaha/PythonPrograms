# Program to check for prime number using Square Root Rest.
# Program to implement Square Root Test.
n = int(input('Enter a number: '))
is_prime = True
for x in range(2, (n//2) + 1):
    if ((x * x) % n) == 1:
        print('{} mod {} = {}'.format((x*x), n, (x * x) % n))
        is_prime = False
        break

if is_prime:
    print('The number is prime')
else:
    print('The number is NOT prime')

# Numbers like 4, 6, 10, 14, 18, 22 and many more, satisfy the
# "Square Root Test" but they are composite numbers.
