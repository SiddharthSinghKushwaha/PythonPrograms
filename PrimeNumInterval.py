# WAP to print all the prime numbers between given intervals as input from the user.

start = int(input('Enter Starting interval: '))
end = int(input('Enter Ending interval: '))
print('Prime number between {} and {} are: '.format(start, end))
for j in range(start, end + 1):
    number = j
    no_of_divisor = 2
    prime_number = True
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            prime_number = False

    if prime_number:
        print(number, end=' ')
