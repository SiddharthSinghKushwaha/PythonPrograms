# Program to find Sum of first N natural number using for loop
# (Method 1): Using for loop
# (Method 2): Direct formula n*(n+1)/2

N = int(input('Enter the value of n: '))
Sum = 0
for i in range(1, N+1):
    Sum += i

print('Sum of first ', N, ' natural number is ', Sum)
