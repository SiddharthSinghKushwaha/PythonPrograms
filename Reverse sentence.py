# WAP to accept a line of text (string) and create a new string that stores the original string in reverse wordwise.
# For example, Input- This is python programming
# Output- programming python is This

# Method 1
sentence = input('Enter the line of text: ')
reverse_sentence = sentence[:: -1]
list_sentence = reverse_sentence.split()
ans_str = ""
for word in list_sentence:
    reverse = word[:: -1]
    ans_str += reverse + ' '

print(ans_str.strip())  # strip() will remove all the spaces before and after str

# Method 2
list_sentence2 = sentence.split()
ans_str2 = ""
for i in range(len(list_sentence2) - 1, -1, -1):
    ans_str2 += list_sentence2[i] + " "

print(ans_str2.strip())
