# WAP to print the number of vowels and consonants in a string
str = input('Enter a string: ')
vowel = 'aeiouAEIOU'
v = c = 0
for ch in str:
    if ch in vowel:
        v += 1
    else:
        c += 1

print('Number of vowels:', v)
print('Number of consonants:', c)
