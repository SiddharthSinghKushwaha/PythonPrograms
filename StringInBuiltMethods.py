# Write a program to show the use of different In-Built methods/Functions used in String

# 1. capitalize(): Converts the first/initial character to upper case.
name = 'siddharth singh'
name_changed = name.capitalize()
print(name_changed)

# 2. casefold(): Converts the entire string to lowercase.
last_name = "KUSHWAHA"
last_name_change = last_name.casefold()
print(last_name_change)

# 3. center(): Returns a centered string
text = 'python'
text_centered = text.center(10)
print(text_centered)
text_centered = text.center(10, '*')
print(text_centered)

# 4. count(): Returns the number of times a substring occurs in the given string.
message = 'I am learning python. You should also learn python.'
no_of_times = message.count('python')
print(no_of_times)

# 5. encode(): Converts the string into its encoded version.
message_encoded = message.encode()
print(message_encoded)

# 6. endswith(): Returns true if the given string ends with the specified substring otherwise false
print(last_name.endswith('WAHA'))
print(last_name.endswith('waha'))  # this show that last_name was not modified

# 7. expandtabs(): Replaces the tab size to the given numeric character spaces. The default size is 8 character spaces.
full_name = "Siddharth\tSingh\tKushwaha"
full_name_change = full_name.expandtabs(2)
print(full_name_change)

# 8. find(): Searches the main string from the left for a specified substring and returns its position within a match
# is found; if not, return -1 when no match is found.
first_index = message.find('python')
print(first_index)

# 9. format(): Helps format the string by making use of placeholders.
x, y = 2, 3
print('Way1: Sum of {} and {} is {}'.format(x, y, x + y))
print('Way2: Sum of {0} and {1} is {2}'.format(x, y, x + y))
print('Way3: Sum of {one} and {two} is {three}'.format(two=x, one=y, three=x + y))

# 10. index(): Finds the position of occurrence of a substring by searching the main string for a specified substring
# and returns its position within a match is found, if not throws an error.
index = message.index('python')
print(index)

# 11. isalnum(): Determines if all the characters in a given string are alphanumeric, that is, only alphabets and
# numbers. In case there is a space in between, it returns false.
roll_no = 'BS18-031'     # return is false because '-' is present
print(roll_no.isalnum())

# 12. isalpha(): Determines if all the characters in the given string are alphabets.In case there is a space in
# between, it returns false.
print(message.isalpha())        # false because spaces are present
print(last_name.isalpha())

# 13. isdecimal(): Determines if all the characters in a given string are decimals.
# In case there is a space (special character) in between, it returns false.
mark = '90'
print(mark.isdecimal())

# 14. isidentifier(): Determines whether the string is a valid identifier or not.
# In case there is a space in between, it returns false.
print('Try1'.isidentifier())

# 15. islower(): Determines if all the characters in a given string are in lower case. If yes, then returns true,
# else returns false.
print('sidD'.islower())

# 16. isnumeric(): Determines if all the characters in a given string are numeric, that is, numbers and exponents
# that could be in fractions. If yes, then returns true, else return false.
print('1234'.isnumeric())

# 17. isprintable(): Determines if all the characters in a given string are printable or not.
# Characters such as “\t” or “\n” are not printable.
print('Siddharth\tSingh'.isprintable())

# 18. isspace(): Determines if all the characters in a given string are white spaces.
print("\n\n".isspace())

# 19. istitle(): Determines if a string follows a set of rules to qualify as a title.
print('nottitle'.istitle())     # if first letter is capital then true

# 20. isupper(): Determines if all the characters in a given string are in the upper case.
print(last_name.isupper())

# 21. join(): Meant to concatenate two strings in an iterated manner.
print("Siddharth".join("123"))
print("Sid".join('****'))

# 22. lower(): Meant to convert the entire string to lower case.
print(last_name.lower())

# 23. upper(): Meant to convert the entire string to the upper case.
print(full_name.upper())

# 24. replace(): Meant to replace a substring with another.
print("abcdef".replace("abc", 'sid'))