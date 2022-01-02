# Program to print sum of digits of a number

num = int(input("Enter a number: "))
temp = num
sod = 0
while num > 0:
    d = int(num % 10)
    sod += d        # sod - sum of digits
    num = int(num / 10)

print("The sum of digits of", temp, " number is ", sod)
