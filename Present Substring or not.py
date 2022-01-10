# Program to check whether a substring is present or not in a given string.

# for time being direct input
para = input('Enter the string: ')
substring = input('Enter the substring to search')

if substring in para:
    print('Substring \"{}\" is present at {}'.format(substring, para.index(substring)))
else:
    print('Substring \"{}\" is not present in the string'.format(substring))
