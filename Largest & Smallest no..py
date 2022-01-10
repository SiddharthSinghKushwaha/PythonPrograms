# Program to print the largest and the smallest number in a list.

numbers = []
size = int(input('Enter how many elements you want: '))
print('Start entering', size, ' numbers')
for n in range(0, size):
    numbers.append(int(input()))

min = max = numbers[0]
print("Numbers list =", numbers)
for i in range(0, size):
    if numbers[i] > max:
        max = numbers[i]
    if numbers[i] < min:
        min = numbers[i]

print("Maximum element in the list:", max)
print('Minimum elements in the list:', min)
