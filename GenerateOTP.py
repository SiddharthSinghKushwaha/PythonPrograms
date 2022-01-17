# WAP to generate OTP (One Time Code) of 4-digit number only.
import random
otp = ''
# n = int(input('Enter how many digits OTP you want to generate? (4/6/8): '))
# for this program, take n = 4
n = 4
for num in range(n):
    ele = random.randint(0, 9)
    otp = otp + str(ele)
print('OTP of 4-digit number is:', int(otp))

# way 2: in one line
print('OTP of 4-digit number is:', random.randint(10**(n-1), 10**n))

# You can also generate OTP of lower-case letters like 'afgy'
n = 4
otp_l = ''
lower_case = 'abcdefghijklmnopqrstuvwxyz'
for num in range(n):
    index = random.randint(0, 26)
    otp_l = otp_l + lower_case[index]
print('OTP of 4-letters is:', otp_l)
