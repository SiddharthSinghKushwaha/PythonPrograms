# WAP to sort an array using BUBBLE sort.
array = [7, 4, 2, 1, 4, 6, 3]
# Bubble sort code
size = len(array)
for i in range(size):
    exchange = 0
    for j in range(size - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            exchange += 1

    if not exchange:
        break
print('The sorted array is', array)
