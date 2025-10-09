input_str = input()
list_re = []
for elem in input_str:
    if elem == input_str[1]: 
        elem = input_str[0]
        list_re.append(elem)
    elif elem == input_str[0]: 
        elem = input_str[1]
        list_re.append(elem)
    else: 
        list_re.append(elem)

re = "".join(list_re)
print(re)