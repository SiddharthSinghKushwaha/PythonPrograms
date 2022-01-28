# WAP to print the frequency of each character in a string (single word). For example,
# Input (only letters, ignore uppercase and lowercase)- madam
# Output-
# Character   Frequency
# m                 2
# a                 2
# d                 1

word = input('Enter a string: ')
unique = ''
# removing duplicate elements
for letter in word:
    if letter not in unique:
        unique += letter

# Method 1: frequency of each character
print('Characters\tFrequency')
for character in unique:
    count = 0
    for letter in word:
        if letter == character:
            count += 1
    print('{}\t\t\t{}'.format(character, count))

# Method 2 (Better)
print('Characters\tFrequency')
for character in unique:
    count2 = word.count(character)
    print('{}\t\t\t{}'.format(character, count2))
