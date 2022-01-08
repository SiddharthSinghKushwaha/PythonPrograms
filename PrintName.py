# Write a program to print your name, character by character.
name = input('Enter your name: ')

# way 1
for i in name:
    print(i, end=',')
print("\b")

# way2 using range
for j in range(0, len(name)):
    print(name[j], end=',')
print('\b')


# way3 using negative indexes
for k in range(-len(name), 0):
    print(name[k], end=" ")
