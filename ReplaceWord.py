# WAP to replace a word with a searched word if found otherwise print "Can't replace because searched word not found".
# Input- Python is good for AI
# Search word- good
# Replace word- best
# Output- Python is best for AI

sentence = input('Enter a line of text: ')
search_word = input('Enter search word: ')
replace_word = input('Enter replace word: ')
# method 1
index = sentence.find(search_word)
if index != -1:
    sentence = sentence.replace(search_word, replace_word)
    print(sentence)
else:
    print('can not replace because searched not found')
