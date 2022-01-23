# WAP to check whether a string is a palindrome or not.
str = input('Enter a string: ')
rev_str = str[:: -1]
if str == rev_str:
    print('{} is a palindrome'.format(str))
else:
    print('The input string is not palindrome')


# another way to reverse a string
def reverse_str(str1):
    rev = ''
    for c in range(-1, -len(str1)-1, -1):
        rev += str1[c]

    return rev


# Driver code
if str == reverse_str(str):
    print('Palindrome')
else:
    print('Not Palindrome')
