# Program to print multiplication table of any number.
num = int(input('Enter a number to find its multiplication: '))
for i in range(1, 11):
    print(num, 'X', i, '=', num * i)

# way 2: only different way of printing
print('\nWay 2\n')
for i in range(1, 11):
    print('{} X {} = {}'.format(num, i, num * i))
