# WAP to accept a line of text from the user and modify it such that the last word comes to the first position.
# For example Input- It does not make sense
# Output-  sense It does not make

sentence = input('Enter line of text: ')

# Method 1
index_last_space = sentence.rfind(' ')  # rfind(ele) - search the ele from backwards and returns its index
last_word = sentence[index_last_space + 1:]  # store the last word
without_last_word = sentence[: index_last_space + 1]  # store the sentences without last word
ans = last_word + ' ' + without_last_word
print('Method 1:', ans)

# Method 2
list_sentence = sentence.rsplit(' ', 1)  # list that contains only 2 words
last_word2 = list_sentence[1]
without_last_word2 = list_sentence[0]
ans2 = last_word2 + ' ' + without_last_word2
print('Method 2:', ans2)
