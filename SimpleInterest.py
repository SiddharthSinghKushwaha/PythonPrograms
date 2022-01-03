# Program to input principal, time, and rate (P, T, R) from the user and find Simple Interest

principal = float(input('Enter the principal amount: '))
time = int(input('Enter number of year: '))
rate = float(input('Enter the rate of interest: '))

simple_interest = (principal * time * rate)/100
print('The Simple Interest for the entered details: ', simple_interest)
