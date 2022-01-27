# WAP to print the biggest word present in the line of text (string). For example,
# Input- My name is Siddharth
# Output- Siddharth

sentence = input('Enter line of text: ')
list_sentence = sentence.split()
max_length = 0
longest_word = ''

for word in list_sentence:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print('The longest word is:', longest_word)
