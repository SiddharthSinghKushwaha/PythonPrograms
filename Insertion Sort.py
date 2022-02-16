# WAP to sort an array using INSERTION sort.
array = [4, 7, 3, 9, 4, 2]

for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key

print(array)
