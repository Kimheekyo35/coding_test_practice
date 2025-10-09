input_str = input()
list_str = list(input_str)
list_str[1] = 'a'
list_str[-2] = 'a'

string = ''.join(list_str)

print(string)