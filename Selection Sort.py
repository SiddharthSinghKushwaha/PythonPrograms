# WAP to sort an array using SELECTION sort.
array = [7, 5, 3, 1]

for i in range(len(array) - 1):
    min = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min]:
            min = j
    if min is not i:
        array[i], array[min] = array[min], array[i]

print(array)
