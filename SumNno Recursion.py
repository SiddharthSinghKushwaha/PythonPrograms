# Program to find the sum of the first N natural number using recursion.

# defining the function
def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n-1)


# calling the function
n = int(input('Enter value of N: '))
print('Sum of first', n, ' Natural number is', sum_rec(n))
