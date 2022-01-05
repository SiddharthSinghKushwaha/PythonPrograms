# Write a program to show the use of built-in methods used in List and Tuples.
# First In-built methods used in the List

name_list = ['Siddharth', 'Sonali', 'Prakash', 'are', 'friends']
print('DataType of name_list is ', type(name_list), '\nList = ', name_list)

# 1. append(): Adds an element at the end of the list
name_list.append('forever')
print(name_list)

# 2. clear(): Removes all the elements from the list
name_list.clear()
print('In future, your friend list', name_list)

# 3. copy(): Returns a copy of the list
school_friends = ['Ansaf', 'Aman', 'Siddharth', 'Jeetan', 'Deepak']
name_list = school_friends.copy()
print(name_list)

# 4. count(): Returns the number of elements with the specified value
print(name_list.count('Aman'))

# 5. extend(): Add the elements of a list (or any iterable), to the end of the current list
friends = []    # empty list
college_friends = ['Prakash', 'Sonali', 'Rashmi']
friends.extend(college_friends)
friends.extend(school_friends)
print(friends)

# 6. index(): Returns the index of the first element with the specified value
print('Index of Ansaf in friends group: ', friends.index('Ansaf'))
print('Index of Ansaf in school group: ', school_friends.index('Ansaf'))

# 7. insert(): Adds an element at the specified position
school_friends.insert(4, 'Debashish')
print(school_friends)

# 8. pop(): Removes the element at the specified position
college_friends.pop(2)
print(college_friends, 'after 3 years')

# 9. remove(): Removes the first item with the specified value
friends.remove('Deepak')
print(friends)

# 10. reverse(): Reverses the order of the list
friends.reverse()
print(friends)

# 11. sort(): Sorts the list
friends.sort()
print(friends)

# Second, In-built function used in Tuple
# 1. count(): Returns the number of times a specified value occurs in a tuple
color_tuple = ('Red', 'Orange', 'Blue', 'Black', 'Purple')
print('\n\nDatatype of color_tuple is ', type(color_tuple), '\nTuple is: ', color_tuple)

# 2. index(): Searches the tuple for a specified value and returns the position of where it was found
print(color_tuple.index('Blue'))
