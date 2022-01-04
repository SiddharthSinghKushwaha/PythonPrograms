# Write a program to check whether a year is a Leap or not. [Hint: (1) If the year, when divided by 4 has no
# remainder and has remaindered when divided by 100, then it IS a leap year, (2) If the year, when divided by 400 has
# no remainder. ] 

year = int(input('Enter a year to check: '))

if year % 400 == 0:
    print(year, ' is a leap year')
elif year % 4 == 0 and year % 100 != 0:
    print(year, ' is a leap year')
else:
    print("Not a leap year")
