# WAP to accept a line of text (String) from the user and modify it such that the first word and the last word will
# be interchanged. For example Input- It does not make sense
# Output- sense does not make it

sentence = input('Enter line of text: ')

# Method 1
first_index = sentence.find(' ')  # index of first occurrence of space
last_index = sentence.rfind(' ')  # index of last occurrence of space
first_word = sentence[: first_index]  # store the first word
last_word = sentence[last_index + 1:]  # store the last word
rest_words = sentence[first_index + 1: last_index]  # sentences without last word amd first word
ans = last_word + ' ' + rest_words + ' ' + first_word
print(ans)

# Method 2
# example- It does not make sense
list1 = sentence.rsplit(' ', 1)  # ['It does not make', 'sense']
last_word2 = list1[1]   # sense
rest_list1 = list1[0]   # It does not make

list2 = rest_list1.split(' ', 1)  # ['It', 'does not make']
first_word2 = list2[0]  # It
middle_word = list2[1]  # does not make
ans2 = last_word2 + ' ' + middle_word + ' ' + first_word2
print(ans2)
