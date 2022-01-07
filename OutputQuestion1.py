# Write a program to print odd number or even number between 25 and 50 (including both ends).
# Output should be like this:
# 25 is an odd number
# 26 is an even number
# ... 50 is an even number

num = 25
while num:
    if num == 51:
        break
    if num % 2 == 0:
        print(num, ' is an odd number')
    else:
        print(num, ' is an even number')
    num += 1
