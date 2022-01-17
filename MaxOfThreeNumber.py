# Write a program to find the largest number among three number without using in-built function.
a = int(input('Enter 1st no.: '))
b = int(input('Enter 2nd no.: '))
c = int(input('Enter 3rd no.: '))

if a > b:
    if a > c:
        print(a, ' is the largest number')
    else:
        print(c, ' is the largest number')
else:
    if b > c:
        print(b, ' is the largest number')
    else:
        print(c, ' is the largest number')


# One line code using in-built function
print('The largest number is:', max(a, max(b, c)))
