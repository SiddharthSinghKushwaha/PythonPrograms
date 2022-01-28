# WAP to search a word in a string, accepted by the user. If the word is present then print YES along with its
# position otherwise display an appropriate message. Input- Python is good for AI.
# Search word- good
# Output- YES, the searched word is present at 11 positions. (10 index number)

sentence = input('Enter a line of text: ')
search_word = input('Enter search word: ')
# method 1
index = sentence.find(search_word)
if index != -1:
    print('Yes searched word is present at {} position'.format(index + 1))
else:
    print('No searched word not found')

# method 2
if search_word in sentence:
    print('Yes searched word is present at {} position'.format(sentence.find(search_word) + 1))
else:
    print('No searched word not found')
