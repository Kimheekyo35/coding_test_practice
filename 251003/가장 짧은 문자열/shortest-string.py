string_list = [input() for _ in range(3)]
len_list = [ len(string) for string in string_list]

print(max(len_list) - min(len_list))
