# WAP to store and print 10 random numbers in a list between 100 and 200.
import random
random_number = []
for i in range(10):
    ele = random.randint(100, 200)
    random_number.append(ele)

print('List of Random number:', random_number)

# way 2 to generate random number
print('Way 2 (One liner code to generate random: )', random.sample(range(100, 200), 10))
