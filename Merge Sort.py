# WAP to sort an array (list) using MERGE Sort.
# Defining the 'merge' function
def merge(num_list, p, q, r):
    size1 = q - p + 1
    size2 = r - q
    left = [0] * size1
    right = [0] * size2
    for i in range(0, size1):
        left[i] = num_list[p + i]
    for j in range(0, size2):
        right[j] = num_list[q + 1 + j]

    i = j = 0
    k = p
    while i < size1 and j < size2:
        if left[i] <= right[j]:
            num_list[k] = left[i]
            i += 1
        else:
            num_list[k] = right[j]
            j += 1
        k += 1

    # while loops to store rest elements
    while i < size1:
        num_list[k] = left[i]
        i += 1
        k += 1

    while j < size2:
        num_list[k] = right[j]
        j += 1
        k += 1


# Defining the 'mergeSort' function
def mergeSort(list_num, p, r):
    if p < r:
        q = p + (r - p)//2
        mergeSort(list_num, p, q)
        mergeSort(list_num, q + 1, r)
        merge(list_num, p, q, r)


# driver code
numbers = [3, 6, 4, 1, 2, 5, 8]
size = len(numbers)
print('Before Sorting\nList = ', numbers)
mergeSort(numbers, 0, size - 1)
print('After Sorting\nList = ', numbers)
