string = input()
len_string = len(string)

print(string)

for _ in range(len_string):
    string = string[-1] + string[:-1]

    print(string)