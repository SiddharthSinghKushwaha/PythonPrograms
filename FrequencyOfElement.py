# WAP to print the frequency of each element present in the list.
# Taking input from the uesr
n = int(input('Enter the list of number: '))
number = []
print('Start Entering number')
for index in range(n):
    ele = int(input())
    number.append(ele)

# Removing repeated element
unique_number = []

for i in range(len(number)):
    if number[i] not in unique_number:
        unique_number.append(number[i])

# calculating the frequency
print('Number\tFrequency')
for i in range(len(unique_number)):
    count = 0
    num = unique_number[i]
    for j in range(len(number)):
        if num == number[j]:
            count += 1
    print('{}\t\t{}'.format(num, count))
