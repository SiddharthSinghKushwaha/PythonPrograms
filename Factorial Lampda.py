# Calculate the factorial of a number using anonymous functions.
# anonymous function definition WAY -1
fact = lambda n: n * (n - 1)

num = int(input('Enter a number: '))
ans = 1
while num >= 2:
    ans *= fact(num)
    num -= 2
print('Factorial = ', ans)

# Way - 2
factorial = lambda n: 1 if n < 2 else n * factorial(n - 1)
print('Way2 Factorial =', factorial(int(input('Way2: Enter a number: '))))
