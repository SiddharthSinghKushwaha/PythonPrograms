# Write a program to show DataType conversion of following (in single program)
# int(), float(), str(), tuple(), list(), set(), dict(), chr(), hex(), oct()

string = '342'          # You can  'string' & 'real number' datatype only, here
convert_to_int = int(string)
print('1. int() ', convert_to_int)

convert_to_float = float(string)
print("2. float() ", convert_to_float)

num_set = (2, 4, 5, 6, 7)   # You can use any datatypes, here
convert_to_str = str(num_set)
print("3. str() ", convert_to_str)

String = "Tuple"             # used only those object which are iterable like string, list, dictionary
convert_to_tuple = tuple(String)
print("4. tuple() ", convert_to_tuple)  # In case of dict, only key will be stored in tuple

convert_to_list = list(String)
print("5. list() ", convert_to_list)  # In case of dict, only key will be stored in list

convert_to_set = set(String)
print("6. set() ", convert_to_set)  # In case of dict, only key will be stored in set

example = {1: 'one', 2: 'two'}
convert_to_dict = dict(example)
print("7. dict() ", convert_to_dict)  # In case of dict, only key will be stored in tuple

ascii_value = 99           # use only integer values
convert_to_char = chr(ascii_value)
print("8. chr()", convert_to_char)

value = 10
convert_to_hexa = hex(value)
print('9. hex()', convert_to_hexa)

convert_to_oct = oct(value)
print('10. oct()', convert_to_oct)
