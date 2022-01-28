# WAP to print the input word (String) in alphabetical order. For example,
# Input: sonali (ignore uppercase & lowercase conflict)
# Output- ailnos
word = input('Enter a string: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    for ch in word:
        if ch == letter:
            print(ch, end="")
