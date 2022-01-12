# WAP to store and print 10 random numbers in a list between 100 and 200.
import random
random_number = []
for i in range(10):
    ele = random.randint(100, 200)
    random_number.append(ele)

print('List of Random number:', random_number)
