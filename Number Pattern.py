# Program to print number pattern. Consider n = 5
# Pattern 1
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5

n = 5   # you can take user input also
print('Pattern 1\n')
for row in range(n):
    for col in range(1, n + 1):
        print(col, end=' ')
    print()

# Pattern 2
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5

print('\nPattern 2\n')
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=' ')
    print()


# Pattern 3
#   1 2 3 4 5
#   1 2 3 4
#   1 2 3
#   1 2
#   1

print('\nPattern 3\n')
for row in range(n, 0, -1):
    for col in range(1, row + 1):
        print(col, end=' ')
    print()


# Pattern 4
#   1
#   2 2
#   3 3 3
#   4 4 4 4
#   5 5 5 5 5

print('\nPattern 4\n')
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(row, end=' ')
    print()


# Pattern 5
#   5 5 5 5 5
#   4 4 4 4
#   3 3 3
#   2 2
#   1

print('\nPattern 5\n')
for row in range(n, 0, -1):
    for col in range(1, row + 1):
        print(row, end=' ')
    print()
