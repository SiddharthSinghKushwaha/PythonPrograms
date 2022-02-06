# Write a program to search an element in a list using Binary Search.
numbers = [1, 4, 7, 9, 14]  # We take sorted elements, always
search_ele = int(input('Enter a element to search: '))

# Without recursive
low, high = 0, len(numbers) - 1
found = False
while low <= high:
    mid = low + int((high - low) / 2)
    if numbers[mid] < search_ele:
        low = mid + 1
    elif numbers[mid] > search_ele:
        high = mid - 1
    else:
        print('Element is found at index ', mid)
        found = True
        break

if not found:
    print('Searched Element Not Found')


# function definition
def binary_Search(num, l, h, search):
    if l <= h:
        m = l + int((h - l) / 2)
        if num[m] < search:
            return binary_Search(num, m + 1, h, search)
        elif numbers[m] > search:
            return binary_Search(num, l, m - 1, search)
        else:
            return m
    return -1


# Using Recursion
index = binary_Search(numbers, 0, len(numbers), search_ele)
if index == -1:
    print('Element Not Found')
else:
    print('Element Found At index ', index)
