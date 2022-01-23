# WAP to modify the name as signature (follows):
# Input - Prakash chandra mohapatra
# Output - P.C.Mohapatra
name = input('Enter the name: ')
list_name = name.split()
signature = ''
for index in range(0, len(list_name)):
    word = list_name[index].capitalize()
    if index < len(list_name) - 1:
        first_letter = word[0]
        signature += first_letter + '.'
    else:
        signature += word

print(signature)
