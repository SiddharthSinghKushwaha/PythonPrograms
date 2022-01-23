# Write a program to remove duplicate characters in the given string.
str = input('Enter a string to remove duplicate characters: ')
rem_str = ''
for ch in str:
    if ch not in rem_str:
        rem_str += ch

print('After removing duplicate character, string = ', rem_str)
