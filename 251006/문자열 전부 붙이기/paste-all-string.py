n = int(input())

string_list=[input()
    for _ in range(n)
    ]

new_string = ""
for string in string_list:
    new_string += string

print(new_string)