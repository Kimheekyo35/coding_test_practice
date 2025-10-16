input_str = input()
command_list = list(map(str,input()))

for c in command_list:
    if c == 'L':
        input_str = input_str[1:] + input_str[0]
    else:
        input_str = input_str[-1] + input_str[:-1]
    
print(input_str)