# WAP to generate strong password of 8-alphanumerical.
# A password is said be strong if it has at least one Lower case, one Upper case, one special character, and one digit.
import random as r
lop = 8     # you can take user input also      lop = length of password
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_symbol = '!@#$%^&*'
digits = '0123456789'
alphanumerical = lower_case + upper_case + special_symbol + digits
password = lower_case[r.randint(0, 25)] + upper_case[r.randint(0, 25)] + special_symbol[r.randint(0, 7)] + \
    digits[r.randint(0, 9)]
for i in range(4):
    index = r.randint(0, 69)
    password += alphanumerical[index]

print('Your Strong password is:', password)
