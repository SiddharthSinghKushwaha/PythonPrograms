# A number is said to be Perfect number if the sum of all the divisor is equals to that number
# Example: Divisor is 6 are 1, 2, and 3. Sum of them: 1 + 2 + 3 = 6 (which is equals to that number)
# so, 6 is a perfect number

num = int(input('Enter a number: '))
Sum = 1
for i in range(2, 6):
    if num % i == 0:
        Sum += i

if Sum == num:
    print('The number', num, ' is perfect number')
else:
    print('Not a perfect number')
