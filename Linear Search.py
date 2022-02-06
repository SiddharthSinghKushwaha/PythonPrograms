# Write a program to search an element in a list using Linear Search.
numbers = [2, 5, 1, 9, 4]
search_ele = int(input('Enter a element to search: '))

# In linear search, we simply traverse each element in the list and check whether it is equal or not.
found = False
for element in numbers:
    if search_ele == element:
        print('Search Element Found at index ', numbers.index(element))
        found = True
        break

if not found:
    print('Element Not Found')
