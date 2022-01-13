# Program to remove repeated numbers in a list. Print the list with unique value.
# For example Input- [5, 7, 5, 3, 2, 2, 1, 9, 2, 9] Output: [5, 7, 3, 2, 1, 9]

n = int(input('Enter the list of number: '))
number = []
print('Start Entering number')
for index in range(n):
    ele = int(input())
    number.append(ele)

unique_number = []

for i in range(len(number)):
    if number[i] not in unique_number:
        unique_number.append(number[i])

print('After removing number for the list: ', unique_number)
