# WAP to modify the name as signature (follows):
# Input - Prakash chandra mohapatra
# Output - P.C.Mohapatra
name = input('Enter the name: ')
list_name = name.split()
signature = ''
for index in range(0, len(list_name)):
    word = list_name[index].capitalize()        # capitalize each words in the name(string)
    if index < len(list_name) - 1:              # for all indexes except last one
        first_letter = word[0]                  # first letter is stored
        signature += first_letter + '.'
    else:                                       # for last word
        signature += word

print(signature)
