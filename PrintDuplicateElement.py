# Program to print only duplicate elements in the list.
n = int(input('Enter the list of number: '))
number = []
print('Start Entering number')
for index in range(n):
    ele = int(input())
    number.append(ele)

unique_number = []
duplicate_number = []

for i in range(len(number)):
    if number[i] not in unique_number:
        unique_number.append(number[i])
    elif number[i] not in duplicate_number:
        duplicate_number.append(number[i])

print('Duplicate numbers are', duplicate_number)
