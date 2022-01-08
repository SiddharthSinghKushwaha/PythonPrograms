# Program to print Percentage and Grade of a student of N subjects using List.
marks_list = []
n = int(input('Enter the number of Subjects: '))
sum, invalid_mark = 0, False
marks_scored = 0
for i in range(0, n):
    mark = int(input('Enter marks: '))
    marks_list.append(mark)
    marks_scored += marks_list[i]
    if marks_list[i] > 100:
        invalid_mark = True

# check if user has input marks greater than 100
if invalid_mark:
    print('Invalid mark')
else:
    # marks_scored = int(m1) + int(m2) + int(m3) + int(m4) + int(m5)
    total_mark = 500
    percentage = (marks_scored / total_mark) * 100
    print("Percentage: ", percentage)

    if percentage > 90:
        print('Grade is A++')
    elif 80 < percentage <= 90:
        print('Grade is A')
    elif 70 < percentage <= 80:
        print('Grade is B++')
    elif 60 < percentage <= 70:
        print('Grade is B')
    elif 50 < percentage <= 60:
        print("Grade is C++")
    elif 40 < percentage <= 50:
        print('Grade is C')
    else:
        print('Grade is F')
