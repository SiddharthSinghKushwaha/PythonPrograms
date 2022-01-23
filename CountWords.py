# Program to count number of words in a string and print them.
str = input('Enter a string: ')
list_str = str.split()
print('There are {} words and they are {}'.format(len(list_str), list_str))
