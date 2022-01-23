# WAP to print the number of digits, lower case, upper case, spaces, special characters present in a given string.
str = input('Enter a string: ')
d = lc = uc = s = sc = 0
# digit(d), lower case(lc), upper case(uc), spaces(s), and special character(sc)
for c in str:
    if c.isdigit():
        d += 1
    elif c.islower():
        lc += 1
    elif c.isupper():
        uc += 1
    elif c.isspace():
        s += 1
    else:
        sc += 1

print('Number of digits: ', d)
print('Number of lower case: ', lc)
print('Number of upper case: ', uc)
print('Number of spaces: ', s)
print('Number of special characters: ', sc)
