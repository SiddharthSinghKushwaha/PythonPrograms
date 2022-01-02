# Program to print Grade of a student
# You can take input from user also. I have given direct value.

marks = 90

if marks > 90:
    print('Grade is A++')
elif 80 < marks <= 90:
    print('Grade is A')
elif 70 < marks <= 80:
    print('Grade is B++')
elif 60 < marks <= 70:
    print('Grade is B')
elif 50 < marks <= 60:
    print("Grade is C++")
elif 40 < marks <= 50:
    print('Grade is C')
else:
    print('Grade is F')
