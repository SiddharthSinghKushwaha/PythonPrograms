# A number is said to be Palindrome if reverse of the number is equals to itself.
# Example: 343 is a palindrome while 234 is not. Reverse of 234 is 432 (clearly they aren't equal)

num = int(input('Enter a number '))
temp = num
rev = 0
while num > 0:
    d = int(num % 10)
    rev = rev * 10 + d
    num = int(num/10)

if rev == temp:
    print(temp, ' is a palindrome number')
else:
    print(temp, " is not palindrome")
