# Write a program to show the use of built-in methods used in dictionary.
number_dict = {1: 'One', 2: 'Two', 3: 'Three'}
print(type(number_dict), '\nDictionary: ', number_dict)

# 1. clear(): Removes all the elements from the dictionary
number_dict.clear()
print('After using clear(): Dict - ', number_dict)

# 2. copy(): Returns a copy of the dictionary
full_name = {'Sid': 'Singh', 'Ansaf': 'Khan', 'Prakash': 'Mohapatra'}
friends_dict = full_name.copy()
print(friends_dict)

# 3. fromkeys(): Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 1
new_dict = dict.fromkeys(x, y)
print(new_dict)

# 4. get(): Returns the value of the specified key
print(friends_dict.get('Sid'))

# 5. items(): Returns a list containing a tuple for each key value pair
surname_tuple = friends_dict.items()
print(surname_tuple)

friends_dict['Ansaf'] = 'Raja Khan'
print(surname_tuple)   # changes is also reflected into surname_tuple

# 6. keys(): Returns a list containing the dictionary's keys
key_list = friends_dict.keys()
print(key_list)

# 7. pop(): Removes the element with the specified key
friends_dict.pop('Sid')
print(friends_dict)

# 8. popitem(): Removes the last inserted key-value pair
print('Last pair deleted: ', friends_dict.popitem())

# 9. setdefault(): Returns the value of the specified key. If the key does not exist: insert the key,
# with the specified value
print(friends_dict.setdefault('Ansaf'))
friends_dict.setdefault('Sid', 'Singh')
print(friends_dict)

# 10. update(): Updates the dictionary with the specified key-value pairs
friends_dict.update({'Sonali': 'Palai', 'Prakash': 'Mohapatra'})
print(friends_dict)

# 11. values(): Returns a list of all the values in the dictionary
print(friends_dict.values())


