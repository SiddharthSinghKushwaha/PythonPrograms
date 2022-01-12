# WAP to print the ASCII value of characters present in the string.
string = input('Enter a sentence: ')

for letter in string:
    ascii_value = ord(letter)
    print('ASCII value of {} is {}'.format(letter, ascii_value))

# ord() - gives the ASCII value of the character passed in it
# ASCII - American Standard Code For Information Interchange
