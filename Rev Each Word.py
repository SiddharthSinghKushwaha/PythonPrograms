# WAP to reverse each word in the string (line of text).
# Input- This is python programming
# Output- sihT si nohtyp gnimmargorp

sentence = input('Enter the line of text: ')
list_sentence = sentence.split()
ans_str = ""
for word in list_sentence:
    reverse = word[:: -1]
    ans_str += reverse + ' '

print(ans_str.strip())  # strip() will remove all the spaces before and after str
