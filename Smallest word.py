# WAP to print the smallest word present in the line of text (String). For example,
# Input- My name was Siddharth
# Output- My

sentence = input('Enter line of text: ')
list_sentence = sentence.split()
min_length = len(list_sentence[0])
smallest_word = list_sentence[0]

for word in list_sentence:
    if len(word) < min_length:
        min_length = len(word)
        smallest_word = word

print('The longest word is:', smallest_word)
print(max('my', 'is'))
