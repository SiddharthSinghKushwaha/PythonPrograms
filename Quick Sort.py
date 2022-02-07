# WAP to sort an array (list) using Quick Sort.

# defining the 'quickSort' function
def quickSort(num_list, p, r):
    if p < r:
        q = partition(num_list, p, r)
        quickSort(num_list, p, q - 1)
        quickSort(num_list, q + 1, r)


# defining the 'partition' function
def partition(num_list, p, r):
    pivot = num_list[r]
    i = p - 1
    for j in range(p, r):
        if num_list[j] < pivot:
            i += 1
            num_list[i], num_list[j] = num_list[j], num_list[i]  # one line code to swap two values
    num_list[i + 1], num_list[r] = num_list[r], num_list[i + 1]
    return i + 1


# driver code
numbers = [3, 6, 4, 1, 2, 5, 8]
print('Before Sorting\nList = ', numbers)
quickSort(numbers, 0, (len(numbers) - 1))
print('After Sorting\nList = ', numbers)
