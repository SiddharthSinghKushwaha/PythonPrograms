# WAP to print vowels first, then consonants in a string
str = input('Enter a string: ')
vowel = 'aeiouAEIOU'
v = c = ''
for ch in str:
    if ch in vowel:
        v += ch
    else:
        c += ch

print('Modified string (vowels first then consonants)', v + c)
