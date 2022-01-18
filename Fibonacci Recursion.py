# Program to Display Fibonacci Sequence Using Recursion

# defining a function
def fibo_rec(a, b, n):
    sum = a + b
    if sum > n:
        return 0
    print(sum, end=' ')
    return sum + fibo_rec(b, sum, n)


# server
n = int(input('Enter up to which you want Fibonacci series: '))
print('0 1', end=' ')
fibo_rec(0, 1, n)
