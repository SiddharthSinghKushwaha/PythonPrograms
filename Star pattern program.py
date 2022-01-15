# Print the star pattern program for n = 5
# Pattern 1
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = 5   # you can also take input from the user
print('Pattern 1\n')
for row in range(n):
    for col in range(n):
        print('*', end=' ')
    print()

# Pattern 2
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

print('\nPattern 2\n')
for row in range(n):
    for col in range(row + 1):
        print('*', end=' ')
    print()

# Pattern 3
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

print('\nPattern 3\n')
for row in range(n, 0, -1):
    for col in range(row):
        print('*', end=' ')
    print()

# Pattern 4
#   * * *
#   * * * * *
#   * * *
#   * * * * *
#   * * *

print('\nPattern 4\n')
for row in range(1, n + 1):
    if row % 2 != 0:
        print('* * *')
    else:
        print('* * * * *')
